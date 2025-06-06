from .utils.answer_data_json import ANSWER_DATA_JSON
from .chatgpt import ChatGPT
from project import LogType
from .grok import Grok
import json

class IAHandler:
    def __init__(self):
        self.ia_classes = {
            'chatgpt': ChatGPT,
            'grok': Grok
        }
        self.data = self.load_json()

    def load_json(self):
        try:
            with open(ANSWER_DATA_JSON, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f'[{LogType.ERROR}] Arquivo não encontrado: {ANSWER_DATA_JSON}')
            return {}
        except json.JSONDecodeError:
            print(f'[{LogType.ERROR}] Erro ao decodificar JSON: {ANSWER_DATA_JSON}')
            return {}

    def get_ias(self):
        ias = []
        for name, cls in self.ia_classes.items():
            ia_data = self.data.get('ia', {}).get(name, {})
            ias.append(cls(ia_data))
        return ias
