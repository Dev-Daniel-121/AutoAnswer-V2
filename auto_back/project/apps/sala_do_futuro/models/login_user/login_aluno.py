from project.config import types

class LoginAluno:
    def __init__(
            self, page, tipo, ra, dg_ra, uf_ra, senha,
            btn_tipo_class, input_ra_id, input_dg_ra_name, input_uf_ra_class, li_uf_ra_class, input_senha_id):
        
        self.page = page
        self.tipo = tipo
        self.ra = ra
        self.dg_ra = dg_ra
        self.uf_ra = uf_ra
        self.senha = senha

        self.btn_tipo_class = btn_tipo_class
        self.input_ra_id = input_ra_id
        self.input_dg_ra_name = input_dg_ra_name
        self.input_uf_ra_class = input_uf_ra_class
        self.li_uf_ra_class = li_uf_ra_class
        self.input_senha_id = input_senha_id

    def btn_tipo(self):
        try:
            btn = self.page.locator(f':nth-match({self.btn_tipo_class}, 1)')
            btn.click()
        except Exception as e:
            print(f"\n[{types[4]}] Erro ao clicar no botão de tipo: {e}")

    def input_ra(self):
        try:
            input_ra = self.page.locator(f'{self.input_ra_id}')
            input_ra.fill(self.ra)
        except Exception as e:
            print(f"\n[{types[4]}] Erro ao preencher o campo RA: {e}")

    def input_dg_ra(self):
        try:
            input_dg_ra = self.page.locator(f'{self.input_dg_ra_name}')
            input_dg_ra.fill(self.dg_ra)
        except Exception as e:
            print(f"\n[{types[4]}] Erro ao preencher o campo dígito do RA: {e}")

    def input_uf_ra(self):
        try:
            input_uf_ra = self.page.locator(f'{self.input_uf_ra_class}')
            input_uf_ra.click()

            li_uf_ra = self.page.locator(f'{self.li_uf_ra_class}')
            li_uf_ra.select_option(value=self.uf_ra)
        except Exception as e:
            print(f"\n[{types[4]}] Erro ao selecionar a UF do RA: {e}")

    def input_senha(self):
        try:
            input_senha = self.page.locator(f'{self.input_senha_id}')
            input_senha.fill(self.senha)
        except Exception as e:
            print(f"\n[{types[4]}] Erro ao preencher o campo de senha: {e}")

    def run(self):
        try:
            self.btn_tipo()
            self.input_ra()
            self.input_dg_ra()
            self.input_uf_ra()
            self.input_senha()
            print(f"[{types[7]}] Login realizado com sucesso.")
        except Exception as e:
            print(f"[{types[4]}] Erro durante o processo de login: {e}")