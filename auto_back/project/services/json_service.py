from project.utils import JSONHandler
from project import LogType
import json

class JSONService:
    def __init__(self, file_path):
        self.file_path = file_path
        self.json_handler = JSONHandler(file_path)

    def carregar_dados(self):
        return self.json_handler.carregar()

    def salvar_dados(self, data):
        return self.json_handler.salvar(data)

    def validar_json(self, data):
        try:
            json.dumps(data)
            return True
        except (TypeError, ValueError):
            print(f'[{LogType.ERROR}] Dados inválidos para JSON.')
            return False