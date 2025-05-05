from project import types
import re

class QuestionInfo:
    def __init__(
            self, page, time_wait, actual_quest, activity_score_class, 
            score_class, quest_section_class
        ):
        self.page = page
        self.time_wait = time_wait
        self.actual_quest = actual_quest
        self.activity_score_class = activity_score_class
        self.score_class = score_class
        self.quest_section_class = quest_section_class

    def get_activity_score(self):
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
            print(f'[{types[4]}] Elementos não encontrados após {self.time_wait} milésimos')
            return {
                'activity_score': '',
                'score': ''
            }
        
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter pontuações: {e}')
            return {
                'activity_score': '',
                'score': ''
            }

    def get_quest_section(self):
        try:
            if not self.quest_section_class:
                return None

            section_elements = self.page.locator(self.quest_section_class)
            actual_box = self.actual_quest.bounding_box()

            closest_section = None
            closest_section_top = float('-inf')

            for i in range(section_elements.count()):
                section = section_elements.nth(i)
                section_box = section.bounding_box()

                if section_box and section_box['y'] <= actual_box['y']:
                    if section_box['y'] > closest_section_top:
                        closest_section_top = section_box['y']
                        closest_section = section

            return closest_section.text_content() if closest_section else None

        except Exception as e:
            print(f'[{types[4]}] Erro ao obter Seção da questão: {e}')
            return None

    def run(self):
        pass
