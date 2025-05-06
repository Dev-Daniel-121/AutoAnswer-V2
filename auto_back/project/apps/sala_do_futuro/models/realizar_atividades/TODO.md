<style>
    .classification {
        font-weight: bold;
        border-radius: 5em;
        padding: .25em 2em;
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
    }
    
    .a {
        color: rgb(255, 255, 255);
        background-color: rgba(255, 0, 0, 0.517);
    }

    .b {
        color: rgb(0, 0, 0);
        background-color: rgba(255, 177, 0, 0.89);
    }

    .obj {
        float: right;
    }

    .task_and_projects {
        font-weight: bold;
        padding: .25em 1em;
        display: inline-flex;
        align-items: center;
        justify-content: start;
        text-wrap: nowrap;
    }

    .title {
        font-weight: bold;
        padding: .2em 1em;
        border-radius: 5em;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }
    
    .project_title {
        color: rgb(255, 255, 255);
        background-color: rgba(0, 170, 17, 0.47);
    }

    .project {
        color: rgb(21, 255, 0);
        background-color: rgba(0, 170, 17, 0.3);
        padding: .25em 1em;
        border-radius: 5em;
    }

    .bloco_icon {
        width: 1.3em;
        height: 1.3em;
        background-color: rgb(255, 255, 255);
        border-radius: 50%;
        margin: 0 1em 0 0;
    }

    .bloco {
        font-weight: bold;
        border-radius: 5em;
        padding: .25em 2em;
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        text-wrap: nowrap;
    }

    .b1 {
        color: rgb(230, 0, 255);
        background-color: rgba(102, 0, 255, 0.3);
    }

    .b1_icon {
        background-color: rgb(230, 0, 255);
    }

    .status {
        /* width: 1.7em; */
        padding: .1em 1.7em;
        height: 1.7em;
        color: rgb(0, 0, 0);
        background-color: rgb(255, 255, 255);
        border-radius: 5em;
        font-weight: bold;
        margin: auto;
    }

    .done {
        color: rgb(0, 255, 13);
        background-color: rgba(0, 255, 13, 0.26);
    }

    .waiting {
        color: rgb(255, 140, 0);
        background-color: rgba(255, 140, 0, 0.24);
    }

    .doing {
        color: rgb(0, 217, 255);
        background-color: rgba(0, 110, 255, 0.36);
    }

    .stoped {
        color: rgb(247, 0, 255);
        background-color: rgba(106, 0, 255, 0.34);
    }

    .deleted {
        color: rgba(255, 255, 255, 0.43);
        background-color: rgba(0, 0, 0, 0.34);
    }

    .error {
        color: rgb(255, 0, 0);
        background-color: rgba(255, 0, 0, 0.17);
    }
    .progress {
        width: 100%;
        height: 2.5em;
        display: flex;
        align-items: center;
        margin: 2em 0 0 0;
        border-radius: 5em;
        padding: .25em;
        overflow: hidden;
        background-color: rgb(255, 255, 255);
    }

    .porcent {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: end;
        overflow: hidden;
        width: 10%;
        padding: 0 1em 0 0;
        border-radius: 5em;
        color: rgb(255, 255, 255);
        font-weight: bold;
        background-color: rgb(0, 0, 0);
    }

    .bad {
        background-color: rgb(81, 2, 2);
    }

    .bad .porcent {
        color: rgb(255, 0, 0);
        background-color: rgb(44, 0, 0);
    }

    .half {
        background-color: rgb(81, 46, 2);
    }

    .half .porcent {
        color: rgb(255, 145, 0);
        background-color: rgb(44, 21, 0);
    }

    .good {
        background-color: rgb(2, 35, 81);
    }

    .good .porcent {
        color: rgb(0, 187, 255);
        background-color: rgb(0, 10, 44);
    }

    .excelent {
        background-color: rgb(3, 81, 2);
    }

    .excelent .porcent {
        color: rgb(0, 255, 21);
        background-color: rgb(0, 44, 4);
    }

    .progress_porcent {
        width: 10em;
        padding: .5em;
        border-radius: 5em;
        overflow: hidden;
    }

    .progress_porcent {
        width: 10em;
        padding: .5em;
        border-radius: 5em;
        overflow: hidden;
        display: flex;
        align-items: center;
    }
</style>

# Entrar nas tarefas

|              Importância               | Tarefas                         | Duração 15min |               Status                |                                             Porcent                                             |
| :------------------------------------: | :------------------------------ | :-----------: | :---------------------------------: | :---------------------------------------------------------------------------------------------: |
| <div class="classification a">A1</div> | Planejar como irá ser feito     |     2 min     | <div class="status done">Done</div> | <div class="progress_porcent excelent"><div class="porcent" style="width: 100%">100</div></div> |
| <div class="classification a">A2</div> | Entrar em 1 array de componente |    10 min     | <div class="status done">Done</div> | <div class="progress_porcent excelent"><div class="porcent" style="width: 100%">100</div></div> |
| <div class="classification a">A3</div> | Entrar em todos o componentes   |    10 min     | <div class="status done">Done</div> | <div class="progress_porcent excelent"><div class="porcent" style="width: 100%">100</div></div> |
| <div class="classification a">A4</div> | Entrar em 1 array de tarefas    |    10 min     | <div class="status done">Done</div> | <div class="progress_porcent excelent"><div class="porcent" style="width: 100%">100</div></div> |
| <div class="classification a">A5</div> | Fazer todas as tarefas          |     3 min     | <div class="status done">Done</div> | <div class="progress_porcent excelent"><div class="porcent" style="width: 100%">100</div></div> |


<div class="progress excelent"><div class="porcent" style="width: 100%">100</div></div>

<br>

# Classificação e Númeração

|              Importância               | Tarefas                                                                                                 | Duração |                Status                 |                                             Porcent                                             |
| :------------------------------------: | :------------------------------------------------------------------------------------------------------ | :-----: | :-----------------------------------: | :---------------------------------------------------------------------------------------------: |
| <div class="classification a">A1</div> | Varrer a lição                                                                                          | 20 min  | <div class="status doing">Done</div>  | <div class="progress_porcent excelent"><div class="porcent" style="width: 100%">100</div></div> |
| <div class="classification a">A2</div> | Classificar como TXT, IMG, Mp4 ou Quest                                                                 | 20 min  | <div class="status doing">Doing</div> |    <div class="progress_porcent bad"><div class="porcent" style="width: 25%">25</div></div>     |
| <div class="classification a">A3</div> | Númerar e classifcar as quest como Radios, Checkbox, Textarea, Dragable, Order, Select ou Select Order. | 20 min  | <div class="status doing">Doing</div> |     <div class="progress_porcent bad"><div class="porcent" style="width: 0%">0</div></div>      |

<div class="progress half"><div class="porcent" style="width: 50%">50</div></div>

<br>

# Pegar infos da quest

|              Importância               | Tarefas                              | Duração |                  Status                   |                                        Porcent                                         |
| :------------------------------------: | :----------------------------------- | :-----: | :---------------------------------------: | :------------------------------------------------------------------------------------: |
| <div class="classification a">A1</div> | Pegar Título da quest                | 50 min  | <div class="status waiting">Waiting</div> | <div class="progress_porcent bad"><div class="porcent" style="width: 0%">0</div></div> |
| <div class="classification a">A2</div> | Pegar alters da quest                | 50 min  | <div class="status waiting">Waiting</div> | <div class="progress_porcent bad"><div class="porcent" style="width: 0%">0</div></div> |
| <div class="classification a">A3</div> | Salvar em 1 .JSON para data_quest    | 50 min  | <div class="status waiting">Waiting</div> | <div class="progress_porcent bad"><div class="porcent" style="width: 0%">0</div></div> |
| <div class="classification a">A3</div> | Criar 1 .JSON para data_quest_answer | 50 min  | <div class="status waiting">Waiting</div> | <div class="progress_porcent bad"><div class="porcent" style="width: 0%">0</div></div> |

<div class="progress bad"><div class="porcent" style="width: 0%">0</div></div>

<br>

# Responder quest

|              Importância               | Tarefas                             | Duração |                  Status                   |                                        Porcent                                         |
| :------------------------------------: | :---------------------------------- | :-----: | :---------------------------------------: | :------------------------------------------------------------------------------------: |
| <div class="classification a">A1</div> | Criar sys. answer para cada quest   | 50 min  | <div class="status waiting">Waiting</div> | <div class="progress_porcent bad"><div class="porcent" style="width: 0%">0</div></div> |
| <div class="classification a">A2</div> | Pegar os dados do data_quest_answer | 50 min  | <div class="status waiting">Waiting</div> | <div class="progress_porcent bad"><div class="porcent" style="width: 0%">0</div></div> |
| <div class="classification a">A3</div> | Validar answer com cada quest       | 50 min  | <div class="status waiting">Waiting</div> | <div class="progress_porcent bad"><div class="porcent" style="width: 0%">0</div></div> |
| <div class="classification a">A4</div> | Responder cada quest                | 50 min  | <div class="status waiting">Waiting</div> | <div class="progress_porcent bad"><div class="porcent" style="width: 0%">0</div></div> |

<div class="progress bad"><div class="porcent" style="width: 0%">0</div></div>

<br><br><br>

| O que está sendo feito                                                  | Tempo Inicio | Tempo Fim | Tempo Total |
| :---------------------------------------------------------------------- | :----------: | :-------: | :---------: |
| Planejando Armazenamento dos Dados Obtidos                              |    09:49     |   10:14   |    25min    |
| Planejando Coletando Informações dos texto Informativos                 |    10:35     |   11:00   |    25min    |
| Coletando Informações dos texto Informativos                            |    11:05     |   11:17   |    12min    |
| Transformando função de coleta de Seção em Class                        |    11:18     |   11:42   |    24min    |
| Resolvendo Bugs da CollectSection                                       |    12:23     |   12:31   |    8min     |
| Alterado class Activity Score e Collect Section                         |    12:34     |   12:36   |    2min     |
| Coletando Informações dos texto Informativos                            |    12:34     |   12:59   |    25min    |
| Atualizando a Classe Text                                               |    13:17     |   13:24   |    7min     |
| Adicionando as Seções Corretas na Class Text                            |    13:28     |   13:35   |    7min     |
| Planejando JSON para Receber dados de Outras Midías (Img, Youtube, etc) |    13:37     |   13:39   |    2min     |
| Planejando Código para Coletar Img, Legendas do Youtube, etc            |    13:39     |   13:41   |    3min     |
| Veficação antes de Coletar as Sections                                  |    16:50     |   16:52   |    2min     |
| Veficação antes de Coletar Pontução e Pontos Obtidos da Atividade       |    16:53     |   17:07   |    14min    |
| Procura de uma Biblioteca para Pegar Transcrição do YT Vídeo            |    17:09     |   17:19   |    10min    |
| Procura de uma Biblioteca para Pegar Transcrição do YT Vídeo            |    17:47     |   17:49   |    2min     |
|                                                                         |              |           |             |
| Aramazenar dados no JSON                                                |    14:37     |           |             |
| Passar dados para answer JSON                                           |    17:22     |           |             |
|                                                                         |              |           |             |

<!--


--- Pomodoro 1

09:49 - 10:34
CCB:JARDIM YARA-ISAQUE MARQUIZETE ANCIÃO PREGOU SEM MEDO-O AVISO FOI DADO-27/04/2025-SE PREPARE

09:49 - 10:14
Planejando passos

--- 25min


--- Pomodoro 2

10:35 - 11:07
CCB-JARDIM TRANSILVANIA IMPERDIVEL DEUS DÁ O ULTIMOAVISO A TERRA!SE PREPARE POVO DE DEUS!!

10:35 - 11:00
Planejado Coletando Informações dos texto Informativos

--- 25min


--- Pomodoro 3

11:08 - 11:25
CCB- TONINHO DO PINHAL -CAMPINAS ESTREMECEU NESTE CULTO!!NÃO TEVE QUE NÃO CHORASSE!DEUS PURO

11:05 - 11:17
Coletando Informações dos texto Informativos

11:26 - 11:41
CCB- TESTEMUNHO VIRALIZOU ANCIÃO DE SANTA CATARINA -O MENINO QUE NÃO QUERIA RECITAR!LINDO!!

--- 30min


--- Pomodoro 4

12:23 - 12:49
CCB-VILA BUENO AIRES EM FESTA -ULTIMO CULTO DEUS FALA ASIM COM A IRMANDADE!!FORTISSIMO!

12:23 - 12:48
Consertando Bugs da Class CollectSection

--- 25min


--- Pomodoro 5

13:17 - 13:53
CCB-CULTO DA LAPA SP - DEUS MANDA UM AVISO A IGREJA!!MUITO FORTE ISSO!! SANTO DEUS

--- 25min


--- Pomodoro 6

14:53 - 15:00
Analise do que estamos fazendo e do que foi feito

--- 7min


-->

<!--

| Cronometrar e verificar tempo gasto na atividade |    12:15     |   12:30   |     15min     |
| Coletar informações da Lição                     |    14:25     |   14:50   |     25min     |
| Coletar inforamções das Questões                 |    17:57     |   18:21   |     25min     |
| melhorado códiog task_info (self)                |    18:00     |   18:09   |     9min      |
| Teste das altearções                             |    18:09     |   18:16   |     7min      |
| Criar JSON para receber resposta                 |              |           |               |
| Colocar na área de Transferencia do Usuário      |              |           |               |
| Esperar respostas                                |              |           |               |
| Respondendo a Lição                              |              |           | 30min + 15min |
| Esperar 1min pela resposta                       |              |           |               |

-->

<br><br><br>

---

<br><br><br>

# EXTRA

- Salvar algumas informações para Analise de Desenpenho

<br><br>

## JSON - TAREFAS

<!-- {
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
                    "dificuldade": "", # 1- Fácil, 2- Média, 3- Difícil
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
} -->

## JSON - REDAÇÃO

<!-- {
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
} -->

## JSON - PROVAS

<!-- {
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
} -->
