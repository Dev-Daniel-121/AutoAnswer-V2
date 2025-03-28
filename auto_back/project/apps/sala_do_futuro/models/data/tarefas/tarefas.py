from project.apps.sala_do_futuro.models.data.tarefas import Activities, Go, Sections
from project import types
import os

class Tarefas:
    def __init__(self, page):
        self.page = page

    def run_tarefas(self, go, sections, activities):
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

    def run_redacoes(self, go, sections, activities):
        go.go_redacoes()

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

    def run_provas(self, go, sections, activities):
        go.go_provas()

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

    def run(self):
        go = Go(
            page=self.page, get_title_class='span.css-14ra0qi', 
            btn_go_home_class=':nth-match(a.css-lumvx8, 1)',
            btn_go_tarefas_class=':nth-match(a.css-lumvx8, 2)', 
            btn_go_redacoes_class=':nth-match(a.css-lumvx8, 3)', btn_go_provas_class=':nth-match(a.css-lumvx8, 4)', 
            go_btn_class=':nth-match(div.css-39ukww, 2)', go_list_class='li.css-4dqmvd')

        sections = Sections(page=self.page, sections_turmas_class=':nth-match(div.css-39ukww, 1)', sections_status_class=':nth-match(div.css-39ukww, 2)', sections_componentes_class='input.css-scvshb')

        activities = Activities(page=self.page, total_activities_class='div.css-fm7u1u', get_component_name_class='p.css-9kams2', get_component_day_class='p.css-1d78sd9', get_component_date_class='p.css-1gwkyaz')

        os.system('cls' if os.name == 'nt' else 'clear')

        self.run_tarefas(go=go, sections=sections, activities=activities)

        os.system('cls' if os.name == 'nt' else 'clear')

        self.run_redacoes(go=go, sections=sections, activities=activities)

        os.system('cls' if os.name == 'nt' else 'clear')

        self.run_provas(go=go, sections=sections, activities=activities)

        go.go_home()
