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
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('https://saladofuturo.educacao.sp.gov.br/')
            
            menu_system = MenuSystem(page)
            menu_system.run(usuario)

'''
    {
        "ID_DA_ATIVIDADE": { # ID automático gerado pelo programa
            # Se for Tarefa
            "HEADER_INFO": {
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
                    "num_de_chutes": "", # Número total de chutes
                    "num_de_user_resposta": "", # Número total de vezes que o usuário respondeu sem o programa
                    "num_de_erros": "", # Número total de erros
                    "ERROR_TYPES": {}, # Tipos de Erros
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
                "TEXTO": {
                    "num_text": "", # Número gerado automaticamente pelo programa para diferenciar os textos
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

        # Se for Redação
        "ID_DA_ATIVIDADE": { # ID automático gerado pelo programa
            # Se for Tarefa
            "HEADER_INFO": {
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
                    "num_de_redaoes": "", # Número total de redações
                    "num_de_user_resposta": "", # Número total de vezes que o usuário respondeu sem o programa
                    "num_de_erros": "", # Número total de erros
                    "ERROR_TYPES": {}, # Tipos de Erros
                    "QUESTIONS_TYPES": { # Número de quantas vezes cada tipo de questão apareceu
                        "card-img":"",
                        "card-gif": "",
                        "card-video": "",
                        "Text": "",
                    }
                },
                "TEXTOS": {
                    "num_text": "", # Número gerado automaticamente pelo programa para diferenciar os textos
                },
                "QUESTIONS": {
                    "numero_da_questao": {
                        # Se o tipo for Radios
                        "tipo": "Radios",
                        "titulo": "",
                        "ia": "", # Ia que foi usada
                        "resposta": "", # Redacao
                        "user_resposta": "", # Se o usuário teve que responder ele irá contar
                        "tempo_gasto": "", # Tempo cronometrado pelo programa para colocar a resposta
                        "erro": "" # Algum erro na hora de responder alguma pergunta
                    },
                }
            }
        }
    }
'''