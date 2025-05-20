# from project.apps.answer.models import Grok
from project import Display, LogType
import json, os

class MenuSystem:
    def __init__(self, user, close_terminal_flag=False):
        self.user = user
        # self.grok = Grok(user=self.user)
        self.close_terminal_flag = close_terminal_flag

    def _get_data_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(os.path.dirname(current_dir), 'data')
        os.makedirs(data_dir, exist_ok=True)
        
        return os.path.join(data_dir, 'answer_data.json')

    def carregar_ias(self):
        file_path = self._get_data_path()
        
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

            ias = [ia.title() for ia in data['ia'].keys()]
            
            return ias
        
        except FileNotFoundError:
            print(f'[{LogType.ERROR}] Arquivo JSON não encontrado: {file_path}')
            return []
        except json.JSONDecodeError:
            print(f'[{LogType.ERROR}] Erro ao decodificar o JSON.')
            return []

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
        ias = self.carregar_ias()
        
        options_data = [(LogType.OPTION, f'{ia}') for ia in ias]
        options_data.append((LogType.OPTION, 'Voltar'))
        
        options = Display(options_data, 'IA', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if user_choice == len(ias) + 1:
            self.menu()
        elif 1 <= user_choice <= len(ias):
            ia_escolhida = ias[user_choice - 1]
            print(f'[{LogType.INFO}] {ia_escolhida}')
            input('Pressione qualquer tecla para voltar...')
            self.menu()
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')

    def settings(self):
        options_data = [(LogType.OPTION, 'IA'), (LogType.OPTION, 'Etapas da Automação'), (LogType.OPTION, 'Localização dos circulos'), (LogType.OPTION, 'Voltar')]
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
