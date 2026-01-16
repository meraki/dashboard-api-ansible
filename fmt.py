import os
import re
import subprocess

def process_files(directory):
    for root, _dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                process_file(os.path.join(root, file))

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    sections = ['DOCUMENTATION', 'EXAMPLES', 'RETURN']
    for section in sections:
        content = process_section(content, section)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

def process_section(content, section):
    pattern = rf'{section} = r""".*?"""'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        section_content = match.group(0)
        yaml_content = section_content.split('r"""')[1].rsplit('"""', 1)[0].strip()

        if section == 'DOCUMENTATION' or section == 'EXAMPLES':
            with open('tmp.yaml', 'w', encoding='utf-8') as tmp_file:
                tmp_file.write(yaml_content)

            # subprocess.run(['yamlfmt', 'tmp.yaml'])
            subprocess.run(['yamlfmt', 'tmp.yaml', '-conf', '.yamlfmt'], check=False)

            with open('tmp.yaml', 'r', encoding='utf-8') as tmp_file:
                formatted_content = tmp_file.read()

            os.remove('tmp.yaml')
        else:
            formatted_content = yaml_content

        if section == 'DOCUMENTATION':
            formatted_content = update_notes_section(formatted_content)

        formatted_content = re.sub(r'\n\s*\n', '\n', formatted_content).strip()
        new_section_content = f'{section} = r"""\n{formatted_content}\n"""'
        content = content.replace(section_content, new_section_content)

    return content

def update_notes_section(content):
    notes_pattern = re.compile(r'notes:\n(  - .*\n)+', re.DOTALL)
    match = notes_pattern.search(content)
    if match:
        notes_content = match.group(0)
        # Ensure correct indentation and line breaks
        updated_notes = re.sub(r',\s*', ',\n    ', notes_content)
        updated_notes = re.sub(r'(\n\s+)-\s+(SDK Method used are|Paths used are)', r'\n  - \2\n   ', updated_notes)
        # Ensure the closing triple quotes are on a new line without spaces
        updated_notes = re.sub(r'\n\s*"""', '\n"""', updated_notes)
        content = content.replace(notes_content, updated_notes)
    else:
        print('No notes section found in DOCUMENTATION')
    return content


if __name__ == "__main__":
    directory = "/Users/franciscomunozmiranda/Desktop/Work/GitHub/dashboard-api-ansible/plugins/modules"
    process_files(directory)
