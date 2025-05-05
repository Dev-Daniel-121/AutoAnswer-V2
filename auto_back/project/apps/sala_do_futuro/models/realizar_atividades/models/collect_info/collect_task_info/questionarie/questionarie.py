from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie import Questions, QuestionInfo
from project import types

class Questionarie:
    def __init__(
            self, page,
            question='div.css-b200pa'
        ):
        self.page = page
        self.types = types
        self.question = question

    def run(self):
        try:
            questionarie = {}
            elements = self.page.locator(self.question)

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
                    score_class='p.css-1dej7zy', quest_section_class='div.css-8atqhb h2'
                )

                section_text = question_info.get_quest_section()
                points = question_info.get_activity_score()
                activity_score, score = points['activity_score'], points['score']

                quest_type = question_obj.get_quest_type()
                statement = question_obj.get_question_statement()
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
                        'alternatives': alternatives if alternatives else [''],
                        'answer': ''
                    }
                }
                
                # print(f'\n{'-' * 30}\n')
                # print(f'Questão: {i + 1}')
                # print(f'Tipo: {questionarie[i]['quest']['type']}')
                # print(f'Obrigatório: {questionarie[i]['quest']['required']}\n')
                # print(f'\nEnunciado: {questionarie[i]['quest']['statement']}\n')
                # print(f'\nAlternativas: {questionarie[i]['quest']['alternatives']}\n')

            return questionarie
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter informações das questões: {e}')
            return