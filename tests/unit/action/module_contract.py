"""
Offline contract checks for every action plugin in this checkout.

Nothing here talks to the Meraki API. A fake DashboardAPI stands in for
the SDK and validates every call against the real SDK installed in the
environment (its method signatures and its body/query parameter lists).

Used by test_all_modules.py (pytest) and runnable on its own to print a
categorised report:

    python tests/unit/action/module_contract.py [--json out.json]
"""

import ast
import copy
import importlib
import inspect
import os
import re
import sys
import tempfile
from functools import lru_cache
from pathlib import Path
from unittest.mock import MagicMock, patch

# MERAKI_COLLECTION_ROOT lets the same checks run against another copy of the
# collection, e.g. ~/.ansible/collections/ansible_collections/cisco/meraki
REPO = Path(os.environ.get("MERAKI_COLLECTION_ROOT") or Path(__file__).resolve().parents[3])
ACTION_DIR = REPO / "plugins" / "action"
MODULE_DIR = REPO / "plugins" / "modules"
PKG = "ansible_collections.cisco.meraki"

# Options injected by the meraki doc fragment / meraki_argument_spec().
COMMON_PREFIX = "meraki_"


# --------------------------------------------------------------------------
# Import the collection from this checkout (not from ~/.ansible/collections)
# --------------------------------------------------------------------------

def _setup_import_path():
    if getattr(_setup_import_path, "done", False):
        return
    utils = None
    search = list(sys.path)
    search += os.environ.get("ANSIBLE_COLLECTIONS_PATH", "").split(os.pathsep)
    search.append(str(Path.home() / ".ansible" / "collections"))
    for p in filter(None, search):
        cand = Path(p) / "ansible_collections" / "ansible" / "utils"
        if cand.is_dir():
            utils = cand
            break
    root = Path(tempfile.mkdtemp(prefix="meraki_contract_"))
    ac = root / "ansible_collections"
    (ac / "cisco").mkdir(parents=True)
    (ac / "__init__.py").touch()
    (ac / "cisco" / "__init__.py").touch()
    os.symlink(REPO, ac / "cisco" / "meraki")
    if utils is not None:
        (ac / "ansible").mkdir()
        (ac / "ansible" / "__init__.py").touch()
        os.symlink(utils, ac / "ansible" / "utils")
    for name in [m for m in sys.modules if m == "ansible_collections" or m.startswith("ansible_collections.")]:
        del sys.modules[name]
    sys.path.insert(0, str(root))
    _setup_import_path.done = True


# --------------------------------------------------------------------------
# SDK introspection
# --------------------------------------------------------------------------

@lru_cache(maxsize=None)
def _dashboard():
    import meraki
    return meraki.DashboardAPI(api_key="0" * 40, suppress_logging=True,
                               output_log=False, print_console=False)


@lru_cache(maxsize=None)
def sdk_method(family, function):
    fam = getattr(_dashboard(), family, None)
    if fam is None:
        return None
    return getattr(type(fam), function, None)


@lru_cache(maxsize=None)
def sdk_contract(family, function):
    """(required, accepted) parameter names for an SDK operation."""
    m = sdk_method(family, function)
    sig = inspect.signature(m)
    required, accepted = set(), set()
    for name, p in list(sig.parameters.items())[1:]:  # skip self
        if p.kind in (p.VAR_KEYWORD, p.VAR_POSITIONAL):
            continue
        accepted.add(name)
        if p.default is p.empty:
            required.add(name)
    src = inspect.getsource(m)
    for lst in re.findall(r"(?:body_params|query_params|array_params)\s*=\s*\[([^\]]*)\]", src):
        accepted.update(re.findall(r"""['"]([^'"]+)['"]""", lst))
    # Multipart uploads and pagination helpers handled by the SDK itself
    accepted.update({"total_pages", "direction", "multipart_fields",
                     "multipart_monitor_callback"})
    return frozenset(required), frozenset(accepted)


# --------------------------------------------------------------------------
# Plugin discovery
# --------------------------------------------------------------------------

def action_names():
    return sorted(p.stem for p in ACTION_DIR.glob("*.py") if p.stem != "__init__")


def module_names():
    return sorted(p.stem for p in MODULE_DIR.glob("*.py") if p.stem != "__init__")


def load_action(name):
    _setup_import_path()
    return importlib.import_module("%s.plugins.action.%s" % (PKG, name))


@lru_cache(maxsize=None)
def static_calls(name):
    """Every exec_meraki(family=..., function=...) call site in the file."""
    tree = ast.parse((ACTION_DIR / (name + ".py")).read_text())
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, "attr", None) == "exec_meraki":
            kw = {k.arg: k.value for k in node.keywords}
            fam, fn = kw.get("family"), kw.get("function")
            if isinstance(fam, ast.Constant) and isinstance(fn, ast.Constant):
                calls.append((fam.value, fn.value, node.lineno))
    return calls


def branch_keys(name):
    """Args an info plugin branches on (id = self._task.args.get("X"))."""
    src = (ACTION_DIR / (name + ".py")).read_text()
    return sorted(set(re.findall(r'\bid = self\._task\.args\.get\("(\w+)"\)', src)))


# --------------------------------------------------------------------------
# Argument generation
# --------------------------------------------------------------------------

def _dummy(spec, mutate=False):
    t = spec.get("type", "str")
    if spec.get("choices"):
        ch = list(spec["choices"])
        return ch[1 % len(ch)] if mutate else ch[0]
    if t == "dict":
        sub = spec.get("options")
        return build_args(sub, mutate) if sub else ({"k": "Y2"} if mutate else {"k": "X1"})
    if t == "list":
        el = spec.get("elements", "str")
        if el == "dict":
            sub = spec.get("options")
            return [build_args(sub, mutate) if sub else {"k": "X1"}]
        return [_dummy({"type": el}, mutate)]
    if t == "int":
        return 2 if mutate else 1
    if t == "float":
        return 2.0 if mutate else 1.0
    if t == "bool":
        return not mutate
    return "Y2" if mutate else "X1"


def build_args(spec, mutate=False):
    out = {}
    for k, v in (spec or {}).items():
        if k.startswith(COMMON_PREFIX) or k == "state":
            continue
        out[k] = _dummy(v, mutate)
    return out


# --------------------------------------------------------------------------
# Fake SDK
# --------------------------------------------------------------------------

class Recorder:
    def __init__(self, mode, echo):
        self.mode = mode          # "empty" | "same" | "diff"
        self.echo = echo          # object returned by GETs in same/diff
        self.calls = []
        self.violations = []

    def call(self, family, function, params):
        self.calls.append((family, function))
        m = sdk_method(family, function)
        if m is None:
            self.violations.append(("missing_sdk_function", family, function, None))
            return {}
        required, accepted = sdk_contract(family, function)
        missing = sorted(required - set(params))
        if missing:
            self.violations.append(("missing_required", family, function, missing))
        unknown = sorted(set(params) - accepted)
        if unknown:
            self.violations.append(("dropped_by_sdk", family, function, unknown))
        if function.startswith("get"):
            return [] if self.mode == "empty" else copy.deepcopy(self.echo)
        return {"id": "X1"}


class _Family:
    def __init__(self, rec, family):
        self._rec, self._family = rec, family

    def __getattr__(self, function):
        def _call(**params):
            return self._rec.call(self._family, function, params)
        return _call


class _Api:
    def __init__(self, rec):
        self._rec = rec

    def __getattr__(self, family):
        return _Family(self._rec, family)


# --------------------------------------------------------------------------
# Running a plugin
# --------------------------------------------------------------------------

def run_plugin(name, args, rec):
    """Run ActionModule.run() with the fake SDK. Returns (outcome, detail)."""
    from ansible.errors import AnsibleActionFail
    from ansible.plugins.action import ActionBase
    mod = load_action(name)
    meraki_utils = importlib.import_module(PKG + ".plugins.plugin_utils.meraki")

    def fake_init(self, params):
        self.result = dict(changed=False, result="")
        self._params = params
        self.api = _Api(rec)

    task = MagicMock()
    task.args = copy.deepcopy(args)
    task.args.setdefault("meraki_api_key", "0" * 40)
    task.action = "cisco.meraki." + name
    task.async_val = 0
    task.check_mode = False
    am = mod.ActionModule(task=task, connection=MagicMock(), play_context=MagicMock(),
                          loader=MagicMock(), templar=MagicMock(),
                          shared_loader_obj=MagicMock())
    with patch.object(meraki_utils.MERAKI, "__init__", fake_init), \
            patch.object(ActionBase, "run", return_value={}):
        try:
            am.run(task_vars={})
            return "ok", None
        except AnsibleActionFail as e:
            return "action_fail", str(e)[:200]
        except Exception as e:  # noqa: BLE001 - a crash is exactly what we look for
            if type(e).__name__ == "InconsistentParameters":
                return "action_fail", str(e)[:200]
            return "crash", "%s: %s" % (type(e).__name__, str(e)[:200])


def scenarios(name):
    """(label, args, mode, echo) combinations that exercise every branch."""
    mod = load_action(name)
    spec = mod.argument_spec
    full = build_args(spec)
    diff = build_args(spec, mutate=True)
    out = []
    states = spec.get("state", {}).get("choices") if "state" in spec else None
    if states:
        same_echo = dict(full, id="X1")
        diff_echo = dict(diff, id="X1")
        for st in states:
            a = dict(full, state=st)
            out.append(("%s/empty" % st, a, "empty", None))
            out.append(("%s/same" % st, a, "same", same_echo))
            out.append(("%s/diff" % st, a, "diff", diff_echo))
    else:
        echo = dict(full, id="X1")
        out.append(("full", full, "same", echo))
        keys = branch_keys(name)
        if keys:
            reduced = {k: v for k, v in full.items() if k not in keys}
            out.append(("without:" + ",".join(keys), reduced, "same", echo))
    return out


def check_plugin(name):
    """Full report for one plugin."""
    report = {"name": name, "import_error": None, "crashes": [], "violations": set(),
              "uncovered": [], "missing_sdk": [], "required_not_in_argspec": [],
              "required_optional_in_argspec": []}
    try:
        mod = load_action(name)
        spec = mod.argument_spec
    except Exception as e:  # noqa: BLE001
        report["import_error"] = "%s: %s" % (type(e).__name__, e)
        return report

    # Static: every call site exists in the SDK
    for fam, fn, line in static_calls(name):
        if sdk_method(fam, fn) is None:
            report["missing_sdk"].append("%s.%s (line %d)" % (fam, fn, line))
            continue
        required, _accepted = sdk_contract(fam, fn)
        for r in sorted(required):
            if r not in spec:
                report["required_not_in_argspec"].append("%s: %s" % (fn, r))
            elif not spec[r].get("required"):
                report["required_optional_in_argspec"].append("%s: %s" % (fn, r))

    # Dynamic
    called = set()
    for label, args, mode, echo in scenarios(name):
        rec = Recorder(mode, echo)
        outcome, detail = run_plugin(name, args, rec)
        called.update(rec.calls)
        if outcome == "crash":
            report["crashes"].append("%s -> %s" % (label, detail))
        for kind, fam, fn, extra in rec.violations:
            report["violations"].add((kind, fn, tuple(extra) if extra else ()))
    report["violations"] = sorted(report["violations"])
    report["uncovered"] = sorted({"%s.%s" % (f, fn) for f, fn, _line in static_calls(name)
                                  if (f, fn) not in called and sdk_method(f, fn) is not None})
    return report


# --------------------------------------------------------------------------
# Documentation
# --------------------------------------------------------------------------

def doc_options(name):
    import yaml
    src = (MODULE_DIR / (name + ".py")).read_text()
    tree = ast.parse(src)
    docs = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and \
                isinstance(node.targets[0], ast.Name) and isinstance(node.value, ast.Constant):
            docs[node.targets[0].id] = node.value.value
    doc = yaml.safe_load(docs.get("DOCUMENTATION", "")) or {}
    yaml.safe_load(docs.get("EXAMPLES", "") or "[]")
    return doc


@lru_cache(maxsize=None)
def fragment_options(frag):
    """Options contributed by plugins/doc_fragments/<frag>.py."""
    import yaml
    path = REPO / "plugins" / "doc_fragments" / (frag + ".py")
    if not path.exists():
        return frozenset()
    opts = set()
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant) \
                and isinstance(node.value.value, str):
            try:
                opts |= set((yaml.safe_load(node.value.value) or {}).get("options") or {})
            except Exception:  # noqa: BLE001
                pass
    return frozenset(opts)


def check_docs(name):
    problems = []
    if not (MODULE_DIR / (name + ".py")).exists():
        return ["no module documentation file plugins/modules/%s.py" % name]
    try:
        doc = doc_options(name)
    except Exception as e:  # noqa: BLE001
        return ["DOCUMENTATION/EXAMPLES do not parse: %s" % str(e)[:150]]
    spec = load_action(name).argument_spec
    documented = set((doc.get("options") or {}).keys())
    frags = doc.get("extends_documentation_fragment") or []
    for frag in [frags] if isinstance(frags, str) else frags:
        documented |= fragment_options(frag.split(".")[-1])
    documented = {k for k in documented if not k.startswith(COMMON_PREFIX)}
    declared = {k for k in spec if not k.startswith(COMMON_PREFIX)}
    if declared - documented:
        problems.append("options not documented: %s" % sorted(declared - documented))
    if documented - declared:
        problems.append("documented but not accepted: %s" % sorted(documented - declared))
    return problems


# --------------------------------------------------------------------------
# CLI report
# --------------------------------------------------------------------------

def main():
    import json
    _setup_import_path()
    out = {"actions": {}, "docs": {}, "modules_without_action": []}
    names = action_names()
    for i, n in enumerate(names, 1):
        r = check_plugin(n)
        r["docs"] = check_docs(n) if not r["import_error"] else []
        out["actions"][n] = r
        if i % 100 == 0:
            print("  %d/%d" % (i, len(names)), file=sys.stderr)
    acts = set(names)
    out["modules_without_action"] = [m for m in module_names()
                                     if m not in acts and not m.startswith("meraki_")]
    if "--json" in sys.argv:
        path = sys.argv[sys.argv.index("--json") + 1]
        with open(path, "w") as f:
            json.dump(out, f, indent=1, default=list)
    A = out["actions"].values()

    def count(key):
        return sum(1 for r in A if r[key])
    print("plugins:", len(names))
    for key in ("import_error", "missing_sdk", "crashes", "violations",
                "required_not_in_argspec", "docs", "uncovered"):
        print("  %-28s %d" % (key, count(key)))
    print("  modules_without_action       %d" % len(out["modules_without_action"]))


if __name__ == "__main__":
    main()
