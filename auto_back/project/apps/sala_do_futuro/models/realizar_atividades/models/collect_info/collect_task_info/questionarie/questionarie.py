from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie import Questions, QuestionInfo
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info import CollectSection
from project import types

class Questionarie:
    def __init__(
            self, page, elem_section_class, 
            can_get_points, btn_end_activity, btn_save_as_draft_activity, question
        ):
        self.page = page
        self.types = types
        self.elem_section_class = elem_section_class
        self.can_get_points = can_get_points
        self.btn_end_activity = btn_end_activity
        self.btn_save_as_draft_activity = btn_save_as_draft_activity
        self.question = question

    def run(self):
        try:
            questionarie = {}
            elements = self.page.locator(self.question)

            section_finder = None
            use_sections = False

            if self.elem_section_class:
                locator = self.page.locator(self.elem_section_class)
                if locator.count() > 0:
                    use_sections = True
                    section_finder = CollectSection(
                        page=self.page,
                        elem_section_class=self.elem_section_class,
                        time_wait=125
                    )

            should_get_score = not (
                (self.can_get_points and len(self.can_get_points) > 1) or
                self.btn_end_activity or
                self.btn_save_as_draft_activity
            )

            count = elements.count()
            for i in range(count):
                actual_quest = elements.nth(i)
                question_obj = Questions(
                    page=self.page,
                    required_class='p.css-sz9ejl',
                    question_statement_class='div.css-1a4wlpz',
                    has_radios_class='div.css-1h7anqn',
                    has_checkbox_class='div.css-107ow6p',
                    actual_quest=actual_quest
                )

                question_info = QuestionInfo(
                    page=self.page, time_wait=125,
                    actual_quest=actual_quest, activity_score_class='p.css-yy9bdr',
                    score_class='p.css-1dej7zy', can_get_points=self.can_get_points,
                    btn_end_activity= self.btn_end_activity,
                    btn_save_as_draft_activity= self.btn_save_as_draft_activity
                )

                section_text = ''
                if use_sections and section_finder:
                    section_text = section_finder.get_section_for_element(actual_quest)

                activity_score, score = '', ''
                if should_get_score:
                    points = question_info.get_activity_score()
                    activity_score = points['activity_score']
                    score = points['score']

                quest_type = question_obj.get_quest_type()
                statement = question_obj.get_question_statement()
                statement_media = question_obj.get_question_statement_media(video_media_selector='div.css-pcbmqt iframe', img_media_selector='img')
                alternatives = question_obj.get_question_alternatives(quest_type)
                isRequired = question_obj.isRequired()

                questionarie[i] = {
                    'quest_info': {
                        'required': isRequired or '',
                        'time': {
                            'day': '',
                            'start_time': '',
                            'end_time': ''
                        },
                        'activity_score': activity_score or '',
                        'score': score or '',
                        'section': section_text or '',
                        'number_of_guesses': '',
                        'number_of_user_responses': '',
                        'user_feedback': '',
                        'difficulty': '',
                        'media': statement_media or {},
                        'history_of_attempts': {
                            # 0: { 'quest': '', 'author': '', 'result': '', 'time': '' },
                            # 1: { 'quest': '', 'author': '', 'result': '', 'time': '' }
                        },
                        'error_num': '',
                        'error_types': ['', '', ''],
                        'error_logs': {
                            '0': {
                                'type': '',
                                'details': '',
                                'question': '',
                                'timestamp': ''
                            }
                        },
                        'ia': '',
                        'time_spent': '',
                    },
                    'quest': {
                        'type': quest_type or '',
                        'statement': statement or '',
                        'alternatives': {
                            'media': {},
                            'alternative': alternatives if alternatives else [''],
                        },
                        'answer': ''
                    }
                }

            return questionarie
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter informações das questões: {e}')
            return