from project.models import SelecionarUsuarios, SistemaUsuarios
from project import Display, types
import sys
import os

class MenuSystem:
    def __init__(self):
        self.display = Display
        self.types = types

    def menu(self):
        options_data = [(2, 'Start'), (2, 'Settings'), (2, 'Sair')]
        options = self.display(options_data, 'MENU', answer=True, user='', title_quest='')
        user_choice = options.display()

        if user_choice == 1:
            self.selectUser()
        elif user_choice == 2:
            self.settings()
        elif user_choice == 3:
            sys.exit()
        else:
            print(f'[{types[4]}] Opção inválida')

    def selectUser(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        sistema = SistemaUsuarios()
        selecionar = SelecionarUsuarios()
        selecionar.run()

        ids_selecionados = selecionar.get_usuarios_selecionados()
        if not ids_selecionados:
            print(f'[{types[8]}] Nenhum usuário selecionado.')
            return

        sistema.usuarios = sistema.carregar_usuarios()

        print(f'\n[{types[9]}] Usuários selecionados:')

        for id_usuario in ids_selecionados:
            id_usuario = str(id_usuario)

            if id_usuario not in sistema.usuarios:
                print(f'[{types[4]}] ID \'{id_usuario}\' não encontrado no dicionário!')
                continue

            usuario = sistema.usuarios[id_usuario]
            print(f'[{types[5]}] ID: {usuario.id_usuario} - Nome: {usuario.nome} {usuario.sobrenome}')

        for id_usuario in ids_selecionados:
            usuario = sistema.usuarios[str(id_usuario)]
            nome_completo = f'{usuario.nome} {usuario.sobrenome}'
            self.apps(nome_completo, id_usuario)

    def apps(self, nome_usuario, id_usuario):
        options_data = [(2, 'Sala do futuro'), (2, 'Sair')]
        options = self.display(options_data, 'APPS', answer=True, user=nome_usuario, title_quest='')
        user_choice = options.display()

        if user_choice == 1:
            from project.apps.sala_do_futuro import SalaDoFuturo
            sala_do_futuro = SalaDoFuturo()
            sala_do_futuro.run(id_usuario)
            input(f'\n[{types[6]}] Pressione Enter para continuar...')
        elif user_choice == 2:
            print(f'\n[{types[9]}] Encerrando processos...')
            return
        else:
            print(f'[{types[4]}] Opção inválida')
            input(f'\n[{types[6]}] Pressione Enter para continuar...')
            sys.exit()

    def settings(self):
        options_data = [(2, 'Format'), (2, 'Browser'), (2, 'User'), (2, 'Voltar')]
        options = self.display(options_data, 'SETTINGS', answer=True, user='', title_quest='')
        user_choice = options.display()

        if user_choice == 1:
            self.format_()
        elif user_choice == 2:
            self.browser()
        elif user_choice == 3:
            self.users()
        elif user_choice == 4:
            self.menu()
        else:
            print(f'[{types[4]}] Opção inválida')
            sys.exit()

    def format_(self):
        options_data = [(2, 'WEB'), (2, 'CMD'), (2, 'Voltar')]
        options = self.display(options_data, 'FORMAT', answer=True, user='', title_quest='')
        user_choice = options.display()

        if user_choice == 1:
            print('WEB...')
            sys.exit()
        elif user_choice == 2:
            print('CMD...')
            sys.exit()
        elif user_choice == 3:
            self.settings()
        else:
            print(f'[{types[4]}] Opção inválida')
            sys.exit()

    def browser(self):
        options_data = [(2, 'Chrome'), (2, 'FireFox'), (2, 'Voltar')]
        options = self.display(options_data, 'BROWSER', answer=True, user='', title_quest='')
        user_choice = options.display()

        if user_choice == 1:
            print('WEB...')
            sys.exit()
        elif user_choice == 2:
            print('CMD...')
            sys.exit()
        elif user_choice == 3:
            self.settings()
        else:
            print(f'[{types[4]}] Opção inválida')
            sys.exit()

    def users(self):
        sistema = SistemaUsuarios()
        sistema.run()

    def run(self):
        self.menu()