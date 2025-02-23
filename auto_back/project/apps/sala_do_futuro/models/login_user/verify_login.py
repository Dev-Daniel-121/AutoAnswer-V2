from project import SistemaUsuarios, types

class VerifyLogin:
    def __init__(self, page, open_perfil_class, close_perfil_class, get_info_nome_class, get_info_user_class):
        self.page = page
        self.open_perfil_class = open_perfil_class
        self.close_perfil_class = close_perfil_class
        self.get_info_nome_class = get_info_nome_class
        self.get_info_user_class = get_info_user_class
        self.user_system = SistemaUsuarios()

    def open_perfil(self, timeout=1000):
        try:
            self.page.wait_for_selector(self.open_perfil_class, timeout=timeout)
            open_perfil = self.page.locator(f'{self.open_perfil_class}')
            open_perfil.click()
        except Exception as e:
            print(f'[{types[4]}] Erro ao tentar encontrar o botão de login: {e}')
            return False
        return True

    def close_perfil(self):
        try:
            close_perfil = self.page.locator(f'{self.close_perfil_class}')
            close_perfil.click()
        except Exception as e:
            print(f'[{types[4]}] Erro ao tentar fechar perfil: {e}')

    def get_info(self):
        try:
            nome = self.page.inner_text(f'{self.get_info_nome_class}', strict=True).split('\n')[0].strip()
            user = self.page.inner_text(f'{self.get_info_user_class}', strict=True).strip()
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter informações de login do usuário: {e}')
            return None, None

        return nome, user
    
    def get_user_by_id(self, id_usuario):
        usuarios = self.user_system.carregar_usuarios()
        return usuarios.get(id_usuario)

    def validate_info(self, usuario, nome, user):
        if not usuario:
            return 'Usuário não encontrado'
        
        nome_completo = f'{usuario.nome} {usuario.sobrenome}'
        return 'Logado' if nome.strip().lower() == nome_completo.strip().lower() and user.strip().lower() == usuario.user.strip().lower() else 'Não logado'

    def run(self, id_usuario):
        try:
            if not self.open_perfil():
                return 'Não logado'

            nome, user = self.get_info()
            if nome is None or user is None:
                return 'Não logado'
            
            usuarios = self.get_user_by_id(id_usuario)
            validate = self.validate_info(usuarios, nome, user)

            self.close_perfil()

            return validate
        except Exception as e:
            print(f'[{types[3]}] Erro ao tentar obter dados de login: {e}')
            input(f'\n[{types[6]}] Pressione Enter para continuar...')