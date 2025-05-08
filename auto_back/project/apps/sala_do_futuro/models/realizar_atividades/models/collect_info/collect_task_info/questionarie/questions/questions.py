from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions import GetRadios, GetCheckbox
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info import CollectMedia
from project import types

class Questions:
    def __init__(
            self, page,
            required_class, 
            question_statement_class,
            has_radios_class,
            has_checkbox_class,
            actual_quest
        ):
        self.page = page
        self.required_class = required_class
        self.question_statement_class = question_statement_class
        self.has_radios_class = has_radios_class
        self.has_checkbox_class = has_checkbox_class
        self.actual_quest = actual_quest
        self.get_radios = GetRadios(
            page=self.page, has_radios_class=self.has_radios_class,
            radios_alternative_class='div.css-10zfeld', actual_quest=self.actual_quest,
            video_media_selector='div.css-pcbmqt iframe', img_media_selector='img'
        )
        self.get_checkbox = GetCheckbox(
            page=self.page, has_checkbox_class=self.has_checkbox_class,
            checkbox_alternative_class='div.css-107ow6p', actual_quest=self.actual_quest,
            video_media_selector='div.css-pcbmqt iframe', img_media_selector='img'
        )

    def get_quest_type(self):
        try:
            if self.actual_quest.locator(f'{self.has_radios_class}').count() > 0:
                return 'Radios'

            if self.actual_quest.locator(f'{self.has_checkbox_class}').count() > 0:
                return 'Checkbox'

            return 'Unknown Type'
        
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter o tipo da questão: {e}')
            return

    def get_question_statement(self):
        try:
            question_statement = self.actual_quest.locator(f'{self.question_statement_class}').first.text_content()
            return question_statement
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter enunciado da questão: {e}')
            return

    def get_question_alternatives(self, quest_type):
        try:
            alternatives = []
            if quest_type == 'Radios':
                alternatives = self.get_radios.get_alternatives()
        
            elif quest_type == 'Checkbox':
                alternatives = self.get_checkbox.get_alternatives()

            elif quest_type == 'Unknown Type':
                return []

            return alternatives
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter alternativas da questão: {e}')
            return
    
    def get_question_statement_media(self, video_media_selector, img_media_selector):
        try:
            statement_element = self.actual_quest.locator(f'{self.question_statement_class}')
            media_collector = CollectMedia(
                card=statement_element,
                video_media_selector=video_media_selector,
                img_media_selector=img_media_selector
            )
            return media_collector.extract_media()
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter mídias do enunciado: {e}')
            return {'video': {}, 'image': {}, 'gif': {}}
    
    def isRequired(self) -> bool: return self.page.locator(self.required_class).count() > 0