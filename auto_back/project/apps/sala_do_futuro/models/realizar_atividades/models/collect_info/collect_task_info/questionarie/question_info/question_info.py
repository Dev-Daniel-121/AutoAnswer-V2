from project import types
import re

class QuestionInfo:
    def __init__(
            self, page, 
            activity_score_class = 'p.css-1wgaj9w'
        ):
        self.page = page
        self.activity_score_class = activity_score_class

    def get_activity_score(self):
        try:
            activity_score = self.page.locator(f'{self.activity_score_class}').text_content()
            number_only = re.search(r'\d+', activity_score)
            return number_only.group() if number_only else None
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter pontuação: {e}')
            return

    def run(self):
        pass
