from project import types

class Go:
    def __init__(self, page, btn_go_tarefas_class, go_btn_class, go_list_class):
        self.page = page
        self.btn_go_tarefas_class = btn_go_tarefas_class
        self.go_btn_class = go_btn_class
        self.go_list_class = go_list_class

    def go_tarefas(self):
        btn_go_tarefas_class = self.btn_go_tarefas_class
        btn_go_tarefas = self.page.locator(f'{btn_go_tarefas_class}')
        btn_go_tarefas.click()
    
    def go_btn(self):
        go_btn_class = self.go_btn_class
        go_btn = self.page.locator(f'{go_btn_class}')
        go_btn.click()

    def go_list(self, content):
        go_list_class = self.go_list_class

        i = 0

        if content == 'A fazer': i = 1 
        elif content == 'Entregues': i = 2
        elif content == 'Expiradas': i = 3
        else: print(f'[{types[4]}] Número inválido')

        go_list = self.page.locator(f':nth-match({go_list_class}, {i})')
        go_list.click()
    
    def go_aFazer(self):
        self.go_btn()
        self.go_list(content='A fazer')
        
    def go_entregues(self):
        self.go_btn()
        self.go_list(content='Entregues')

    def go_expiradas(self):
        self.go_btn()
        self.go_list(content='Expiradas')