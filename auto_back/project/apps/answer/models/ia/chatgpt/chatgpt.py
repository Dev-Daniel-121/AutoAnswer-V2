from project.apps.answer.models.ia.ia import IA
from .models import AutoGUIGPT, AutoStealphGPT

class ChatGPT(IA):
    def __init__(self, data):
        super().__init__(nome=self.__class__.__name__)
        self.data = data

        self.metodos = {
            'AutoGUI': AutoGUIGPT().working,
            'AutoStealph': AutoStealphGPT().working
        }

    def get_prompts(self):
        return self.data.get('prompts', {})