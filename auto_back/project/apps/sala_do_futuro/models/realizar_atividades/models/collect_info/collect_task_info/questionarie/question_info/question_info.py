from project import types
import re

class QuestionInfo:
    def __init__(
            self, page, time_wait, actual_quest, activity_score_class, 
            score_class, can_get_points, btn_end_activity, btn_save_as_draft_activity
        ):
        self.page = page
        self.time_wait = time_wait
        self.actual_quest = actual_quest
        self.activity_score_class = activity_score_class
        self.score_class = score_class
        self.can_get_points = can_get_points
        self.btn_end_activity = btn_end_activity
        self.btn_save_as_draft_activity = btn_save_as_draft_activity

    def get_activity_score(self):
        if (self.can_get_points and len(self.can_get_points) > 1) or self.btn_end_activity or self.btn_save_as_draft_activity:
            return {
                'activity_score': '',
                'score': ''
            }

        try:
            self.page.locator(f'{self.activity_score_class}').wait_for(state='attached', timeout=self.time_wait)
            self.page.locator(f'{self.score_class}').wait_for(state='attached', timeout=self.time_wait)
            
            activity_score_text = self.page.locator(f'{self.activity_score_class}').text_content()
            score_text = self.page.locator(f'{self.score_class}').text_content()

            activity_number = re.search(r'\d+', activity_score_text) if activity_score_text else None
            score_number = re.search(r'\d+', score_text) if score_text else None

            return {
                'activity_score': activity_number.group() if activity_number else '',
                'score': score_number.group() if score_number else ''
            }
        
        except TimeoutError:
            print(f'[{types[8]}] Elementos não encontrados após {self.time_wait} milésimos')
            return {
                'activity_score': '',
                'score': ''
            }
        
        except Exception as e:
            print(f'[{types[8]}] Erro ao obter pontuações: {e}')
            return {
                'activity_score': '',
                'score': ''
            }
