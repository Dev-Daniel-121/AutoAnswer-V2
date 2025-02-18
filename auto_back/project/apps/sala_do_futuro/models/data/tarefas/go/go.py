class Go:
    def __init__(self, page, btn_go_tarefas_class, container_go_class, btn_go_class, list_go_class):
        self.page = page
        self.btn_go_tarefas_class = btn_go_tarefas_class
        self.container_go_class = container_go_class
        self.btn_go_class = btn_go_class
        self.list_go_class = list_go_class

    def go_tarefas(self):
        btn_go_tarefas_class = self.btn_go_tarefas_class
        btn_go_tarefas = self.page.locator(f'{btn_go_tarefas_class}')
        btn_go_tarefas.click()

    def go_click(self):
        container = self.page.locator(self.container_go_class)
        if container.count() < 1:
            btn_go = self.page.locator(self.btn_go_class)
            btn_go.click()

    def go_list(self, content):
        container = self.page.locator(self.container_go_class).all()
        for item in container:
            if item.locator(self.list_go_class).text_content() == content:
                item.click()

    def go_aFazer(self):
        self.go_click()
        self.go_list(content='A fazer')

    def go_entregues(self):
        self.go_click()
        self.go_list(content='Entregues')

    def go_expiradas(self):
        self.go_click()
        self.go_list(content='Expiradas')