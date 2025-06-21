from bs4 import BeautifulSoup

class ResponseValidator:
    def __init__(
            self, page, unanswered_questions_class, num_question_current_class
        ):
        self.page = page
        self.unanswered_questions_class = unanswered_questions_class
        self.num_question_current_class = num_question_current_class
        self.unanswered_questions = []

    def validate(self):
        soup = BeautifulSoup(self.page, 'html.parser')
        divs = soup.find_all('div', class_=self.unanswered_questions_class)
        
        for div in divs:
            p = div.find('p', class_=self.num_question_current_class)
            if p:
                b = p.find('b')
                if b and b.text.isdigit():
                    self.unanswered_questions.append(b.text)

        self._print_result()
        return self.unanswered_questions

    def _print_result(self):
        if len(self.unanswered_questions) == 1:
            print(f'A questão {self.unanswered_questions[0]} não foi respondida')
        elif len(self.unanswered_questions) > 1:
            questoes = ', '.join(self.unanswered_questions)
            print(f'As questões {questoes} não foram respondidas')
        else:
            print('Erro ao exibir questões não respondidas')

'''

'''
