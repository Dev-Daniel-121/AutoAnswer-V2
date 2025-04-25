from project.apps.sala_do_futuro.menus import MenuSystem
from playwright.sync_api import sync_playwright
from project import SistemaUsuarios, types

class SalaDoFuturo:
    def __init__(self):
        self.sistema_usuarios = SistemaUsuarios()

    def run(self, id_usuario):
        usuarios = self.sistema_usuarios.carregar_usuarios()
        usuario = usuarios.get(str(id_usuario))

        if not usuario:
            print(f'[{types[4]}] Usuário com ID {id_usuario} não encontrado.')
            return

        print(f'\n[{types[9]}] Iniciando automação para {usuario.nome} {usuario.sobrenome} ({usuario.tipo_conta})')

        with sync_playwright() as p:
            try:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto('https://saladofuturo.educacao.sp.gov.br/')
            except Exception as e:
                print(f'[{types[4]}] Erro ao entrar no site Sala Do Futuro. {e}')
            
            try:
                menu_system = MenuSystem(page)
                menu_system.run(usuario)
            except Exception as e:
                print(f'[{types[4]}] Erro ao inicializar Sistema De Menu. {e}')

'''
    {
        "id_usuario": "" { # Id do Usuário
            # Se for Tarefa
            "ID_DA_ATIVIDADE": { # ID automático gerado pelo programa
                "HEADER_INFO": {
                    "status_atividade": "", # A fazer, Entregue, Expirada
                    "id_da_atividade_do_site": "00000000", # ID da atividade pelo site
                    "tipo_atividade": "", # Tipo da Atividade (Tarefa, Redação ou Prova)
                    "matéria": "",
                    "titulo_atividade": "", # Título da Atividade
                    "usuario": "", # Usuário que realizou a atividade
                    "autor": "", # Autor da Atividade
                    "turma": "",
                    "data_expiracao": "00/00/0000 - 00:00:00",
                    "tempo_gasto": "00:00:00", # Tempo Cronometrado pelo programa para fazer a atividade
                    "rascunho": "", # Se o user optiou por salvar como rascunho ele irá contar quantas vezes a atividade foi salva dessa forma
                    "enviado": "", # Se o usuer optiou por enviar ele irá contar
                },

                # Se matéria for Multidisciplinar
                "QUESTIONS_INFO": {
                    "HEADER_QUIESTIONS": {
                        "pontuação_da_atividade": "", # Pontuação total que a atividade proporciona
                        "pontuação_adiquirida": "", # Pontuação que o programa adiquiriu
                        "num_de_textos": "", # Número total de textos
                        "num_de_questoes": "", # Número total de questões
                        "num_de_secoes": "", # Número total de seções
                        "secoes": [
                            { "num_da_secao": "", "nome_da_secao": "" },
                        ],
                        "num_de_chutes": "", # Número total de chutes
                        "num_de_user_resposta": "", # Número total de vezes que o usuário respondeu sem o programa
                        "feedback_usuario": "",
                        "dificuldade": "", # Fácil, Média, Difícil
                        "historico_tentativas": [
                            { "tentativa": 1, "autor": "", "resultado": "", "tempo": "" },
                        ],
                        "analise_ia": {
                            "desempenho_geral": "Bom",
                            "sugestoes": [
                                "Aumente a quantidade de detalhes na questão 3",
                                "Reforce o estudo sobre equações quadráticas"
                            ]
                        },
                        "num_de_erros": "", # Número total de erros
                        "ERROR_TYPES": {}, # Tipos de Erros
                        "LOGS_DE_ERROS": { # Logs de Erros
                            "num_erro": {
                                "tipo": "",
                                "detalhes": "",
                                "questao": "",
                                "timestamp": ""
                            }
                        },
                        "QUESTIONS_TYPES": { # Número de quantas vezes cada tipo de questão apareceu
                            "card-img":"",
                            "card-gif": "",
                            "card-video": "",
                            "Text": "",
                            "Radios": "",
                            "Checkbox": "",
                            "Dragable": "",
                            "Order": "",
                            "Textarea": "",
                            "Select": ""
                        }
                    },
                    "QUESTIONS": {
                        "numero_da_questao": {
                            "secao": { "num_da_secao": "", "nome_da_secao": "" },
                            "tipo": "",
                            "titulo": "",
                            "alternativas": ["Algo 1", "Algo 2", "Algo 3", "Algo 4", "Algo 5"],
                            "ia": "", # Ia que foi usada
                            "resposta": "",
                            "num_de_chutes": "", # Se teve algum chute ele irá contar
                            "user_resposta": "", # Se o usuário teve que responder ele irá contar
                            "tempo_gasto": "", # Tempo cronometrado pelo programa para colocar a resposta
                            "erro": "" # Algum erro na hora de responder alguma pergunta
                        },
                    }
                },
                "QUESTIONS_INFO": {
                    "HEADER_QUIESTIONS": {
                        "pontuação_da_atividade": "", # Pontuação total que a atividade proporciona
                        "pontuação_adiquirida": "", # Pontuação que o programa adiquiriu
                        "num_de_textos": "", # Número total de textos
                        "num_de_questoes": "", # Número total de questões
                        "num_de_chutes": "", # Número total de chutes
                        "num_de_user_resposta": "", # Número total de vezes que o usuário respondeu sem o programa
                        "feedback_usuario": "",
                        "dificuldade": "", # Fácil, Média, Difícil
                        "historico_tentativas": [
                            { "tentativa": 1, "autor": "", "resultado": "", "tempo": "" },
                        ],
                        "analise_ia": {
                            "desempenho_geral": "Bom",
                            "sugestoes": [
                                "Aumente a quantidade de detalhes na questão 3",
                                "Reforce o estudo sobre equações quadráticas"
                            ]
                        },
                        "num_de_erros": "", # Número total de erros
                        "ERROR_TYPES": {}, # Tipos de Erros
                        "LOGS_DE_ERROS": { # Logs de Erros
                            "num_erro": {
                                "tipo": "",
                                "detalhes": "",
                                "questao": "",
                                "timestamp": ""
                            }
                        },
                        "QUESTIONS_TYPES": { # Número de quantas vezes cada tipo de questão apareceu
                            "card-img":"",
                            "card-gif": "",
                            "card-video": "",
                            "Text": "",
                            "Radios": "",
                            "Checkbox": "",
                            "Dragable": "",
                            "Order": "",
                            "Textarea": "",
                            "Select": ""
                        }
                    },
                    "TEXTOS": {
                        "num_text": { # Número gerado automaticamente pelo programa para diferenciar os textos
                            "conteudo": "",
                        },
                    },
                    "QUESTIONS": {
                        "numero_da_questao": {
                            # Se o tipo for Radios
                            "tipo": "Radios",
                            "titulo": "",
                            "alternativas": ["Algo 1", "Algo 2", "Algo 3", "Algo 4", "Algo 5"],
                            "ia": "", # Ia que foi usada
                            "resposta": "", # Apenas 1 alternativa
                            "num_de_chutes": "", # Se teve algum chute ele irá contar
                            "user_resposta": "", # Se o usuário teve que responder ele irá contar
                            "tempo_gasto": "", # Tempo cronometrado pelo programa para colocar a resposta
                            "erro": "" # Algum erro na hora de responder alguma pergunta
                        },
                        "numero_da_questao": {
                            # Se o tipo for Checkbox
                            "tipo": "Checkbox",
                            "titulo": "",
                            "alternativas": ["Algo 1", "Algo 2", "Algo 3", "Algo 4", "Algo 5"],
                            "ia": "", # Ia que foi usada
                            "resposta": [""], # Minimo 1 alternativa
                            "num_de_chutes": "", # Se teve algum chute ele irá contar
                            "user_resposta": "", # Se o usuário teve que responder ele irá contar
                            "tempo_gasto": "", # Tempo cronometrado pelo programa para colocar a resposta
                            "erro": "" # Algum erro na hora de responder alguma pergunta
                        },
                        "numero_da_questao": {
                            # Se o tipo for Dragable
                            "tipo": "Dragable",
                            "titulo": "",
                            "alternativas": ["Algo 1", "Algo 2", "Algo 3", "Algo 4", "Algo 5"],
                            "ia": "", # Ia que foi usada
                            "resposta": ["Algo 5", "Algo 2", "Algo 4", "Algo 3", "Algo 1"], # Resposta na ordem correta alternativa
                            "num_de_chutes": "", # Se teve algum chute ele irá contar
                            "user_resposta": "", # Se o usuário teve que responder ele irá contar
                            "tempo_gasto": "", # Tempo cronometrado pelo programa para colocar a resposta
                            "erro": "" # Algum erro na hora de responder alguma pergunta
                        },
                        "numero_da_questao": {
                            # Se o tipo for Order
                            "tipo": "Order",
                            "titulo": "",
                            "alternativas": ["Order 1", "Order 2", "Order 3", "Order 4", "Order 5"],
                            "ia": "", # Ia que foi usada
                            "resposta": ["Order 5", "Order 2", "Order 4", "Order 3", "Order 1"], # Resposta na ordem correta alternativa
                            "num_de_chutes": "", # Se teve algum chute ele irá contar
                            "user_resposta": "", # Se o usuário teve que responder ele irá contar
                            "tempo_gasto": "", # Tempo cronometrado pelo programa para colocar a resposta
                            "erro": "" # Algum erro na hora de responder alguma pergunta
                        },
                        "numero_da_questao": {
                            # Se o tipo for Textarea
                            "tipo": "Textarea",
                            "titulo": "",
                            "ia": "", # Ia que foi usada
                            "resposta": "", # Texto
                            "user_resposta": "", # Se o usuário teve que responder ele irá contar
                            "tempo_gasto": "", # Tempo cronometrado pelo programa para colocar a resposta
                            "erro": "" # Algum erro na hora de responder alguma pergunta
                        },
                        "numero_da_questao": {
                            # Se o tipo for Select
                            "tipo": "Select",
                            "titulo": "",
                            "alternativas": ["Opção 1", "Opção 2", "Opção 3", "Opção 4", "Opção 5"],
                            "ia": "", # Ia que foi usada
                            "resposta": ["Opção 5", "Opção 2", "Opção 4", "Opção 3", "Opção 1"], # Resposta na ordem correta alternativa
                            "num_de_chutes": "", # Se teve algum chute ele irá contar
                            "user_resposta": "", # Se o usuário teve que responder ele irá contar
                            "tempo_gasto": "", # Tempo cronometrado pelo programa para colocar a resposta
                            "erro": "" # Algum erro na hora de responder alguma pergunta
                        },
                    }
                }
            }
        },

        # Se for Redação
        "id_usuario": "" { # Id do Usuário
            "ID_DA_ATIVIDADE": { # ID automático gerado pelo programa
                "HEADER_INFO": {
                    "status_atividade": "", # A fazer, Entregue, Expirada
                    "id_da_atividade_do_site": "00000000", # ID da atividade pelo site
                    "tipo_atividade": "", # Tipo da Atividade (Tarefa, Redação ou Prova)
                    "matéria": "",
                    "titulo_atividade": "", # Título da Atividade
                    "usuario": "", # Usuário que realizou a atividade
                    "autor": "", # Autor da Atividade
                    "turma": "",
                    "data_expiracao": "00/00/0000 - 00:00:00",
                    "tempo_gasto": "00:00:00", # Tempo Cronometrado pelo programa para fazer a atividade
                    "rascunho": "", # Se o user optiou por salvar como rascunho ele irá contar quantas vezes a atividade foi salva dessa forma
                    "enviado": "", # Se o usuer optiou por enviar ele irá contar
                },
                "QUESTIONS_INFO": {
                    "HEADER_QUIESTIONS": {
                        "pontuação_da_atividade": "", # Pontuação total que a atividade proporciona
                        "pontuação_adiquirida": "", # Pontuação que o programa adiquiriu
                        "num_min_de_caracteres": "", # Número min de caracteres
                        "num_de_caracteres_escritos": "", # Número de caracteres que o programa fez
                        "genero_textual": "",
                        "criterios_de_avaliacao": {
                            "num_do_criterio": { # Gerado automaticamente pelo programa
                                "competencia": "",
                                "nota": "",
                                "peso": "",
                            },
                        },
                        "num_de_textos": "", # Número total de textos
                        "num_de_redaoes": "", # Número total de redações
                        "num_de_user_resposta": "", # Número total de vezes que o usuário respondeu sem o programa
                        "feedback_usuario": "",
                        "dificuldade": "", # Fácil, Média, Difícil
                        "historico_tentativas": [
                            { "tentativa": 1, "autor": "", "resultado": "", "tempo": "" },
                        ],
                        "analise_ia": {
                            "desempenho_geral": "Bom",
                            "sugestoes": [
                                "Aumente a quantidade de detalhes na questão 3",
                                "Reforce o estudo sobre equações quadráticas"
                            ]
                        },
                        "num_de_erros": "", # Número total de erros
                        "ERROR_TYPES": {}, # Tipos de Erros
                        "LOGS_DE_ERROS": { # Logs de Erros
                            "num_erro": {
                                "tipo": "",
                                "detalhes": "",
                                "questao": "",
                                "timestamp": ""
                            }
                        },
                        "QUESTIONS_TYPES": { # Número de quantas vezes cada tipo de questão apareceu
                            "Text": "",
                        }
                    },
                    "TEXTOS": {
                        "num_text": { # Número gerado automaticamente pelo programa para diferenciar os textos
                            "conteudo": "",
                        },
                    },
                    "QUESTIONS": {
                        "numero_da_questao": {
                            # Se o tipo for Textarea
                            "tipo": "Textarea",
                            "titulo": "",
                            "ia": "", # Ia que foi usada
                            "redacao": "", # Redação
                            "user_resposta": "", # Se o usuário teve que responder ele irá contar
                            "tempo_gasto": "", # Tempo cronometrado pelo programa para colocar a resposta
                            "erro": "" # Algum erro na hora de responder alguma pergunta
                        },
                    }
                }
            }
        },

        # Se for Provas
        "id_usuario": "" { # Id do Usuário
            "ID_DA_ATIVIDADE": { # ID automático gerado pelo programa
                "HEADER_INFO": {
                    "status_atividade": "", # A fazer, Entregue, Expirada
                    "id_da_atividade_do_site": "00000000", # ID da atividade pelo site
                    "tipo_atividade": "", # Tipo da Atividade (Tarefa, Redação ou Prova)
                    "matéria": "",
                    "titulo_atividade": "", # Título da Atividade
                    "usuario": "", # Usuário que realizou a atividade
                    "autor": "", # Autor da Atividade
                    "turma": "",
                    "data_expiracao": "00/00/0000 - 00:00:00",
                    "tempo_gasto": "00:00:00", # Tempo Cronometrado pelo programa para fazer a atividade
                    "rascunho": "", # Se o user optiou por salvar como rascunho ele irá contar quantas vezes a atividade foi salva dessa forma
                    "enviado": "", # Se o usuer optiou por enviar ele irá contar
                },
                "QUESTIONS_INFO": {
                    "HEADER_QUIESTIONS": {
                        "pontuação_da_atividade": "", # Pontuação total que a atividade proporciona
                        "pontuação_adiquirida": "", # Pontuação que o programa adiquiriu
                        "num_de_textos": "", # Número total de textos
                        "num_de_questoes": "", # Número total de questões
                        "num_de_secoes": "", # Número total de seções
                        "secoes": [
                            { "num_da_secao": "", "nome_da_secao": "" },
                        ],
                        "num_de_chutes": "", # Número total de chutes
                        "num_de_user_resposta": "", # Número total de vezes que o usuário respondeu sem o programa
                        "feedback_usuario": "",
                        "dificuldade": "", # Fácil, Média, Difícil
                        "historico_tentativas": [
                            { "tentativa": 1, "autor": "", "resultado": "", "tempo": "" },
                        ],
                        "analise_ia": {
                            "desempenho_geral": "Bom",
                            "sugestoes": [
                                "Aumente a quantidade de detalhes na questão 3",
                                "Reforce o estudo sobre equações quadráticas"
                            ]
                        },
                        "num_de_erros": "", # Número total de erros
                        "ERROR_TYPES": {}, # Tipos de Erros
                        "LOGS_DE_ERROS": { # Logs de Erros
                            "num_erro": {
                                "tipo": "",
                                "detalhes": "",
                                "questao": "",
                                "timestamp": ""
                            }
                        },
                        "QUESTIONS_TYPES": { # Número de quantas vezes cada tipo de questão apareceu
                            "Text": "",
                            "Radios": "",
                            "Checkbox": "",
                        }
                    },
                    "TEXTOS": {
                        "num_text": { # Número gerado automaticamente pelo programa para diferenciar os textos
                            "conteudo": "",
                        },
                    },
                    "QUESTIONS_INFO": {
                        "HEADER_QUIESTIONS": {
                            "pontuação_da_atividade": "", # Pontuação total que a atividade proporciona
                            "pontuação_adiquirida": "", # Pontuação que o programa adiquiriu
                            "num_de_textos": "", # Número total de textos
                            "num_de_questoes": "", # Número total de questões
                            "num_de_secoes": "", # Número total de seções
                            "secoes": [
                                {
                                    "num_da_secao": "",
                                    "nome_da_secao": ""
                                },
                            ],
                            "num_de_chutes": "", # Número total de chutes
                            "num_de_user_resposta": "", # Número total de vezes que o usuário respondeu sem o programa
                            "feedback_usuario": "",
                            "dificuldade": "", # Fácil, Média, Difícil
                            "historico_tentativas": [
                                { "tentativa": 1, "autor": "", "resultado": "", "tempo": "" },
                            ],
                            "analise_ia": {
                                "desempenho_geral": "Bom",
                                "sugestoes": [
                                    "Aumente a quantidade de detalhes na questão 3",
                                    "Reforce o estudo sobre equações quadráticas"
                                ]
                            },
                            "num_de_erros": "", # Número total de erros
                            "ERROR_TYPES": {}, # Tipos de Erros
                            "LOGS_DE_ERROS": { # Logs de Erros
                                "num_erro": {
                                    "tipo": "",
                                    "detalhes": "",
                                    "questao": "",
                                    "timestamp": ""
                                }
                            },
                            "QUESTIONS_TYPES": { # Número de quantas vezes cada tipo de questão apareceu
                                "card-img":"",
                                "card-gif": "",
                                "card-video": "",
                                "Text": "",
                                "Radios": "",
                                "Checkbox": "",
                                "Dragable": "",
                                "Order": "",
                                "Textarea": "",
                                "Select": "",
                            }
                        },
                        "TEXTOS": {
                            "num_text": { # Número gerado automaticamente pelo programa para diferenciar os textos
                                "conteudo": "",
                            },
                        },
                        "QUESTIONS": {
                            "numero_da_questao": {
                                # Se o tipo for Radios
                                # "secao": { "num_da_secao": "", "nome_da_secao": "" },
                                "tipo": "Radios",
                                "titulo": "",
                                "alternativas": ["Algo 1", "Algo 2", "Algo 3", "Algo 4", "Algo 5"],
                                "ia": "", # Ia que foi usada
                                "resposta": "", # Apenas 1 alternativa
                                "num_de_chutes": "", # Se teve algum chute ele irá contar
                                "user_resposta": "", # Se o usuário teve que responder ele irá contar
                                "tempo_gasto": "", # Tempo cronometrado pelo programa para colocar a resposta
                                "erro": "" # Algum erro na hora de responder alguma pergunta
                            },
                            "numero_da_questao": {
                                # Se o tipo for Checkbox
                                "secao": { "num_da_secao": "", "nome_da_secao": "" },
                                "tipo": "Checkbox",
                                "titulo": "",
                                "alternativas": ["Algo 1", "Algo 2", "Algo 3", "Algo 4", "Algo 5"],
                                "ia": "", # Ia que foi usada
                                "resposta": [""], # Minimo 1 alternativa
                                "num_de_chutes": "", # Se teve algum chute ele irá contar
                                "user_resposta": "", # Se o usuário teve que responder ele irá contar
                                "tempo_gasto": "", # Tempo cronometrado pelo programa para colocar a resposta
                                "erro": "" # Algum erro na hora de responder alguma pergunta
                            },
                        }
                    }
                }
            }
        },
    }
'''