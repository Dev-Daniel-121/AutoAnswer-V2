from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie import Questions
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
            data = {}
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

                quest_type = question_obj.get_quest_type()
                statement = question_obj.get_question_statement()
                alternatives = question_obj.get_question_alternatives(quest_type)
                isRequired = question_obj.isRequired()

                data[i] = {
                    'quest_info': {
                    },
                    'quest': {
                        'type': quest_type or '',
                        'required': isRequired or '',
                        'statement': statement or '',
                        'alternatives': alternatives if alternatives else [''],
                        'answer': ''
                    }
                }
                
                # print(f'\n{'-' * 30}\n')
                # print(f'Questão: {i + 1}')
                # print(f'Tipo: {data[i]['quest']['type']}')
                # print(f'Obrigatório: {data[i]['quest']['required']}\n')
                # print(f'\nEnunciado: {data[i]['quest']['statement']}\n')
                # print(f'\nAlternativas: {data[i]['quest']['alternatives']}\n')

            return data
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter informações das questões: {e}')
            return
    
    '''
    
    Essa classe tem que para cada div.css-b200pa ele tem que chamar a classe QUESTIONS e QUESTION_INFO

    A classe QUESTIONS coleta informações dentro da questão relacionados ao que ela solicita ser feito

    A classe QUESTION_INFO coleta informações dentro da questão relacionados a dados como pontuação, ect.


    Esse código tem que retornar isso:

    0: {
        quest_info {
            obrigatoria: '',
            pontuação_da_questao: '',
            pontuação_adiquirida: '',
            secao: '',
            num_de_chutes: '',
            num_de_user_resposta: '',
            feedback_usuario: '',
            dificuldade: '',
            historico_tentativas: {
                0: { quest: '', 'autor': '', 'resultado': '', 'tempo': '' },
                1: { quest: '', 'autor': '', 'resultado': '', 'tempo': '' }
            },
            num_de_erro: '',
            tipos_de_erro: ['', '', ''],
            logs_de_erro: {
                0: {
                    tipo: '',
                    detalhes: '',
                    questao: '',
                    timestamp: ''
                }
            },
            ia: '',
            tempo_gasto: '',
        },
        quest: {
            tipo: '',
            enunciado: '',
            alternativas: ['', '', '', '', ''],
            resposta: ''
        }
    },
    1: {
        quest_info {
            pontuação_da_questao: '',
            pontuação_adiquirida: '',
            secao: '',
            num_de_chutes: '',
            num_de_user_resposta: '',
            feedback_usuario: '',
            dificuldade: '',
            historico_tentativas: {
                0: { quest: '', 'autor': '', 'resultado': '', 'tempo': '' },
                1: { quest: '', 'autor': '', 'resultado': '', 'tempo': '' }
            },
            num_de_erro: '',
            tipos_de_erro: ['', '', ''],
            logs_de_erro: {
                0: {
                    tipo: '',
                    detalhes: '',
                    questao: '',
                    timestamp: ''
                }
            },
            ia: '',
            tempo_gasto: '',
        },
        quest: {
            tipo: '',
            enunciado: '',
            alternativas: ['', '', '', '', ''],
            resposta: ''
        }
    },
    
    '''