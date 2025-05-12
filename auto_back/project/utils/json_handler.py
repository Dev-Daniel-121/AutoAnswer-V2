from project import LogType
import json, os

class JSONHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def carregar(self):
        try:
            if not os.path.exists(os.path.dirname(self.file_path)):
                os.makedirs(os.path.dirname(self.file_path))
            
            if not os.path.exists(self.file_path):
                return {}
            
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f'[{LogType.ERROR}] Arquivo {self.file_path} está mal formatado.')
            input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')
            return {}
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao carregar o arquivo {self.file_path}: {e}')
            input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')
            return {}

    def salvar(self, data):
        try:
            if not os.path.exists(os.path.dirname(self.file_path)):
                os.makedirs(os.path.dirname(self.file_path))
            
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False)
            
            self.carregar()
            return True
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao salvar o arquivo {self.file_path}: {e}')
            input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')
            return False