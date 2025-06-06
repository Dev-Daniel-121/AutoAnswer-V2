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

| O que está sendo feito                                                                   |    Dia     | Tempo Inicio | Tempo Fim | Tempo Total |
| :--------------------------------------------------------------------------------------- | :--------: | :----------: | :-------: | :---------: |
| Autoanswer (Preparando e planejando passos para hoje)                                    | 06/06/2025 |    12:34     |   12:45   |             |
|                                                                                          | 06/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                      | 06/06/2025 |              |           |             |
| Autoanswer (Commitando código)                                                           | 06/06/2025 |    13:17     |   13:17   |             |
| Autoanswer (Commitando código)                                                           | 06/06/2025 |    13:21     |   13:24   |             |
| Autoanswer (Configurando as contas)                                                      | 06/06/2025 |    13:24     |   13:27   |             |
| Autoanswer (Criando repositório)                                                         | 06/06/2025 |    13:35     |   13:37   |             |
| Autoanswer (Dar git pull no repositório)                                                 | 06/06/2025 |    13:37     |   13:   |             |
| Autoanswer (Pausa)                                                                       | 06/06/2025 |              |           |             |
|                                                                                          | 06/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                      | 06/06/2025 |              |           |             |
| Autoanswer (Adicionar mais informações aos prompts)                                      | 06/06/2025 |              |           |             |
| Autoanswer (Data e hora de criação ao prompt)                                            | 06/06/2025 |              |           |             |
| Autoanswer (Criar histório no prompt do JSON)                                            | 06/06/2025 |              |           |             |
| Autoanswer (Adicionar datas, horários, matéria e id da matéria ao histórico do prompt)   | 06/06/2025 |              |           |             |
| Autoanswer (Exibir os prompt mais usados e com as melhores métricas)                     | 06/06/2025 |              |           |             |
| Autoanswer (Pausa)                                                                       | 06/06/2025 |              |           |             |
|                                                                                          | 06/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 40/45min                                                      | 06/06/2025 |              |           |             |
| Autoanswer (Answer - Melhorar desing do Settings)                                        | 06/06/2025 |              |           |             |
| Autoanswer (Answer - Melhorar o Settings)                                                | 06/06/2025 |              |           |             |
| Autoanswer (Answer - Criando Automação para Coletar Resposta (CollectAutoGui - Search))  | 06/06/2025 |              |           |             |
| Autoanswer (Pausa)                                                                       | 06/06/2025 |              |           |             |
|                                                                                          | 06/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                      | 06/06/2025 |              |           |             |
| Autoanswer (Criar validação para cada tipo de questão e resposta recebida para o tipo)   | 06/06/2025 |              |           |             |
| Autoanswer (Responder as questões)                                                       | 06/06/2025 |              |           |             |
| Autoanswer (Enviar ou Salvar como Rascunho a Atividade respostas)                        | 06/06/2025 |              |           |             |
| Autoanswer (Mostrar Resultado)                                                           | 06/06/2025 |              |           |             |
| Autoanswer (Pausa)                                                                       | 06/06/2025 |              |           |             |
|                                                                                          | 06/06/2025 |              |           |             |
| Autoanswer (Planejar Dashboard para Ánalise)                                             | 07/06/2025 |              |           |             |
| Autoanswer (Criar dashboard para Ánalise)                                                | 07/06/2025 |              |           |             |
| Autoanswer (Pausa)                                                                       | 07/06/2025 |              |           |             |
| Autoanswer (Planejar próximos passos para o Redação, Leia, Speak, Khanacademy, Expansão) | 07/06/2025 |              |           |             |
| Autoanswer (Pausa)                                                                       | 07/06/2025 |              |           |             |
|                                                                                          | 07/06/2025 |              |           |             |

<!--

Quase lá, está assim, vou explicar melhor como irá funcionar o design, atualizei o design

[1]. Title Prompt                   A: 27  C: 19  W: 8
Prompt for Grok

TENDENCIA:                        Mat: 67%    His: 33%
ANSWERS: 27      -  CORRECTS: 19      -  WRONGS: 8


O design terá o width de 52 caracteres e irá exibr até 99 prompts, terão o width de 52 caracteres para pegar 100% do width do design


Explicando o design do prompt 

HEADER
   Aqui termos 2 tipos de informações e no meio espaço, dados do prompt (ID e Título) e dados gerais (A - Answers, C - Corrects, W - Wrongs), o espaço tem que ter no minimo 3 espaço (   )

   Os "dados do prompt" irão ficar a esquerda e terão no máximo 32 caracteres (essa será o tamanho máximo: "[100]. NOME DO PROMPT MUITO L..."), se ultrapassar 32 caracteres iremos exibir 29 caracteres e iremos adicinar "..." para dar os 32 caracteres

   Tem que ter no minimo 3 espaços para o user ver e saber o que é título e o que são dados gerais do prompt

   Os "dados gerais" irão ficar a direita e para cada item (A, C e W) terá no máximo o valor de 99999999 se for maior iremos colocar +9999999

   Uma outra coisa, se os "dados gerais" tiver mais caracateres, digo ter uma quantidade de caracteres que somando o total de caracteres header do prompt for maior que o limite que é width 52 caracteres iremos remover alguns caracteres do "dados do prompt" para compensar, não se esqueça o "espaço" será flexivel pois ele irá espçar e deixar os "dados do prompt" a esquerda e os "dados gerais" a direita, porém ela terá um limite de no minimo 3 espaços (   )

BODY
   Aqui teremos o prompt em si

   O prompt terá os mesmo width 100% (52 caracteres por linha) para cada prompt iremos exibir no máximo 208 caracteres se for maior iremos exibir 205 caracteres e iremos colocar "..." para dar os 208, para não ficar tudo em uma linha iremos contar 51 caracteres pular uma linha e colocar "-" para ficar mais bonito e mostrar para o user que pulou a linha, iremos fazer isso até terminar os 208 caracteres

FOOTER
   Aqui teremos os dados de "TENDENCIA" do prompt que irá exbir no máximo 3 matérias que ele teve mais acerto, aqui será em porcentagens ou seja o máximo é 100%, iremos ter espaço para dividir, "TENDENCIA:" irá ficar a esquerda "dados de tendencias" irá ficar a direita, o espaço será flexivel, ou seja a linha tem que ter no máximo 52 caractres no total se for a mais iremos diminuir o espaço, para cada matéria iremos exibir os primeiro 4 caracteres

Exemplo

[1]. NOME D...   A: +9999999 C: +9999999 W: +9999999
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlklj-
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
asdf gasdgasdf ashasdçlk jasçkldf asçdlkfjaçlsdka...

TENDENCIA:            Mate: 50%  Hist 45%  Mult: 20%

[2]. NOME DO PROMPT +LONG...       A: -- C: -- W: --
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlklj-
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
asdf gasdgasdf ashasdçlk jasçkldf asçdlkfjaçlsdka...

TENDENCIA:           ----: --%  ----: --%  ----: --%
ANSWERS: 00.0  -   CORRECTS: 00.0   -   WRONGS: 00.0

[3]. NOME DO PROMPT               A: 100 C: 70 W: 30
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlklj-
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
asdf gasdgasdf ashasdçlk jasçkldf asçdlkfjaçlsdka...

TENDENCIA:                Qui: 10%  Bio: 4%  Red: 1%
ANSWERS: 100    -    CORRECTS: 70    -    WRONGS: 30

[30]. NOME DO PROMPT +LON...       A: -- C: -- W: --
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlklj-
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
asdf gasdgasdf ashasdçlk jasçkldf asçdlkfjaçlsdka...

TENDENCIA:           ----: --%  ----: --%  ----: --%
ANSWERS: 00.0  -   CORRECTS: 00.0   -   WRONGS: 00.0


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
