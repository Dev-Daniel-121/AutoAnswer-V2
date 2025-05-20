from project.models import SelecionarUsuarios, SistemaUsuarios
from project import Display, LogType
import os, sys

class MenuSystem:
    def __init__(self):
        self.display = Display

    def menu(self):
        options_data = [(LogType.OPTION, 'Start'), (LogType.OPTION, 'Settings'), (LogType.OPTION, 'Sair')]
        options = self.display(options_data, 'MENU', answer=True, user='', title_quest='')
        user_choice = options.display()

        if user_choice == 1:
            self.selectUser()
        elif user_choice == 2:
            self.settings()
        elif user_choice == 3:
            sys.exit()
        else:
            print(f'[{LogType.ERROR}] Opção inválida')

    def selectUser(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        sistema = SistemaUsuarios()
        selecionar = SelecionarUsuarios()
        selecionar.run()

        ids_selecionados = selecionar.get_usuarios_selecionados()
        if not ids_selecionados:
            print(f'[{LogType.WARNING}] Nenhum usuário selecionado.')
            return

        sistema.usuarios = sistema.carregar_usuarios()

        print(f'\n[{LogType.INFO}] Usuários selecionados:')

        for id_usuario in ids_selecionados:
            id_usuario = str(id_usuario)

            if id_usuario not in sistema.usuarios:
                print(f'[{LogType.ERROR}] ID \'{id_usuario}\' não encontrado no dicionário!')
                continue

            usuario = sistema.usuarios[id_usuario]
            print(f'[{LogType.USER}] ID: {usuario.id_usuario} - Nome: {usuario.nome} {usuario.sobrenome}')

        for id_usuario in ids_selecionados:
            usuario = sistema.usuarios[str(id_usuario)]
            nome_completo = f'{usuario.nome} {usuario.sobrenome}'
            self.apps(nome_completo, id_usuario)

    def apps(self, nome_usuario, id_usuario):
        options_data = [(LogType.OPTION, 'Sala do futuro'), (LogType.OPTION, 'Sair')]
        options = self.display(options_data, 'APPS', answer=True, user=nome_usuario, title_quest='')
        user_choice = options.display()

        if user_choice == 1:
            from project.apps.sala_do_futuro import SalaDoFuturo
            sala_do_futuro = SalaDoFuturo()
            sala_do_futuro.run(id_usuario)
            input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')
        elif user_choice == 2:
            print(f'\n[{LogType.INFO}] Encerrando processos...')
            return
        else:
            print(f'[{LogType.ERROR}] Opção inválida')
            input(f'\n[{LogType.MSG}] Pressione Enter para continuar...')
            sys.exit()

    def settings(self):
        options_data = [(LogType.OPTION, 'Format'), (LogType.OPTION, 'Browser'), (LogType.OPTION, 'User'), (LogType.OPTION, 'Voltar')]
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
            print(f'[{LogType.ERROR}] Opção inválida')
            sys.exit()

    def format_(self):
        options_data = [(LogType.OPTION, 'WEB'), (LogType.OPTION, 'CMD'), (LogType.OPTION, 'Voltar')]
        options = self.display(options_data, 'FORMAT', answer=True, user='', title_quest='')
        user_choice = options.display()

        if user_choice == 1:
            print(f'[{LogType.INFO}] WEB...')
            sys.exit()
        elif user_choice == 2:
            print(f'[{LogType.INFO}] CMD...')
            sys.exit()
        elif user_choice == 3:
            self.settings()
        else:
            print(f'[{LogType.ERROR}] Opção inválida')
            sys.exit()

    def browser(self):
        options_data = [(LogType.OPTION, 'Chrome'), (LogType.OPTION, 'FireFox'), (LogType.OPTION, 'Voltar')]
        options = self.display(options_data, 'BROWSER', answer=True, user='', title_quest='')
        user_choice = options.display()

        if user_choice == 1:
            print(f'[{LogType.INFO}] WEB...')
            sys.exit()
        elif user_choice == 2:
            print(f'[{LogType.INFO}] CMD...')
            sys.exit()
        elif user_choice == 3:
            self.settings()
        else:
            print(f'[{LogType.ERROR}] Opção inválida')
            sys.exit()

    def users(self):
        sistema = SistemaUsuarios()
        sistema.run()

    def run(self):
        self.menu()