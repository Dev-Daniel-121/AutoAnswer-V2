from project import types
import re

class Questions:
    def __init__(
            self, page, 
            question_statement_class = 'div.css-1a4wlpz'
        ):
        self.page = page
        self.question_statement_class = question_statement_class
        self.quest_container = self.page.locator(':nth-match(div.css-b200pa, 1)')

    def get_quest_type(self):
        try:
            if self.quest_container.locator('div.css-1h7anqn').count() > 0:
                return 'Radios'

            if self.quest_container.locator('div.css-107ow6p').count() > 0:
                return 'Checkbox'

            return 'Unknown Type'
        
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter o tipo da questão: {e}')
            return

    def get_question_statement(self):
        try:
            question_statement = self.quest_container.locator(f'{self.question_statement_class}').text_content()
            return question_statement
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter enunciado da questão: {e}')
            return

    def get_question_alternatives(self, quest_type):
        try:
            if quest_type == 'Radios':
                pass
            elif quest_type == 'Checkbox':
                pass
            elif quest_type == '':
                pass
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter alternativas da questão: {e}')
            return

    def run(self):
        pass
