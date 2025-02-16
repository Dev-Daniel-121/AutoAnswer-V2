from classes.models.data.geral import Geral
from classes.models.data.agenda import Agenda
from classes.models.data.tarefas import Tarefas

class Data:
    def __init__(self, page):
        self.page = page

    def run(self):
        geral = Geral(self.page, values_class='div.css-3vj4l0')
        geral.run()

        agenda = Agenda(self.page, row_class='div.css-4vexei', day_class='p.css-ybeji6', day_of_the_week_class='h6.css-1q42c94', day_content_class='p.css-1w3a6c9')
        agenda.run()

        tarefas = Tarefas(self.page, values_class='')
        tarefas.run()