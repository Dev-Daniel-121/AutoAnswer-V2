from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie import Questions, QuestionInfo
from project import LogType

class CollectResults:
    def __init__(
            self, page, 
            question_locator, section_locator, can_get_points, btn_end_activity, btn_save_as_draft_activity,
            radios_user_class, # div.css-19tjzz6
            radios_correct_class, # div.css-i4v92
            radios_wrong_class, # div.css-13fnmrr
            checkbox_user_class, # div.css-1jah0mi
            checkbox_correct_class, # div.css-1k51hj6
            checkbox_wrong_class # div.css-14296jx
        ):
        self.page = page
        self.question_locator = question_locator
        self.section_locator = section_locator
        self.can_get_points = can_get_points
        self.btn_end_activity = btn_end_activity
        self.btn_save_as_draft_activity = btn_save_as_draft_activity
        self.radios_user_class = radios_user_class
        self.radios_correct_class = radios_correct_class
        self.radios_wrong_class = radios_wrong_class
        self.checkbox_user_class = checkbox_user_class
        self.checkbox_correct_class = checkbox_correct_class
        self.checkbox_wrong_class = checkbox_wrong_class

    def get_answers(self, question, quest_type):
        try:
            if quest_type == 'Radios':
                if question.locator(self.radios_correct_class).count() > 0:
                    answer = question.locator(self.radios_correct_class).inner_text()
                    return answer, answer
                elif question.locator(self.radios_wrong_class).count() > 0:
                    answer = question.locator(self.radios_wrong_class).inner_text()
                    answer_key = question.locator(self.radios_user_class).inner_text()
                    return answer, answer_key
                
            elif quest_type == 'Checkbox':
                selected_correct = question.locator(self.checkbox_correct_class).all()
                selected_wrong = question.locator(self.checkbox_wrong_class).all()
                correct_answers = question.locator(self.checkbox_user_class).all()

                answer = [el.inner_text() for el in selected_correct + selected_wrong]
                answer_key = [el.inner_text() for el in correct_answers]
                return answer, answer_key

        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao coletar respostas: {e}')
        return '', ''

    def run(self):
        from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info import CollectSection
        questions = {}

        try:
            question_elements = self.page.locator(self.btn_save_as_draft_activity)
            count = question_elements.count()

            section_finder = None
            use_sections = False

            if self.section_locator:
                locator = self.page.locator(self.section_locator)
                if locator.count() > 0:
                    use_sections = True
                    section_finder = CollectSection(
                        page=self.page,
                        elem_section_class=self.section_locator,
                        time_wait=125
                    )

            should_get_score = not (
                (self.can_get_points and len(self.can_get_points) > 1) or
                self.btn_end_activity or
                self.btn_save_as_draft_activity
            )

            for i in range(count):
                actual_quest = question_elements.nth(i)

                question_obj = Questions(
                    page=self.page,
                    required_class='p.css-sz9ejl',
                    question_statement_class='div.css-1a4wlpz',
                    has_radios_class='div.css-1h7anqn',
                    has_checkbox_class='div.css-107ow6p',
                    actual_quest=actual_quest
                )

                question_info = QuestionInfo(
                    page=self.page,
                    time_wait=125,
                    actual_quest=actual_quest,
                    activity_score_class='p.css-yy9bdr',
                    score_class='p.css-1dej7zy',
                    can_get_points=self.can_get_points,
                    btn_end_activity=self.btn_end_activity,
                    btn_save_as_draft_activity=self.btn_save_as_draft_activity
                )

                section_text = section_finder.get_section_for_element(actual_quest) if use_sections else ''
                quest_type = question_obj.get_quest_type()
                is_required = question_obj.isRequired()
                points = question_info.get_activity_score() if should_get_score else {'activity_score': '', 'score': ''}

                answer, answer_key = self.get_answers(actual_quest, quest_type)

                questions[f'q{i}'] = {
                    'section': section_text or '',
                    'type': quest_type or '',
                    'required': is_required or False,
                    'score': points['score'] or '',
                    'points': points['activity_score'] or '',
                    'answer': answer,
                    'answer_key': answer_key
                }
                
            return questions

        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao coletar resultados: {e}')
            return {}

'''

O código deve encontrar todas as div.css-19tjzz6 e para cada uma delas ele deve

'''

'''

Como usar

collector = CollectResults(page)
results = collector.run(
    question_locator='div.questao',
    section_locator='div.secao',  # Se tiver
    can_get_points=['p.css-yy9bdr'],
    btn_end_activity=None,
    btn_save_as_draft_activity=None
)

'''

'''

Essa class deve para cada questão coletar os seguintes dados e depois criar esse Dict, aqui estão as classes delas

Dados

Seção - Use os imports do código abaixo
Tipo de Questão - Use os imports do código abaixo
Obritória - h6.css-11b38c9
Nota - p.css-1dej7zy
Pontos - p.css-yy9bdr

HTML

Resposta e Gabarito
    Radios
        Se a resposta estiver certa
        Correct         - div.css-1leca56 div.css-i4v92

        Se a resposta estiver errada
        Wrong           - div.css-1leca56 div.css-13fnmrr

        Se a resposta estiver errada essa seria a correta
        Correct Answer  - div.css-1leca56 div.css-19tjzz6

    Checkbox
        Se a resposta estiver certa
        Correct         - div.css-1leca56 div.css-1k51hj6

        Se a resposta estiver errada
        Wrongs          - div.css-1leca56 div.css-14296jx

        Se a resposta estiver errada essa seria a correta
        Correct Answer  - div.css-1leca56 div.css-1jah0mi


Py Dict

questions = {
    'q$': {
        'section':,
        'type':,
        'required':,
        'score':,
        'points':,
        'answer':,
        'answer_key':
    }
}

Eu tenho um código que já faz isso, porém estava pensando em refazer ele para coletar essas informações.

Py - Playwright

from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie import Questions, QuestionInfo, GeneralQuests
from project import LogType

class Questionarie:
    def __init__(
            self, page, elem_section_class, 
            can_get_points, btn_end_activity, btn_save_as_draft_activity, question
        ):
        self.page = page
        self.elem_section_class = elem_section_class
        self.can_get_points = can_get_points
        self.btn_end_activity = btn_end_activity
        self.btn_save_as_draft_activity = btn_save_as_draft_activity
        self.question = question

    def run(self):
        from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info import CollectSection
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

                questionarie[str(i)] = {
                    'quest_info': {
                        'required': isRequired or '',
                        'time': {
                            'day': '',
                            'start_time': '',
                            'end_time': ''
                        },
                        'activity_score': activity_score or '', # Pontuação máxima da Atividade
                        'score': score or '', # Pontuação obtida da atividade
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
                        'quest_score': '', # Nota
                        'quest_points': '', # Pontos
                        'user_guess': '', # Chute (True/False)
                        'answered_by_user': False, # Respondido pelo User (True/False)
                        'required': False, # Obrigatória (True/False)
                        'type': quest_type or '',
                        'statement': statement or '',
                        'alternatives': {
                            'media': {},
                            'alternative': alternatives if alternatives else [''],
                        },
                        'answer': '', # Resposta User
                        'answer_key': '' # Gabarito
                    }
                }

            general_quests = GeneralQuests(questionarie)
            questionarie = general_quests.run()
            return questionarie
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter informações das questões: {e}')
            return

'''
