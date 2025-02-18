from project import types, Display
from project.apps.sala_do_futuro.models.login_user.login_user import LoginUser
from project.apps.sala_do_futuro.models.data.data import Data
from project.apps.sala_do_futuro.models.realizar_atividades.realizar_atividades import RealizarAtividades

class MenuSystem:
    def __init__(self, page):
        self.display = Display
        self.types = types
        self.logged_in = False
        self.usuario = None  # Variável para armazenar os dados do usuário
        self.page = page

    def menu(self):
        options_data = [(2, 'Efetuar login'), (2, 'Exibir dados escolares'), (2, 'Realizar Atividades'), (2, 'Sair')]
        options = self.display(options_data, 'MENU', answer=False, user=f'{self.usuario.nome} {self.usuario.sobrenome}', title_quest='')
        options.display()
        user_choice = input(f'\n[{types[1]}] Digite as opções (separadas por vírgula) ou "*" para todas: ')

        if user_choice.strip().lower() in ['*', 'all']:
            choices = [1, 2, 3, 4]
        else:
            try:
                choices = [int(choice.strip()) for choice in user_choice.split(',')]
                choices.sort()
            except ValueError:
                print(f'[{types[4]}] Entrada inválida. Por favor, digite números separados por vírgula, "*" ou "all".')
                return

        if any(choice < 1 or choice > 4 for choice in choices):
            print(f'[{types[4]}] Opção inválida. As opções devem estar entre 1 e 4.')
            return

        if not self.logged_in and (2 in choices or 3 in choices):
            print(f'[{types[3]}] A opção 1 (Efetuar login) é obrigatória para as opções 2 e 3. Ela será executada automaticamente.')
            input('Pressione ENTER para continuar...')
            choices.insert(0, 1)

        for choice in choices:
            if choice == 1:
                login_user = LoginUser(
                    page=self.page,
                    tipo=self.usuario.tipo_conta,
                    ra=self.usuario.ra,
                    dg_ra=self.usuario.dg_ra,
                    uf_ra=self.usuario.uf_ra,
                    senha=self.usuario.senha
                )
                login_user.run()  # Passando os dados do usuário
                self.logged_in = True
            elif choice == 2:
                if not self.logged_in:
                    print(f'[{types[4]}] Você precisa estar logado para exibir dados escolares.')
                    continue
                data = Data()
                data.run(self.usuario)  # Passando os dados do usuário
            elif choice == 3:
                if not self.logged_in:
                    print(f'[{types[4]}] Você precisa estar logado para realizar atividades.')
                    continue
                realizar = RealizarAtividades()
                realizar.run(self.usuario)  # Passando os dados do usuário
            elif choice == 4:
                print(f'[{types[4]}] Saindo...')
                break
            else:
                print(f'[{types[4]}] Opção inválida: {choice}')

    def run(self, usuario):
        self.usuario = usuario  # Armazena o usuário para uso posterior
        self.menu()