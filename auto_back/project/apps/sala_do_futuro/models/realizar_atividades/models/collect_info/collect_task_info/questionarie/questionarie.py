from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie import Questions, QuestionInfo
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_section.collect_section import CollectSection
from project import types

class Questionarie:
    def __init__(
            self, page, elem_section_class, 
            can_get_points, btn_end_activity, btn_save_as_draft_activity,
            question='div.css-b200pa'
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

            print(f'{should_get_score}\n\n')

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

            return questionarie
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter informações das questões: {e}')

            """
            
            ^ TaskInfo
            ^ {
            ^    'status_activity': 'A Fazer',
            ^    'site_activity_id': '67467346',
            ^    'auto_activity_id': '', 'activity_type': 'Tarefa SP', 'material_activity': 'História',
            ^    'activity_title': 'Crise da democracia liberal: a ascensão do nazismo',
            ^    'user': 'Daniel Oliveira Matias', 'author': 'rafaelcandido3034757-sp', 'class_school': '3º B EM',
            ^    'expires_in': '16/05/2025 - 23:59:59', 'time_spent': '', 'draft': '', 'submitted': '',
            ^    'question_types': {}
            ^ }

            ? Questionarie
            ? {
            ? 0: {
            ?     'quest_info': {
            ?         'required': True, 
            ?         'time': {
            ?             'day': '', 'start_time': '', 'end_time': ''
            ?         }, 'activity_score': '', 'score': '', 'section': '', 'number_of_guesses': '',
            ?         'number_of_user_responses': '', 'user_feedback': '', 'difficulty': '',
            ?         'history_of_attempts': {}, 'error_num': '', 'error_types': ['', '', ''],
            ?         'error_logs': {
            ?             '0': {
            ?                 'type': '', 'details': '', 'question': '', 'timestamp': ''
            ?             }
            ?         }, 'ia': '', 'time_spent': ''
            ?     },
            ?     'quest': {
            ?         'type': 'Unknown Type',
            ?         'statement': 'O artigo traz uma reflexão sobre a cidade de Weimar, na Alemanha, e sua relação com o nazismo nas décadas de 1920 e 1930, demonstrando uma característica essencial do regime totalitário alemão. Ordene as palavras para completar corretamente a frase sobre a característica do nazismo evidenciada no texto.O nazismo se fez em oposição à República de Weimar, por isso se caracteriza como um regime....',
            ?         'alternatives': [''], 'answer': ''
            ?     }
            ? },
            ? 1: {'quest_info': {'required': True, 'time': {'day': '', 'start_time': '', 'end_time': ''}, 'activity_score': '', 'score': '', 'section': '', 'number_of_guesses': '', 'number_of_user_responses': '', 'user_feedback': '', 'difficulty': '', 'history_of_attempts': {}, 'error_num': '', 'error_types': ['', '', ''], 'error_logs': {'0': {'type': '', 'details': '', 'question': '', 'timestamp': ''}}, 'ia': '', 'time_spent': ''}, 'quest': {'type': 'Radios', 'statement': 'A República de Weimar foi um governo estabelecido na Alemanha após a Primeira Guerra Mundial. O partido fez forte oposição a esse governo republicano até derrubá-lo, substituindo-o por um regime totalitário. Assinale a alternativa que demonstra corretamente a situação da República de Weimar que proporcionou a ascensão da oposição nazista e a consequente queda desse governo.', 'alternatives': ['A) O regime de Weimar teve um enorme sucesso econômico, mas não compensou as perdas sofridas com a Primeira Guerra, como prometiam os nazistas.', 'B) O modelo comunista adotado por Weimar aumentou a insatisfação popular e facilitou a oposição nazista.', 'C) O governo de Weimar cancelou o Tratado de Versalhes, enfurecendo os nazistas, que apoiavam o tratado de fim da Primeira Guerra.', 'D) A estratégia econômica de Weimar causou a crise de 1929 no mundo, o que fez com que os nazistas parassem de apoiar o governo.', 'E) O cenário de crise econômica, política e social, gerado pela guerra e agravado pela crise de 1929, levou os nazistas a conspirarem contra Weimar.'], 'answer': ''}}, 2: {'quest_info': {'required': True, 'time': {'day': '', 'start_time': '', 'end_time': ''}, 'activity_score': '', 'score': '', 'section': '', 'number_of_guesses': '', 'number_of_user_responses': '', 'user_feedback': '', 'difficulty': '', 'history_of_attempts': {}, 'error_num': '', 'error_types': ['', '', ''], 'error_logs': {'0': {'type': '', 'details': '', 'question': '', 'timestamp': ''}}, 'ia': '', 'time_spent': ''}, 'quest': {'type': 'Checkbox', 'statement': 'Os nazistas e Hitler percorreram um longo caminho até chegarem ao poder, utilizando-se de diversos expedientes, inclusive criminosos. Assinale a(s) alternativa(s) correta(s) sobre o processo de tomada de poder pelos nazistas na Alemanha.', 'alternatives': ['A) Em 1923, em sua primeira tentativa de golpe, conhecida como o "Putsch de Munique", Hitler obteve pela primeira vez o poder político na Alemanha.', 'B) O oportunismo de Hitler ao usar um incêndio no parlamento em 1933 como propaganda anticomunista foi um marco do estabelecimento da ditadura nazista.', 'C) As ambições totalitárias de Hitler se traduziram na sua ideia de reconstrução do "império alemão", o Terceiro Reich.', 'D) O envolvimento da população foi pequeno, uma vez que Hitler efetuou seu assalto ao poder com apoio do exército.', 'E) A criação de órgãos de repressão, como grupos paramilitares e órgãos policiais, foi essencial para o controle social e silenciamento da oposição.'], 'answer': ''}}, 3: {'quest_info': {'required': True, 'time': {'day': '', 'start_time': '', 'end_time': ''}, 'activity_score': '', 'score': '', 'section': '', 'number_of_guesses': '', 'number_of_user_responses': '', 'user_feedback': '', 'difficulty': '', 'history_of_attempts': {}, 'error_num': '', 'error_types': ['', '', ''], 'error_logs': {'0': {'type': '', 'details': '', 'question': '', 'timestamp': ''}}, 'ia': '', 'time_spent': ''}, 'quest': {'type': 'Radios', 'statement': 'A partir da leitura do texto e de seus conhecimentos sobre a ideologia nazista, assinale a alternativa que completa corretamente as lacunas do parágrafo.As liberdades econômicas, políticas e sociais eram ________ pela ideologia nazista. Deveria prevalecer o ideal do ________ soberano, que domina e controla a sociedade para levá-la a um suposto momento de grandeza, que estaria, ainda supostamente, perdido no passado e esperando para ser resgatado pelo líder. Usando o ________ como forma de manipular a população, dizem que existem "inimigos" do povo que destruíram essa grandeza e que, portanto, devem ser ________, acrescentando a essa ideia de inimigo um elemento ________ ao apontar para os judeus como os supostos causadores dos males. A manipulação social, a violência política e o racismo são, portanto, os elementos fundamentais que compõem a ideologia nazista.', 'alternatives': ['A) repudiadas – Estado – medo – eliminados – racista.', 'B) repudiadas – povo – medo – educados – racista.', 'C) defendidas – povo – diálogo – educados – econômico.', 'D) repudiadas – Estado – diálogo – educados – racista.', 'E) defendidas – povo – diálogo – eliminados – econômico.'], 'answer': ''}}}

            """

            return
        