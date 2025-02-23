from project import types

class Go:
    def __init__(
            self, page, 
            get_title_class, btn_go_home_class, btn_go_tarefas_class, btn_go_redacoes_class, btn_go_provas_class, 
            go_btn_class, go_list_class):
        self.page = page
        self.get_title_class = get_title_class
        self.btn_go_home_class = btn_go_home_class
        self.btn_go_tarefas_class = btn_go_tarefas_class
        self.btn_go_redacoes_class = btn_go_redacoes_class
        self.btn_go_provas_class = btn_go_provas_class
        self.go_btn_class = go_btn_class
        self.go_list_class = go_list_class

    def get_title(self, get_title_position):
        try:
            get_title = self.page.locator(f':nth-match({self.get_title_class}, {get_title_position})').inner_text()

            print(f'\n~~~~~~ {get_title.upper()} ~~~~~~')
        except Exception as e:
            print(f'[{types[4]}] Erro ao pegar título: {e}')

    def go_home(self):
        try:
            btn_go_home = self.page.locator(f'{self.btn_go_home_class}')
            btn_go_home.click()
        except Exception as e:
            print(f'[{types[4]}] Erro ao ir para Tarefas: {e}')

    def go_tarefas(self):
        try:
            btn_go_tarefas = self.page.locator(f'{self.btn_go_tarefas_class}')
            btn_go_tarefas.click()

            self.get_title(get_title_position=2)
        except Exception as e:
            print(f'[{types[4]}] Erro ao ir para Tarefas: {e}')

    def go_redacoes(self):
        try:
            btn_go_redacoes = self.page.locator(f'{self.btn_go_redacoes_class}')
            btn_go_redacoes.click()

            self.get_title(get_title_position=3)
        except Exception as e:
            print(f'[{types[4]}] Erro ao ir para Redações: {e}')

    def go_provas(self):
        try:
            btn_go_provas = self.page.locator(f'{self.btn_go_provas_class}')
            btn_go_provas.click()

            self.get_title(get_title_position=4)
        except Exception as e:
            print(f'[{types[4]}] Erro ao ir para Provas: {e}')
    
    def go_btn(self):
        try:
            go_btn = self.page.locator(f'{self.go_btn_class}')
            go_btn.click()
        except Exception as e:
            print(f'[{types[4]}] Erro ao clicar no botão principal: {e}')

    def go_list(self, content):
        i = 0

        if content == 'A fazer': i = 1 
        elif content == 'Entregues': i = 2
        elif content == 'Expiradas': i = 3
        else: print(f'[{types[4]}] Conteúdo inválido: \'{content}\'')

        try:
            go_list = self.page.locator(f':nth-match({self.go_list_class}, {i})')
            go_list.click()
        except Exception as e:
            print(f'[{types[4]}] Erro ao clicar na lista de {content}: {e}')
    
    def go_aFazer(self):
        self.go_btn()
        self.go_list(content='A fazer')
        
    def go_entregues(self):
        self.go_btn()
        self.go_list(content='Entregues')

    def go_expiradas(self):
        self.go_btn()
        self.go_list(content='Expiradas')