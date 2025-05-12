from project.config import LogType

class LoginAluno:
    def __init__(
            self, page, tipo, ra, dg_ra, uf_ra, senha,
            btn_tipo_class, btn_entrar_class, input_ra_id, input_dg_ra_name, input_uf_ra_class, ul_uf_ra_class, li_uf_ra_class, input_senha_id):
        
        self.page = page
        self.tipo = tipo
        self.ra = ra
        self.dg_ra = dg_ra
        self.uf_ra = uf_ra
        self.senha = senha

        self.btn_tipo_class = btn_tipo_class
        self.btn_entrar_class = btn_entrar_class
        self.input_ra_id = input_ra_id
        self.input_dg_ra_name = input_dg_ra_name
        self.input_uf_ra_class = input_uf_ra_class
        self.ul_uf_ra_class = ul_uf_ra_class
        self.li_uf_ra_class = li_uf_ra_class
        self.input_senha_id = input_senha_id

    def btn_tipo(self):
        try:
            btn_tipo = self.page.locator(f'{self.btn_tipo_class}')
            btn_tipo.click()
        except Exception as e:
            print(f'\n[{LogType.ERROR}] Erro ao clicar no botão de tipo: {e}')

    def btn_entrar(self):
        try:
            btn_entrar = self.page.locator(f'{self.btn_entrar_class}')
            btn_entrar.click()
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao clicar no botão entrar: {e}')

    def input_ra(self):
        try:
            input_ra = self.page.locator(f'{self.input_ra_id}')
            input_ra.fill(self.ra)
        except Exception as e:
            print(f'\n[{LogType.ERROR}] Erro ao preencher o campo RA: {e}')

    def input_dg_ra(self):
        try:
            input_dg_ra = self.page.locator(f'{self.input_dg_ra_name}')
            input_dg_ra.fill(self.dg_ra)
        except Exception as e:
            print(f'\n[{LogType.ERROR}] Erro ao preencher o campo dígito do RA: {e}')

    def input_uf_ra(self):
        try:
            input_uf_ra = self.page.locator(self.input_uf_ra_class)
            input_uf_ra.click()

            self.page.wait_for_selector(f'{self.ul_uf_ra_class}')

            li_uf_ra = self.page.locator(f'{self.ul_uf_ra_class} > {self.li_uf_ra_class}[data-value=\'{self.uf_ra}\']')
            li_uf_ra.click()
        except Exception as e:
            print(f'\n[{LogType.ERROR}] Erro ao selecionar a UF do RA: {e}')

    def input_senha(self):
        try:
            input_senha = self.page.locator(f'{self.input_senha_id}')
            input_senha.fill(self.senha)
        except Exception as e:
            print(f'\n[{LogType.ERROR}] Erro ao preencher o campo de senha: {e}')

    def run(self):
        try:
            self.btn_tipo()
            self.input_ra()
            self.input_dg_ra()
            self.input_uf_ra()
            self.input_senha()
            self.btn_entrar()
            print(f'\n[{LogType.SUCCESS}] Login realizado com sucesso.')
            input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')
        except Exception as e:
            print(f'\n[{LogType.ERROR}] Erro durante o processo de login: {e}')
            input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')