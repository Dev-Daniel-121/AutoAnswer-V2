from project import LogType, Display

class Grok:
    def __init__(self, user):
        self.user = user

    def prompt(self):
        options_data = [(LogType.OPTION, 'Start'), (LogType.OPTION, 'Settings'), (LogType.OPTION, 'Sair')]
        options = Display(options_data, 'Prompt Grok', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if user_choice == 1:
            self.start()
        elif user_choice == 2:
            self.settings()
        elif user_choice == 3:
            return
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')
