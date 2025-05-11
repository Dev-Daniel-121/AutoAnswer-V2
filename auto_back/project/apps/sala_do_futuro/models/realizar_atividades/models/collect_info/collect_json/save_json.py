from .utils.config import JSON_PATH
from project import types
import json, os

class SaveJson:
    def __init__(self):
        self.json_path = JSON_PATH

        if not os.path.exists(self.json_path):
            self._init_json_file()

    def _init_json_file(self):
        base_structure = {
            'answers': {},
            'tarefas': {},
            'redacao': {},
            'prova': {},
        }
        with open(self.json_path, 'w', encoding='utf-8') as file:
            json.dump(base_structure, file, ensure_ascii=False, indent=4)

    def save_activity(self, materia, user_id, task_info, texts, questionarie):
        with open(self.json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        site_activity_id = task_info['site_activity_id']

        data[materia][site_activity_id] = {
            'task_info': task_info,
            'texts': texts,
            f'{user_id}': questionarie
        }

        with open(self.json_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f'[{types[9]}] Dados da Atividade salvos em \'{self.json_path}\' com ID \'{site_activity_id}\'.\n')
