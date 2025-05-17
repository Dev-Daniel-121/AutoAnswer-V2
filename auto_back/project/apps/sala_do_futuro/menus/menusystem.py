from project.apps.sala_do_futuro.models import Data, LoginUser, RealizarAtividades, Go
from project import Display, LogType

class MenuSystem:
    def __init__(self, page):
        self.display = Display
        self.logged_in = False
        self.usuario = None
        self.page = page

    def menu(self):
        while True:
            options_data = [(LogType.OPTION, 'Efetuar login'), (LogType.OPTION, 'Exibir dados escolares'), (LogType.OPTION, 'Realizar Atividades'), (LogType.OPTION, 'Sair')]
            options = self.display(options_data, 'MENU', answer=False, user=f'{self.usuario.nome} {self.usuario.sobrenome}', title_quest='')
            options.display()
            user_choice = input(f'\n[{LogType.TASK}] Digite as opções desejadas (separadas por \',\') ou \'*\' para todas: ')

            if user_choice.strip().lower() in ['*', 'all']:
                choices = [1, 2, 3, 4]
            else:
                try:
                    choices = [int(choice.strip()) for choice in user_choice.split(',')]
                except ValueError:
                    print(f'[{LogType.ERROR}] Entrada inválida. Por favor, digite números válidos separados por \',\' \'*\' ou \'all\'.')
                    input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')
                    continue

            for choice in choices:
                if choice < 1 or choice > 4:
                    print(f'[{LogType.ERROR}] Opção inválida: {choice}. As opções devem estar entre 1 e 4.')
                    input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')
                    continue

                if choice == 1:
                    if self.logged_in:
                        from project.apps.sala_do_futuro.models import VerifyLogin

                        verify_login = VerifyLogin(page=self.page, open_perfil_class='button.css-15z7wtu', close_perfil_class='div.css-4g6ai3', get_info_nome_class='h6.css-z3qvkh', get_info_user_class='span.css-mpsazb')
                        verify_login.run(id_usuario=self.usuario.id_usuario)
                        
                        print(f'[{LogType.WARNING}] Usuário já cadastrado')
                        input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')
                    else:
                        self.logged_in = False
                        login_user = LoginUser(
                            page=self.page,
                            tipo=self.usuario.tipo_conta,
                            ra=self.usuario.ra,
                            dg_ra=self.usuario.dg_ra,
                            uf_ra=self.usuario.uf_ra,
                            senha=self.usuario.senha
                        )
                        login_user.run()
                        self.logged_in = True
                elif choice == 2:
                    if not self.logged_in:
                        print(f'[{LogType.ERROR}] Você precisa estar logado para exibir dados escolares.')
                        input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')
                        continue
                    data = Data(page=self.page)
                    go = Go(
                            page=self.page, get_title_class='span.css-14ra0qi', 
                            btn_go_home_class=':nth-match(a.css-lumvx8, 1)')
                    go.go_home()
                    data.run()
                elif choice == 3:
                    if not self.logged_in:
                        print(f'[{LogType.ERROR}] Você precisa estar logado para Realizar Atividades.')
                        input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')
                        continue
                    realizar = RealizarAtividades(page=self.page)
                    realizar.run(nome_usuario=f'{self.usuario.nome} {self.usuario.sobrenome}', id_usuario=self.usuario.id_usuario)
                elif choice == 4:
                    from project import MenuSystem
                    menu_system = MenuSystem()
                    menu_system.apps(nome_usuario=f'{self.usuario.nome} {self.usuario.sobrenome}', id_usuario=self.usuario.id_usuario)

                    return
                else:
                    print(f'[{LogType.ERROR}] Opção inválida: {choice}')
                    continue

    def run(self, usuario):
        self.usuario = usuario
        self.menu()
