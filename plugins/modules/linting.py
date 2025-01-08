import os
import yaml

class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)

directory_path = '/Users/fmunoz/Desktop/Work/Github/Meraki/dashboard-api-ansible/plugins/modules/'

# Recorrer todos los archivos en el directorio
for filename in os.listdir(directory_path):
    if filename.endswith('.py'):
        file_path = os.path.join(directory_path, filename)
        
        with open(file_path, 'r') as file:
            lines = file.readlines()

        new_lines = []
        inside_yaml = False
        yaml_content = ""
        yaml_type = ""

        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith('DOCUMENTATION = r"""') or stripped_line.startswith('EXAMPLES = r"""'):
                inside_yaml = True
                yaml_type = 'DOCUMENTATION' if stripped_line.startswith('DOCUMENTATION = r"""') else 'EXAMPLES'
                yaml_content = stripped_line[len(f'{yaml_type} = r"""'):] + "\n"
            elif inside_yaml:
                if stripped_line.endswith('"""'):
                    inside_yaml = False
                    yaml_content += stripped_line[:-len('"""')] + "\n"
                    try:
                        # Asegurarse de que el contenido YAML esté correctamente delimitado
                        if yaml_content.strip():
                            yaml_data = yaml.safe_load(yaml_content)
                            formatted_yaml = yaml.dump(yaml_data, Dumper=IndentDumper, default_flow_style=False, indent=2, sort_keys=False)
                            new_lines.append(f'{yaml_type} = r"""\n' + formatted_yaml + '"""\n')
                        else:
                            new_lines.append(f'{yaml_type} = r"""\n' + yaml_content + '"""\n')
                    except yaml.YAMLError as exc:
                        print(f"Error al procesar el YAML en {filename}: {exc}")
                        new_lines.append(f'{yaml_type} = r"""\n' + yaml_content + '"""\n')
                else:
                    yaml_content += line
            else:
                new_lines.append(line)

        with open(file_path, 'w') as file:
            file.writelines(new_lines)
        
        print(f"Modificación completada en {filename}.")




# # Recorrer todos los archivos en el directorio
# for filename in os.listdir(directory_path):
#     if filename.endswith('.yml') or filename.endswith('.yaml'):
#         file_path = os.path.join(directory_path, filename)
        
#         with open(file_path, 'r') as file:
#             try:
#                 yaml_content = yaml.safe_load(file)
#             except yaml.YAMLError as exc:
#                 print(f"Error al procesar el archivo {filename}: {exc}")
#                 continue

#         # Formatear el YAML
#         formatted_yaml = yaml.dump(yaml_content, Dumper=IndentDumper, default_flow_style=False, indent=2, sort_keys=False)

#         with open(file_path, 'w') as file:
#             file.write(formatted_yaml)
        
#         print(f"Modificación completada en {filename}.")