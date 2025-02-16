from project.config import types
from project.utils import Display

class MenuSystem:
    def __init__(self):
        self.display = Display
        self.types = types
        self.logged_in = False

    def menu(self):
        options_data = [(2, 'Efetuar login'), (2, 'Exibir dados escolares'), (2, 'Realizar Atividades'), (2, 'Sair')]
        options = self.display(options_data, 'MENU', answer=False, user='', title_quest='')
        options.display()
        user_choice = input(f'[{types[1]}] Digite as opções (separadas por vírgula) ou "*" / "all" para todas: ')

        if user_choice.strip().lower() in ['*', 'all']:
            choices = [1, 2, 3]
        else:
            try:
                choices = [int(choice.strip()) for choice in user_choice.split(',')]
                choices.sort()
            except ValueError:
                print(f'[{types[4]}] Entrada inválida. Por favor, digite números separados por vírgula, "*" ou "all".')
                return
            
        if 1 not in choices and (2 in choices or 3 in choices):
            print(f'[{types[3]}] A opção 1 (Efetuar login) é obrigatória para as opções 2 e 3. Ela será executada automaticamente.')
            input('Pressione ENTER para continuar...')
            choices.insert(0, 1)

        for choice in choices:
            if choice == 1:
                from project.apps.sala_do_futuro.classes.models.login_user.login_user import LoginUser
                login_user = LoginUser()
                login_user.run()
                self.logged_in = True
            elif choice == 2:
                if not self.logged_in:
                    print(f'[{types[4]}] Você precisa estar logado para exibir dados escolares.')
                    continue
                from project.apps.sala_do_futuro.classes.models.data.data import Data
                data = Data()
                data.run()
            elif choice == 3:
                if not self.logged_in:
                    print(f'[{types[4]}] Você precisa estar logado para realizar atividades.')
                    continue
                from project.apps.sala_do_futuro.classes.models.realizar_atividades.realizar_atividades import RealizarAtividades
                realizar = RealizarAtividades()
                realizar.run()
            elif choice == 4:
                print(f'[{types[4]}] Saindo...')
                break
            else:
                print(f'[{types[4]}] Opção inválida: {choice}')

    def run(self):
        self.menu()