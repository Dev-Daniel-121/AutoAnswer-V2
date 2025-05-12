from .collect_tarefas import CollectTarefas, CollectTaskInfos
from .collect_task_info.collect_task_info import TaskInfo
from .collect_task_info.questionarie import Questionarie
from .collect_json import CollectJson, SaveJson
from .collect_task_info.texts import Text
from project import Display, LogType
from .collect_time import Time

class CollectInfo:
    def __init__(self, page, activity_status, component):
        self.page = page
        self.display = Display
        self.component = component
        self.activity_status = activity_status

        self.time = Time()
        self.save_json = SaveJson()
        self.collect_json = CollectJson()
        self.collect_tarefas = CollectTarefas(page=self.page)

        self.task_info = TaskInfo(
            page=self.page, activity_status=self.activity_status,
            activity_type_class = ':nth-match(li.MuiBreadcrumbs-li, 2)',
            material_activity_class = 'h6.css-yq44kw',
            activity_title_class = 'p.css-zscg42'
        )

        self.text = Text(
            page=self.page, information_card_class='css-1mpla7o', elem_section_class='div.css-8atqhb h2'
        )

        self.questionarie = Questionarie(
            page=self.page, elem_section_class='div.css-8atqhb h2',
            can_get_points='div.css-18oghjr', btn_end_activity='button.css-1wjnhbh',
            btn_save_as_draft_activity='button.css-19d44l7', question='div.css-b200pa'
        )

        self.collect_task_infos = CollectTaskInfos(
            page = self.page,
            component_class = 'h6.css-yq44kw',
            title_activity_class = 'p.css-zscg42',
            user_activity_class = ':nth-match(p.css-dyxuuh, 1)',
            author_activity_class = ':nth-match(p.css-dyxuuh, 2)',
            class_activity_class = ':nth-match(p.css-dyxuuh, 3)',
            expire_activity_class = ':nth-match(p.css-dyxuuh, 4)',
            id_activity_class = ':nth-match(p.css-dyxuuh, 5)'
        )

        self.ia = {
            'ia': 'Grok 3 - Smartest',
            'prompt': '''
                ### Instruções
                Você receberá algumas questões em formato de um JSON (dicionário Python). Seu trabalho é processar cada questão e retornar as respostas no mesmo formato JSON especificado abaixo. Algumas questões podem incluir imagens anexadas, outras podem não ter alternativas, e há casos em que a "questão" pode ser apenas uma imagem, sem texto. Analise cada caso e preencha o JSON de acordo com as regras fornecidas. Todas as respostas devem ser em português.

                ### Formato JSON Esperado
                {
                "0": {
                    "type": "TIPO DA QUESTÃO",
                    "alternatives": {
                        "media": {DADOS DE MÍDIA DA QUESTÃO},
                        "alternative": ["ALTERNATIVAS"]
                    },
                    "answer": "RESPOSTA PARA TAREFA"
                }
                }

                ### Regras para Preenchimento
                - Índice: Cada questão será representada por um número sequencial começando de 0 (ex.: "0", "1", etc.).
                - Campo `type`:
                - Identifique o tipo da questão (ex.: "Múltipla Escolha", "Resposta Curta", etc.).
                - Se o tipo não puder ser determinado (como uma imagem sem contexto), defina `type` como uma string vazia (`''`).
                - Campo `alternatives`:
                - Se houver alternativas, inclua um objeto `alternatives` com:
                    - `media`: Dados da mídia, como `{ "type": "image", "url": "[link ou descrição]" }` se houver imagem, ou `null` se não houver.
                    - `alternative`: Lista de alternativas (ex.: `["A) Opção 1", "B) Opção 2"]`).
                - Se não houver alternativas, defina `alternatives` como `null`.
                - Campo `answer`:
                - Para questões com alternativas, forneça a resposta correta (ex.: "A)", "B)", etc.).
                - Para questões sem alternativas, forneça uma resposta curta ou descritiva adequada.
                - Para questões que são apenas imagens, analise a imagem e forneça uma descrição ou resposta baseada na análise.
                - Se não for possível responder a questão (ex.: falta de informações ou contexto insuficiente), deixe o campo `answer` como uma string vazia (`''`).

                ### Exemplo de Entrada e Saída
                1. **Entrada**: Questão com imagem e alternativas
                {
                    "0": {
                        "question": "Qual animal está na imagem?",
                        "media": {"type": "image", "url": "[link]"},
                        "alternatives": ["A) Cachorro", "B) Gato"]
                    }
                }
                **Saída**:
                {
                    "0": {
                        "type": "Múltipla Escolha",
                        "alternatives": {
                            "media": {"type": "image", "url": "[link]"},
                            "alternative": ["A) Cachorro", "B) Gato"]
                        },
                        "answer": "B)"
                    }
                }

                2. **Entrada**: Questão sem alternativas
                {
                    "0": {
                        "question": "Qual é a capital do Brasil?"
                    }
                }
                **Saída**:
                {
                    "0": {
                        "type": "Resposta Curta",
                        "alternatives": null,
                        "answer": "Brasília"
                    }
                }

                3. **Entrada**: Apenas uma imagem
                {
                    "0": {
                        "media": {"type": "image", "url": "[link]"}
                    }
                }
                **Saída**:
                {
                    "0": {
                        "type": "",
                        "alternatives": {
                            "media": {"type": "image", "url": "[link]"},
                            "alternative": null
                        },
                        "answer": "Descrição ou resposta baseada na análise da imagem"
                    }
                }

                4. **Entrada**: Questão sem informações suficientes
                {
                    "0": {
                        "question": "Ordene as palavras.",
                        "alternatives": [""]
                    }
                }
                **Saída**:
                {
                    "0": {
                        "type": "",
                        "alternatives": {
                            "media": null,
                            "alternative": [""]
                        },
                        "answer": ""
                    }
                }

                ### Notas Finais
                - Retorne um único JSON com todas as questões processadas.
                - Para tipos desconhecidos, use `type` como `''`.
                - Analise imagens quando necessário para gerar respostas adequadas.
                - Se não for possível responder, deixe `answer` como `''`.
            '''
        }

    def display_info(self, task_info, texts, quests):
        type_counter = {}
        unknown_type_questions = []

        informative_cards = {k: v for k, v in texts.items() if k.isdigit()}

        for quest_num, quest_data in quests.items():
            if not quest_num.isdigit():
                continue

            quest_type = quest_data.get('quest', {}).get('type', '').strip()
            if not quest_type or quest_type == 'Unknown Type':
                unknown_type_questions.append(str(int(quest_num) + 1))
            else:
                type_counter[quest_type] = type_counter.get(quest_type, 0) + 1

        task_info['question_types'] = type_counter
        task_info['text_num'] = len(informative_cards)

        print(f'[{LogType.INFO}] Número de Cards Informativos: {len(informative_cards)}')
        print(f'[{LogType.INFO}] Número de Questões: {len(quests)}\n')

        print(f'[{LogType.INFO}] Tipos de Questões Encontradas:')
        for qtype, count in type_counter.items():
            print(f'   [{LogType.INFO}] {qtype}: {count}')

        if unknown_type_questions:
            print(f'\n[{LogType.INFO}] Questões Desconhecidas Encontradas:')
            print(f'   [{LogType.INFO}] Questões: {", ".join(unknown_type_questions)}\n')

    def run(self, user, id_usuario):
        task_info = self.task_info.run()

        # component, title_activity, user_activity, author_activity, class_activity, expire_activity, id_activity = self.collect_task_infos.run()

        options = self.display(data='', title=f'{task_info['material_activity']} - {task_info['site_activity_id']}', answer=False, user=f'{user}', title_quest='')
        options.display()

        self.time.timer(seconds=60)

        self.collect_json.run(component=self.component, id_activity=task_info['site_activity_id'])

        text = self.text.run()
        questionarie = self.questionarie.run()

        self.display_info(task_info=task_info, texts=text, quests=questionarie)

        self.save_json.save_activity(
            ia=self.ia,
            materia=self.component,
            user_id=id_usuario, 
            task_info=task_info, 
            texts=text, 
            questionarie=questionarie
        )

        """
        self.collect_tarefas.run()

        print(f'\n\n\n{task_info}\n\n\n')
        print(f'{text}\n\n\n')
        print(f'{questionarie}\n\n\n')
        """

        self.time.tempo_restante()


"""

    Infomações
    * Quantas questões (Count div.css-b200pa)
    * Quantos Textos (Count div.css-1mpla7o > p)
    * Quantas Imgs (Count div.css-1mpla7o > p > img)
    * Quantos Mp4 (Count div.css-1mpla7o > div.css-pcbmqt)
    ? Quantos Gifs

    Coletar informações das questões

    ? Radio
        Tipo de Questão                 (div.css-b200pa > div.MuiRadioGroup-root)
        Questão atual                   (div.css-b200pa > p.css-m576f2 > b)
        Obrigatória                     (div.css-b200pa > p.css-sz9ejl)
        Pontuação Possivel da Questão   (div.css-b200pa > p.css-1wgaj9w)
        Titulo da questão               (div.css-b200pa > div.css-1a4wlpz > p)
        Alternativas                    (div.css-b200pa > div.css-9whsf3)
        Conteúdo da Alternativa         (div.css-b200pa > div.css-9whsf3 > div.css-1p78i1z > p)
        Resposta                        (div.css-b200pa > div.css-9whsf3 > input.css-1m9pwf3).click

    ? Right Wrong
        Tipo de Questão                 (div.css-b200pa > div.css-70qvj9)
        Questão atual                   (div.css-b200pa > p.css-m576f2 > b)
        Obrigatória                     (div.css-b200pa > p.css-sz9ejl)
        Pontuação Possivel da Questão   (div.css-b200pa > p.css-1wgaj9w)
        Titulo da questão               (div.css-b200pa > div.css-1a4wlpz > p)
        Alternativas                    (div.css-b200pa > div.css-70qvj9)
        Título da Alternativa           (div.css-b200pa > div.css-70qvj9 > div.css-8atqhb > p)
        Título da opção da Alternativa  (div.css-b200pa > div.css-70qvj9 > label.css-geqbjm > span.css-1h7gjlg)
        Resposta                        (div.css-b200pa > div.css-70qvj9 > label.css-geqbjm > input.css-1m9pwf3).click

"""



{
    "0": {
        "quest_info": {
            "required": True,
            "time": {"day": "", "start_time": "", "end_time": ""},
            "activity_score": "",
            "score": "",
            "section": "",
            "number_of_guesses": "",
            "number_of_user_responses": "",
            "user_feedback": "",
            "difficulty": "",
            "media": {"video": {}, "image": {}, "gif": {}},
            "history_of_attempts": {},
            "error_num": "",
            "error_types": ["", "", ""],
            "error_logs": {
                "0": {"type": "", "details": "", "question": "", "timestamp": ""}
            },
            "ia": "",
            "time_spent": "",
        },
        "quest": {
            "type": "Unknown Type",
            "statement": 'O título das notícias sintetiza o fato central abordado no texto e destaca informações consideradas importantes para atrair a atenção do leitor. As informações mais importantes da notícia respondem às perguntas básicas do jornalismo: "O quê?", "Quem?", "Quando?", "Onde?", "Como?" e "Por quê?". Com relação à composição do título dessa notícia, associe corretamente às lacunas a seguir.I. O quê?II. Onde?III. Quem?( ) estudante de Escola Pública( ) conquista Medalha de Ouro( ) em Concurso de Redação no Estado de São Paulo',
            "alternatives": {"media": {}, "alternative": [""]},
            "answer": "",
        },
    },
    "1": {
        "quest_info": {
            "required": True,
            "time": {"day": "", "start_time": "", "end_time": ""},
            "activity_score": "",
            "score": "",
            "section": "",
            "number_of_guesses": "",
            "number_of_user_responses": "",
            "user_feedback": "",
            "difficulty": "",
            "media": {"video": {}, "image": {}, "gif": {}},
            "history_of_attempts": {},
            "error_num": "",
            "error_types": ["", "", ""],
            "error_logs": {
                "0": {"type": "", "details": "", "question": "", "timestamp": ""}
            },
            "ia": "",
            "time_spent": "",
        },
        "quest": {
            "type": "Radios",
            "statement": "Ao destacar determinadas informações a respeito do fato noticiado e apresentar o ponto de vista do aluno na notícia, o texto jornalístico expressa uma determinada perspectiva com relação ao tema abordado. A respeito disso, julgue as afirmativas a seguir em verdadeiras (V) ou falsas (F). Depois, assinale a alternativa correta.I. A notícia mostra um ponto de vista positivo em relação à influência do hip-hop e da literatura no desenvolvimento dos jovens.II. A notícia sugere que os jovens de escolas públicas devem se aproximar da cultura hip-hop para alcançarem um bom desempenho escolar.III. A notícia valoriza a participação de jovens estudantes em campeonatos e olimpíadas escolares, reconhecendo os resultados como conquistas importantes.",
            "alternatives": {
                "media": {},
                "alternative": [
                    {
                        "text": "A) F – F – V.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "B) F – V – V.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "C) V – F – F.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "D) V – F – V.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "E) V – V – F.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                ],
            },
            "answer": "",
        },
    },
    "2": {
        "quest_info": {
            "required": True,
            "time": {"day": "", "start_time": "", "end_time": ""},
            "activity_score": "",
            "score": "",
            "section": "",
            "number_of_guesses": "",
            "number_of_user_responses": "",
            "user_feedback": "",
            "difficulty": "",
            "media": {"video": {}, "image": {}, "gif": {}},
            "history_of_attempts": {},
            "error_num": "",
            "error_types": ["", "", ""],
            "error_logs": {
                "0": {"type": "", "details": "", "question": "", "timestamp": ""}
            },
            "ia": "",
            "time_spent": "",
        },
        "quest": {
            "type": "Radios",
            "statement": 'A notícia utiliza diferentes recursos para apresentar aos leitores a perspectiva do aluno Guilherme a respeito de sua conquista no Concurso de Redação. Releia a seguir uma citação em discurso indireto presente no texto: Estudante do sétimo ano, Guilherme atribui sua vitória ao incentivo da mãe e à influência do hip-hop e da literatura negra, que moldaram sua visão de mundo e inspiraram a redação premiada.Fonte: https://www.jornaldorap.com.br/noticias/estudante-de-escola-publica-conquista-medalha-de-ouro-em-concurso-de-redacao-no-estado-de-sao-paulo/.Esse trecho enumera para o leitor quais foram as influências às quais Guilherme atribuiu sua vitória. A conjunção "e" utilizada nessa enumeração expressa sentido de...',
            "alternatives": {
                "media": {},
                "alternative": [
                    {
                        "text": "A) adição.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "B) oposição.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "C) conclusão.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "D) alternativa.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "E) consequência.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                ],
            },
            "answer": "",
        },
    },
    "3": {
        "quest_info": {
            "required": True,
            "time": {"day": "", "start_time": "", "end_time": ""},
            "activity_score": "",
            "score": "",
            "section": "",
            "number_of_guesses": "",
            "number_of_user_responses": "",
            "user_feedback": "",
            "difficulty": "",
            "media": {"video": {}, "image": {}, "gif": {}},
            "history_of_attempts": {},
            "error_num": "",
            "error_types": ["", "", ""],
            "error_logs": {
                "0": {"type": "", "details": "", "question": "", "timestamp": ""}
            },
            "ia": "",
            "time_spent": "",
        },
        "quest": {
            "type": "Radios",
            "statement": "(COMVEST Vestibular Indígena, 2019 - Adaptado)Turismo em Terras IndígenasMais do que a possibilidade de visitar belezas naturais intocadas, o turista em uma terra indígena tem a oportunidade de entrar em contato com línguas, narrativas, conhecimentos e comidas da comunidade, algo antes restrito a populações originárias e a uma pequena parcela de não indígenas. Esse intercâmbio gera ainda outros desdobramentos, como afirma o Coordenador-Geral de Etnodesenvolvimento da Funai, Juan Scalia. “O turismo de base comunitária em terras indígenas fortalece a autonomia dos povos, propiciando uma alternativa de geração de renda com mínimos impactos ambientais e com uma distribuição mais justa dos lucros da atividade. Valorizar os diversos atrativos ecológicos e culturais, por outro lado, também contribui para a proteção dos territórios e fortalecimento das tradições”, afirmou.Fonte: http://www.funai.gov.br/index.php/comunicacao/noticias/5224-etnoturismo-ealternativa-sustentavel-de-renda-para-comunidades-indigenas-do-rio-negro.Segundo o texto, o turismo em terras indígenas",
            "alternatives": {
                "media": {},
                "alternative": [
                    {
                        "text": "A) constitui a principal fonte de renda da comunidade indígena mencionada no texto.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "B) é útil para a divulgação respeitosa das especificidades culturais da comunidade.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "C) favorece alianças entre as comunidades e as agências de turismo envolvidas.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "D) provoca, inevitavelmente, impactos ambientais sérios e indesejáveis.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "E) substitui os saberes ancestrais por práticas turísticas comerciais.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                ],
            },
            "answer": "",
        },
    },
}
