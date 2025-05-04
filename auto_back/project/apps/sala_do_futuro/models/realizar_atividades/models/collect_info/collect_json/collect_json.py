from project import types
import json, os

class CollectJson:
    def __init__(self):
        pass

    def check_json_file(self):
        print(f'[{types[9]}] Vericando se há \'Respostas Salvas\' para essa Atividade...\n')
        
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        json_path = os.path.join(base_dir, 'data', 'data.json')

        if not os.path.exists(json_path):
            print(f'[{types[4]}] O arquivo JSON não foi encontrado em {json_path}\n')
            return None
        
        return json_path

    def load_json_data(self, json_path):
        with open(json_path, 'r') as file:
            return json.load(file)

    def check_component_in_responses(self, data, component):
        if component not in data['answers']:
            print(f'[{types[4]}] Componente \'{component}\' não encontrado nas respostas.\n')
            return None
        
        return data['answers'][component]

    def check_saved_activity(self, component_data, id_activity):
        if id_activity in component_data:
            print(f'[{types[7]}] Encontrado \'Respostas Salvas\' para essa Atividade!\n')
            return True
        else:
            print(f'[{types[4]}] Nenhum \'Respostas Salvas\' encontrado para essa Atividade!\n')
            return False

    def interact_with_user(self):
        response = input(f'[{types[0]}] Usar \'data.json\'? (Y/n): ').strip().upper()
        if response == '': 
            response = 'Y'
        
        if response == 'Y':
            print('Usando \'data.json\'\n')
        else:
            print('\'data.json\' não será utilizado\n')

    def run(self, component, id_activity):
        json_path = self.check_json_file()
        if json_path is None:
            return
        
        data = self.load_json_data(json_path)
        component_data = self.check_component_in_responses(data, component)
        if component_data is None:
            return
        
        if self.check_saved_activity(component_data, id_activity):
            self.interact_with_user()
