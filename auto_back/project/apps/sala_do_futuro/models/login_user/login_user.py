from project import types

class LoginUser:
    def __init__(self, page, tipo, ra, dg_ra, uf_ra, senha):
        self.page = page
        self.tipo = tipo
        self.ra = ra
        self.dg_ra = dg_ra
        self.uf_ra = uf_ra
        self.senha = senha

    def run_login_aluno(self):
        from project.apps.sala_do_futuro.models.login_user.login_aluno import LoginAluno

        login_aluno = LoginAluno(
            page=self.page,
            tipo=self.tipo,
            ra=self.ra,
            dg_ra=self.dg_ra,
            uf_ra=self.uf_ra,
            senha=self.senha,
            btn_tipo_class='div.css-m1mmqw',
            input_ra_id='input#input-usuario-sed',
            input_dg_ra_name='input[name=\'digito-ra\']',
            input_uf_ra_class='div.css-r1nef8',
            li_uf_ra_class='li.css-4dqmvd',
            input_senha_id='input#input-senha'
        )
        login_aluno.run()

    def login_servidor(self):
        print(f'[{types[7]}] Login de servidor realizado com sucesso!')

    def login_responsavel(self):
        print(f'[{types[7]}] Login de responsável realizado com sucesso!')

    def run(self):
        if self.tipo == 'Aluno':
            self.run_login_aluno()
        elif self.tipo == 'Servidor':
            self.login_servidor()
        elif self.tipo == 'Responsavel':
            self.login_responsavel()
        else:
            print(f'[{types[4]}] Tipo de conta inválido.')