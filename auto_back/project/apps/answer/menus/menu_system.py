from project.apps.answer.models import Grok
from project import Display, LogType

class MenuSystem:
    def __init__(self, user, close_terminal_flag=False):
        self.user = user
        self.grok = Grok(user=self.user)
        self.close_terminal_flag = close_terminal_flag

    def menu(self):
        options_data = [(LogType.OPTION, 'Start'), (LogType.OPTION, 'Settings'), (LogType.OPTION, 'Sair')]
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
        options_data = [(LogType.OPTION, 'Grok'), (LogType.OPTION, 'ChatGPT'), (LogType.OPTION, 'Voltar')]
        options = Display(options_data, 'IA', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if user_choice == 1:
            print('Grok')
        elif user_choice == 2:
            print('ChatGPT')
        elif user_choice == 3:
            self.menu()
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')

    def settings(self):
        options_data = [(LogType.OPTION, 'Etapas da Automação'), (LogType.OPTION, 'Localização dos circulos'), (LogType.OPTION, 'Voltar')]
        options = Display(options_data, 'Settings', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if user_choice == 1:
            print('Etapas da Automação')
            input('al')
        elif user_choice == 2:
            print('Localização dos Circulos')
            input('al')
        elif user_choice == 3:
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
