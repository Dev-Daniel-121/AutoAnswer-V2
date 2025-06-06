from .models import AutoGUIGROK, AutoStealphGROK
from project.apps.answer.models.ia.ia import IA

class Grok(IA):
    def __init__(self, data):
        super().__init__(nome=self.__class__.__name__)
        self.data = data

        self.metodos = {
            'AutoGUI': AutoGUIGROK().working,
            'AutoStealph': AutoStealphGROK().working
        }

    def get_prompts(self):
        return self.data.get('prompts', {})