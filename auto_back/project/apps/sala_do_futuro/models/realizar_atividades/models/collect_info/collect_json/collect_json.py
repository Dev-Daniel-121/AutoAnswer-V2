from .utils.config import JSON_PATH
from project import LogType
import os, json

class CollectJson:
    def __init__(self):
        self.json_path = JSON_PATH

    def check_json_file(self):
        print(f'[{LogType.INFO}] Verificando se há \'Respostas Salvas\' para essa Atividade...\n')

        if not os.path.exists(self.json_path):
            print(f'[{LogType.ERROR}] O arquivo JSON não foi encontrado em {self.json_path}\n')
            return None
        
        return self.json_path

    def load_json_data(self):
        with open(self.json_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def check_component_in_responses(self, data, component):
        if component not in data['answers']:
            print(f'[{LogType.ERROR}] Componente \'{component}\' não encontrado nas respostas.\n')
            return None
        return data['answers'][component]

    def check_saved_activity(self, component_data, id_activity):
        if id_activity in component_data:
            print(f'[{LogType.SUCCESS}] Encontrado \'Respostas Salvas\' para essa Atividade!\n')
            return True
        else:
            print(f'[{LogType.ERROR}] Nenhum \'Respostas Salvas\' encontrado para essa Atividade!\n')
            return False

    def interact_with_user(self):
        response = input(f'[{LogType.QUESTION}] Usar \'data.json\'? (Y/n): ').strip().upper()
        if response == '': 
            response = 'Y'
        
        if response == 'Y':
            print(f'[{LogType.INFO}] Usando \'data.json\'\n')
        else:
            print(f'[{LogType.INFO}] \'data.json\' não será utilizado\n')

    def run(self, component, id_activity):
        json_path = self.check_json_file()
        if json_path is None:
            return None
        
        data = self.load_json_data()

        component_data = self.check_component_in_responses(data, component)
        if component_data is None:
            return None

        if self.check_saved_activity(component_data, id_activity):
            self.interact_with_user()
            return component_data[id_activity]
        
        return None
