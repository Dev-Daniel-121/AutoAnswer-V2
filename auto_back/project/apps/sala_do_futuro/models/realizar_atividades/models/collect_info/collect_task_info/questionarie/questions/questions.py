from project import types

class Questions:
    def __init__(
            self, page, 
            question_statement_class = 'div.css-1a4wlpz',
            has_radios_class = 'div.css-1h7anqn',
            radios_alternative_class = 'div.css-10zfeld',
            has_checkbox_class = 'div.css-107ow6p',
            checkbox_alternative_class = 'div.css-107ow6p'
        ):
        self.page = page
        self.question_statement_class = question_statement_class
        self.has_radios_class = has_radios_class
        self.radios_alternative_class = radios_alternative_class
        self.has_checkbox_class = has_checkbox_class
        self.checkbox_alternative_class = checkbox_alternative_class
        self.quest_container = self.page.locator(':nth-match(div.css-b200pa, 3)')

    def get_quest_type(self):
        try:
            if self.quest_container.locator(f'{self.has_radios_class}').count() > 0:
                return 'Radios'

            if self.quest_container.locator(f'{self.has_checkbox_class}').count() > 0:
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
            alternatives = []
            if quest_type == 'Radios':
                alternatives_container = self.quest_container.locator(f'{self.has_radios_class}')
                alternatives_elements = alternatives_container.locator(f'{self.radios_alternative_class}')

                count = alternatives_elements.count()
                for i in range(count):
                    alt_text = alternatives_elements.nth(i).locator('p').text_content()
                    alternatives.append(alt_text.strip() if alt_text else '')

            elif quest_type == 'Checkbox':
                alternatives_elements = self.quest_container.locator(f'{self.checkbox_alternative_class}')
                
                count = alternatives_elements.count()
                for i in range(count):
                    alt_text = alternatives_elements.nth(i).locator('p').text_content()
                    alternatives.append(alt_text.strip() if alt_text else '')

            elif quest_type == 'Unknown Type':
                return []

            return alternatives
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter alternativas da questão: {e}')
            return

    def run(self):
        quest_type = self.get_quest_type()
        question_statement = self.get_question_statement()
        question_alternatives = self.get_question_alternatives(quest_type=quest_type)
        
        print(f'\n\nTipo: {quest_type}\nEnunciado: {question_statement}\n\nAlternativas: {question_alternatives}\n\n')
