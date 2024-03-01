from ruamel.yaml import YAML
from pathlib import Path

yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)

# Define os caminhos para os arquivos de dados específicos na pasta 'data/'
data_files = [
    'areas.yaml',
    'advisors.yaml',
    'projects.yaml',  # Adicionado projects.yaml à lista
]

# Define o caminho base para a pasta 'data/'
data_folder = Path('data/')

# Define os caminhos para os arquivos de tradução 'i18n'
i18n_paths = {
    'en': Path('i18n/en.yaml'),
    'pt': Path('i18n/pt.yaml'),
}

# Função para atualizar as traduções a partir do arquivo de advisors
def update_translations_from_advisors(advisors_file_path):
    with open(advisors_file_path, 'r', encoding='utf-8') as file:
        advisors_data = yaml.load(file)

    for lang, i18n_file_path in i18n_paths.items():
        if i18n_file_path.exists():
            with open(i18n_file_path, 'r', encoding='utf-8') as file:
                translations = yaml.load(file) or {}
        else:
            translations = {}

        for advisor_id, advisor_info in advisors_data['advisors'].items():
            translations[advisor_id] = advisor_info['name']

        with open(i18n_file_path, 'w', encoding='utf-8') as file:
            yaml.dump(translations, file)

# Função para atualizar as traduções a partir do arquivo de áreas
def update_translations_from_areas(areas_file_path):
    with open(areas_file_path, 'r', encoding='utf-8') as file:
        areas_data = yaml.load(file)

    for lang, i18n_file_path in i18n_paths.items():
        if i18n_file_path.exists():
            with open(i18n_file_path, 'r', encoding='utf-8') as file:
                translations = yaml.load(file) or {}
        else:
            translations = {}

        for area in areas_data['areas']:
            area_id = area['id']
            translations[area_id] = area['name'][lang]

        with open(i18n_file_path, 'w', encoding='utf-8') as file:
            yaml.dump(translations, file)

# Função para atualizar as traduções a partir do arquivo de projetos
def update_translations_from_projects(projects_file_path):
    with open(projects_file_path, 'r', encoding='utf-8') as file:
        projects_data = yaml.load(file)

    for lang, i18n_file_path in i18n_paths.items():
        if i18n_file_path.exists():
            with open(i18n_file_path, 'r', encoding='utf-8') as file:
                translations = yaml.load(file) or {}
        else:
            translations = {}

        for project in projects_data['projects']:
            project_id = project['id']
            translations[project_id] = project['name'][lang]

        with open(i18n_file_path, 'w', encoding='utf-8') as file:
            yaml.dump(translations, file)

# Processa cada arquivo de dados especificado
for data_file in data_files:
    full_path = data_folder / data_file
    if data_file == 'advisors.yaml':
        update_translations_from_advisors(full_path)
    elif data_file == 'areas.yaml':
        update_translations_from_areas(full_path)
    elif data_file == 'projects.yaml':  # Processamento para projects.yaml
        update_translations_from_projects(full_path)

print("Translation files have been successfully updated.")
