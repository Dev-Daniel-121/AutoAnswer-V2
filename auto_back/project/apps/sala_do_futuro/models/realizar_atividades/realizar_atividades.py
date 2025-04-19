from project.apps.sala_do_futuro.models.data.tarefas import Activities, Go, Sections
from .models import DoProvas, DoRedacao, DoTarefas
from project import Display, types

class RealizarAtividades:
    def __init__(self, page):
        self.page = page
        self.display = Display
        self.doTarefas = DoTarefas(page=self.page)
        self.doRedacao = DoRedacao(page=self.page)
        self.doProvas = DoProvas(page=self.page)
        self.activities = Activities(page=self.page, total_activities_class='div.css-fm7u1u', get_component_name_class='p.css-1is68np', get_component_day_class='p.css-1d78sd9', get_component_date_class='p.css-1gwkyaz')
        self.sections = Sections(page=self.page, sections_turmas_class=':nth-match(div.css-39ukww, 1)', sections_status_class=':nth-match(div.css-39ukww, 2)', sections_componentes_class='input.css-scvshb')

    def get_task_infos(self):
        atividades = self.activities.total_activities()

        if not atividades:
            print(f'[{types[9]}] Não há atividades disponíveis.')
            return []

        task_infos = []

        for materia in atividades:
            nome_materia = self.activities.get_component_name(materia)
            dias = self.activities.get_component_day(materia)
            start_date, end_date = self.activities.get_component_date(materia)

            task_infos.append((2, f'{nome_materia} - {end_date} ({dias})'))

        task_infos.append((2, 'Sair'))

        return task_infos

    def show_task_infos(self, user):
        self.sections.run()
        options_data = self.get_task_infos()

        if not options_data:
            print(f'[{types[9]}] Nenhuma atividade encontrada.')
            return

        options = self.display(options_data, 'Realizar Atividades', answer=False, user=f'{user}', title_quest='', clear_enabled=False)
        options.display()

        user_choice = input(f'\n[{types[1]}] Digite as opções desejadas (separadas por \',\'), \'*\' para todas: ')
        return user_choice

    def select_component(self, user):
        options_data = [(2, 'Tarefas SP'), (2, 'Redação Paulista'), (2, 'Provas'), (2, 'Sair')]
        options = self.display(options_data, 'Realizar Atividades', answer=False, user=f'{user}', title_quest='')
        options.display()

        user_choice = input(f'\n[{types[1]}] Digite as opções desejadas (separadas por \',\'), \'*\' para todas: ')
        return user_choice
    
    def run(self, nome_usuario, id_usuario):
        while True:
            user_choice = self.select_component(nome_usuario).strip().lower()
            
            go = Go(
                page=self.page, get_title_class='span.css-14ra0qi', 
                btn_go_home_class=':nth-match(a.css-lumvx8, 1)',
                btn_go_tarefas_class=':nth-match(a.css-lumvx8, 2)', 
                btn_go_redacoes_class=':nth-match(a.css-lumvx8, 3)', 
                btn_go_provas_class=':nth-match(a.css-lumvx8, 4)')
            
            if user_choice == '4':
                go.go_home()
                break
            
            if user_choice in ['*', 'all']:
                user_choice = '1,2,3'
            
            choices = [choice.strip() for choice in user_choice.split(',')]
            
            for choice in choices:
                try:
                    choice_num = int(choice)
                    if choice_num == 1:
                        go.go_tarefas()
                        self.doTarefas.run(user=nome_usuario, id_usuario=id_usuario)
                    elif choice_num == 2:
                        go.go_redacoes()
                        self.doRedacao.run(user=nome_usuario, id_usuario=id_usuario)
                    elif choice_num == 3:
                        go.go_provas()
                        self.doProvas.run(user=nome_usuario, id_usuario=id_usuario)
                    elif choice_num == 4:
                        continue
                    else:
                        print(f'[{types[4]}] Opção inválida: {choice_num}')
                except ValueError:
                    print(f'[{types[4]}] Opção inválida: {choice}')
