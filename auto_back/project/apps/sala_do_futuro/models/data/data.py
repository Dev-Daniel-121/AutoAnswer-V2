from project.apps.sala_do_futuro.models.data import Geral, Agenda, Tarefas
from project import LogType
import os

class Data:
    def __init__(self, page):
        self.page = page

    def data_geral(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        geral = Geral(page=self.page, values_class='p.css-3vj4l0', pendencias_box_class=':nth-match(div.css-rpybyc, 1)', pendencias_box_close_class='button.css-1u9fbqd', pendencias_p_elements='p.css-1f9zvnk', pendencias_b_elements='b')
        geral.run()
        
        input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')

        os.system('cls' if os.name == 'nt' else 'clear')

        agenda = Agenda(page=self.page, row_class='div.css-4vexei', day_class='p.css-ybeji6', day_of_the_week_class='h6.css-1q42c94', day_content_class='p.css-1w3a6c9')
        agenda.run()
        
        input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')

        os.system('cls' if os.name == 'nt' else 'clear')

        tarefas = Tarefas(page=self.page)
        tarefas.run()
        
        input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')

    def run(self):
        self.data_geral()