from project.apps.sala_do_futuro.models import Data, LoginUser, RealizarAtividades
from project import types, Display

class MenuSystem:
    def __init__(self, page):
        self.display = Display
        self.types = types
        self.logged_in = False
        self.usuario = None
        self.page = page

    def menu(self):
        while True:
            options_data = [(2, 'Efetuar login'), (2, 'Exibir dados escolares'), (2, 'Realizar Atividades'), (2, 'Sair')]
            options = self.display(options_data, 'MENU', answer=False, user=f'{self.usuario.nome} {self.usuario.sobrenome}', title_quest='')
            options.display()
            user_choice = input(f'\n[{types[1]}] Digite as opções desejadas (separadas por vírgula) ou \'*\' para todas: ')

            if user_choice.strip().lower() in ['*', 'all']:
                choices = [1, 2, 3, 4]
            else:
                try:
                    choices = [int(choice.strip()) for choice in user_choice.split(',')]
                except ValueError:
                    print(f'[{types[4]}] Entrada inválida. Por favor, digite números válidos separados por vírgula, \'*\' ou \'all\'.')
                    input(f'\n[{types[6]}] Pressione Enter para continuar...')
                    continue

            for choice in choices:
                if choice < 1 or choice > 4:
                    print(f'[{types[4]}] Opção inválida: {choice}. As opções devem estar entre 1 e 4.')
                    input(f'\n[{types[6]}] Pressione Enter para continuar...')
                    continue

                if choice == 1:
                    if self.logged_in:
                        from project.apps.sala_do_futuro.models import VerifyLogin

                        verify_login = VerifyLogin(page=self.page, open_perfil_class='button.css-15z7wtu', close_perfil_class='div.css-4g6ai3', get_info_nome_class='h6.css-z3qvkh', get_info_user_class='span.css-mpsazb')
                        verify_login.run(id_usuario=self.usuario.id_usuario)
                        
                        print(f'[{types[8]}] Usuário já cadastrado')
                        input(f'\n[{types[6]}] Pressione Enter para continuar...')
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
                        print(f'[{types[4]}] Você precisa estar logado para exibir dados escolares.')
                        input(f'\n[{types[6]}] Pressione Enter para continuar...')
                        continue
                    data = Data(page=self.page)
                    data.run()
                elif choice == 3:
                    if not self.logged_in:
                        print(f'[{types[4]}] Você precisa estar logado para realizar atividades.')
                        input(f'\n[{types[6]}] Pressione Enter para continuar...')
                        continue
                    realizar = RealizarAtividades()
                    realizar.run(self.usuario)
                elif choice == 4:
                    print(f'[{types[4]}] Saindo...')
                    return
                else:
                    print(f'[{types[4]}] Opção inválida: {choice}')
                    continue

    def run(self, usuario):
        self.usuario = usuario
        self.menu()