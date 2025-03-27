from project.apps.sala_do_futuro.models.data.tarefas import Go
from .models import do_provas, do_redacao, do_tarefas
from project import Display, types

class RealizarAtividades:
    def __init__(self, page):
        self.page = page
        self.display = Display
        self.do_tarefas = do_tarefas.DoTarefas(page=self.page)
        self.do_redacao = do_redacao.DoRedacao(page=self.page)
        self.do_provas = do_provas.DoProvas(page=self.page)

    def select_component(self, user):
        options_data = [(2, 'Tarefas SP'), (2, 'Redação Paulista'), (2, 'Provas'), (2, 'Sair')]
        options = self.display(options_data, 'Realizar Atividades', answer=False, user=f'{user}', title_quest='')
        options.display()

        user_choice = input(f'\n[{types[1]}] Digite as opções desejadas (separadas por vírgula), \'*\' para todas: ')
        return user_choice
    
    def run(self, nome_usuario, id_usuario):
        while True:
            user_choice = self.select_component(nome_usuario).strip().lower()
            
            go = Go(
                page=self.page, get_title_class='span.css-14ra0qi', 
                btn_go_home_class=':nth-match(a.css-lumvx8, 1)',
                btn_go_tarefas_class=':nth-match(a.css-lumvx8, 2)', 
                btn_go_redacoes_class=':nth-match(a.css-lumvx8, 3)', 
                btn_go_provas_class=':nth-match(a.css-lumvx8, 4)', 
                go_btn_class=':nth-match(div.css-39ukww, 2)', 
                go_list_class='li.css-4dqmvd')
            
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
                        self.do_tarefas.run(id_usuario=id_usuario)
                    elif choice_num == 2:
                        go.go_redacoes()
                        self.do_redacao.run(id_usuario=id_usuario)
                    elif choice_num == 3:
                        go.go_provas()
                        self.do_provas.run(id_usuario=id_usuario)
                    elif choice_num == 4:
                        continue
                    else:
                        print(f'[{types[4]}] Opção inválida: {choice_num}')
                except ValueError:
                    print(f'[{types[4]}] Opção inválida: {choice}')
            