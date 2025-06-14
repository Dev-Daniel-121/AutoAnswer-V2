from project import LogType
import os

class Display:
    def __init__(self, data, title, answer=False, user='', title_quest='', clear_enabled=True):
        self.data = data
        self.title = title
        self.user = user
        self.title_quest = title_quest
        self.answer = answer
        self.user_answer = None
        self.clear_enabled = clear_enabled

    def clear_terminal(self):
        if self.clear_enabled:
            os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        self.clear_terminal()
        print(f'\n~~~~~~ {self.title} ~~~~~~ ({self.user})' if self.user else f'\n~~~~~~ {self.title} ~~~~~~')
        
        print(f'\n[{LogType.QUESTION}] {self.title_quest}\n' if self.title_quest else '')

        for i, (tipo, value) in enumerate(self.data):
            print(f'[{tipo}] {i+1}. {value}')

        if self.answer:
            while True:
                try:
                    answer = int(input(f'\n[{LogType.TASK}] Digite a opção: '))
                    
                    if 1 <= answer <= len(self.data):
                        self.user_answer = answer
                        print(f'[{LogType.ANSWER}] {self.user_answer}')
                        return self.user_answer
                    
                    print(f'[{LogType.ERROR}] Opção inválida! Escolha um número entre 1 e {len(self.data)}.')

                except ValueError:
                    print(f'[{LogType.ERROR}]  Entrada inválida! Digite um número válido.')