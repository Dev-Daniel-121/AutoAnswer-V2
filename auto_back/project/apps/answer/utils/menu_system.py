from project.apps.answer import IAHandler
from project import Display, LogType

class MenuSystem:
    def __init__(self, user, close_terminal_flag=False):
        self.user = user
        self.close_terminal_flag = close_terminal_flag
        self.ia_handler = IAHandler()

    def menu(self):
        options_data = [
            (LogType.OPTION, 'Start'),
            (LogType.OPTION, 'Settings'),
            (LogType.OPTION, 'Sair')
        ]
        options = Display(options_data, 'Answer', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if user_choice == 1:
            self.start()
        elif user_choice == 2:
            self.settings()
        elif user_choice == 3:
            self.close()
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')

    def start(self):
        self.ias = self.ia_handler.get_ias()
        options_data = []

        for ia in self.ias:
            status_geral, _ = ia.get_status_detalhado()
            options_data.append((LogType.OPTION, status_geral))

        options_data.append((LogType.OPTION, 'Voltar'))

        options = Display(options_data, 'IAs Disponíveis', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if user_choice == len(self.ias) + 1:
            self.menu()
        elif 1 <= user_choice <= len(self.ias):
            ia_escolhida = self.ias[user_choice - 1]
            self.show_metodos(ia_escolhida)
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')

    def show_metodos(self, ia_escolhida):
        _, status_por_metodo = ia_escolhida.get_status_detalhado()

        options_data = [(LogType.OPTION, status) for status in status_por_metodo]
        options_data.append((LogType.OPTION, 'Voltar'))

        options = Display(options_data, f'{ia_escolhida.nome} - Métodos', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if 1 <= user_choice <= len(status_por_metodo):
            metodo_escolhido = list(ia_escolhida.metodos.keys())[user_choice - 1]
            print(f'[{LogType.INFO}] {metodo_escolhido} selecionado')
            input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')
            self.show_metodos(ia_escolhida)
        elif user_choice == len(status_por_metodo) + 1:
            self.start()
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')


    def settings(self):
        options_data = [
            (LogType.OPTION, 'IA'),
            (LogType.OPTION, 'Etapas da Automação'),
            (LogType.OPTION, 'Localização dos circulos'),
            (LogType.OPTION, 'Voltar')
        ]
        options = Display(options_data, 'Settings', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if user_choice == 1:
            print(f'[{LogType.INFO}] IA')
            input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')
        elif user_choice == 2:
            print(f'[{LogType.INFO}] Etapas da Automação')
            input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')
        elif user_choice == 3:
            print(f'[{LogType.INFO}] Localização dos Circulos')
            input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')
        elif user_choice == 4:
            self.menu()
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')

    def close(self):
        print(f'[{LogType.WARNING}] Finalizando processos...\n')
        print(f'[{LogType.WARNING}] Fechando terminal\n')
        if self.close_terminal_flag:
            from project import Answer
            answer = Answer(user=self.user)
            answer.close_terminal()
