# from models import Agenda, Geral
# from models import Tarefas
from project.apps.sala_do_futuro.models.data.agenda import Agenda
from project.apps.sala_do_futuro.models.data.geral import Geral
from project.apps.sala_do_futuro.models.data.tarefas import Tarefas
from project import types
import os

class Data:
    def __init__(self, page):
        self.page = page

    def run(self):
        
        os.system('cls' if os.name == 'nt' else 'clear')

        geral = Geral(self.page, values_class='p.css-3vj4l0', pendencias_box_class=':nth-match(div.css-rpybyc, 1)', pendencias_box_close_class='button.css-1u9fbqd', pendencias_p_elements='p.css-1f9zvnk', pendencias_b_elements='b')
        geral.run()
        
        input(f'\n[{types[6]}] Pressione Enter para continuar...')

        os.system('cls' if os.name == 'nt' else 'clear')

        agenda = Agenda(self.page, row_class='div.css-4vexei', day_class='p.css-ybeji6', day_of_the_week_class='h6.css-1q42c94', day_content_class='p.css-1w3a6c9')
        agenda.run()
        
        input(f'\n[{types[6]}] Pressione Enter para continuar...')

        os.system('cls' if os.name == 'nt' else 'clear')
        
        input(f'\n[{types[6]}] Pressione Enter para continuar...')

        tarefas = Tarefas(self.page)
        tarefas.run()
        