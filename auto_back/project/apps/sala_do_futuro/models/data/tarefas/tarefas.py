# from .tarefas import Activities, Go, Sections
from project.apps.sala_do_futuro.models.data.tarefas.activities.activities import Activities
from project.apps.sala_do_futuro.models.data.tarefas.go.go import Go
from project.apps.sala_do_futuro.models.data.tarefas.sections.sections import Sections
from project import types

class Tarefas:
    def __init__(self, page):
        self.page = page

    def run(self):
        go = Go(self.page, btn_go_tarefas_class=':nth-match(a.css-lumvx8, 2)', go_btn_class=':nth-match(div.css-39ukww, 2)', go_list_class='li.css-4dqmvd')

        sections = Sections(self.page)

        activities = Activities(
            self.page,
            container_activities_class='div.css-1h77wgb', box_activities_class='div.css-wiwm8n', activities_component_class='p.css-9kams2', activities_dates_class='p.css-1d78sd9'
        )

        go.go_tarefas()

        go.go_aFazer()
        sections.run()
        activities.run()

        input(f'\n[{types[6]}] Pressione Enter para continuar...')


        go.go_entregues()
        sections.run()
        activities.run()

        input(f'\n[{types[6]}] Pressione Enter para continuar...')

        go.go_expiradas()
        sections.run()
        activities.run()

        input(f'\n[{types[6]}] Pressione Enter para continuar...')

