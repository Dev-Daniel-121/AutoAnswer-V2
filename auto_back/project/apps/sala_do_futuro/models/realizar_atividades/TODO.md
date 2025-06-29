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

| O que está sendo feito                                                                    |    Dia     | Tempo Inicio | Tempo Fim | Tempo Total |
| :---------------------------------------------------------------------------------------- | :--------: | :----------: | :-------: | :---------: |
| Autoanswer (Preparando e planejando passos para hoje)                                     | 06/06/2025 |    12:34     |   12:45   |             |
|                                                                                           | 06/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                       | 06/06/2025 |              |           |             |
| Autoanswer (Commitando código)                                                            | 06/06/2025 |    13:17     |   13:17   |             |
| Autoanswer (Commitando código)                                                            | 06/06/2025 |    13:21     |   13:24   |             |
| Autoanswer (Configurando as contas)                                                       | 06/06/2025 |    13:24     |   13:27   |             |
| Autoanswer (Criando repositório)                                                          | 06/06/2025 |    13:35     |   13:37   |             |
| Autoanswer (Dar git pull no repositório)                                                  | 06/06/2025 |    13:37     |   13:53   |             |
| Autoanswer (Pausa)                                                                        | 06/06/2025 |    13:53     |   14:03   |             |
|                                                                                           | 06/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                       | 06/06/2025 |              |           |             |
| Autoanswer (Adicionar mais informações aos prompts)                                       | 06/06/2025 |    16:42     |   17:01   |             |
| Autoanswer (Data e hora de criação ao prompt)                                             | 06/06/2025 |    17:01     |   17:03   |             |
| Autoanswer (Criar histório no prompt do JSON)                                             | 06/06/2025 |    17:03     |   17:04   |             |
| Autoanswer (Adicionar datas, horários, matéria e id da matéria ao histórico do prompt)    | 06/06/2025 |    17:04     |   17:07   |             |
| Autoanswer (Melhorando Json dos prompts)                                                  | 06/06/2025 |    17:07     |   17:10   |             |
| Autoanswer (Exibir os prompt mais usados e com as melhores métricas)                      | 06/06/2025 |    17:10     |   17:15   |             |
| Autoanswer (Criando status para os prompts)                                               | 06/06/2025 |    17:15     |   17:25   |             |
| Autoanswer (Criar arquivo .md para guardar os status)                                     | 06/06/2025 |    17:25     |   17:27   |             |
| Autoanswer (Exibir os prompts com o status)                                               | 06/06/2025 |    17:27     |   17:47   |             |
| Autoanswer (Criar histórico no JSON para os prompts)                                      | 06/06/2025 |    17:47     |   17:53   |             |
| Autoanswer (Atualizar código para poder receber o history)                                | 06/06/2025 |    17:53     |   18:07   |             |
| Autoanswer (Pausa)                                                                        | 06/06/2025 |    18:07     |   18:17   |             |
| Autoanswer (Answer - Planejando passos para criar a Automação)                            | 06/06/2025 |    23:10     |   23:51   |             |
|                                                                                           | 06/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 40/45min                                                       | 06/06/2025 |              |           |             |
| Autoanswer (Answer - Criando Automação para Coletar Resposta (CollectAutoGui - Search))   | 06/06/2025 |    23:51     |   00:45   |             |
| Autoanswer (Answer - Exibir circulos)                                                     | 06/06/2025 |    23:51     |   00:45   |             |
|                                                                                           | 06/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 07/06/2025 |              |           |             |
| Tempo no bloco: de 30min à 50/55min                                                       | 07/06/2025 |              |           |             |
| Autoanswer (Answer - Criando Automação para Coletar Resposta (CollectAutoGui - Search))   | 07/06/2025 |    13:00     |   14:31   |             |
| Autoanswer (Answer - Exibir circulos)                                                     | 07/06/2025 |    13:00     |   14:31   |             |
|                                                                                           | 07/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                       | 07/06/2025 |              |           |             |
| Autoanswer (Criar validação para cada tipo de questão e resposta recebida para o tipo)    | 07/06/2025 |    13:41     |   14:31   |             |
| Autoanswer (Planejar Responder as questões)                                               | 07/06/2025 |    14:31     |   15:10   |             |
| Autoanswer (Atualizando estrutura do projeto)                                             | 07/06/2025 |    00:15     |   00:28   |             |
| Autoanswer (Responder as questões)                                                        | 07/06/2025 |    00:28     |   00:33   |             |
|                                                                                           | 07/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 08/06/2025 |              |           |             |
| Tempo no bloco: de 35min à 50/55min                                                       | 08/06/2025 |              |           |             |
| Autoanswer (Melhorando Planejamento Responder as questões)                                | 08/06/2025 |    21:18     |   21:30   |             |
|                                                                                           | 08/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 12/06/2025 |              |           |             |
| Tempo no bloco: de 35min à 50/55min                                                       | 12/06/2025 |              |           |             |
| Autoanswer (Alimentando a IA)                                                             | 12/06/2025 |    22:47     |   22:53   |             |
| Autoanswer (Alimentando a IA)                                                             | 12/06/2025 |    23:10     |   23:50   |             |
| Autoanswer (Gerenciar dados, Validar e Responder)                                         | 12/06/2025 |    23:51     |   00:07   |             |
| Autoanswer (Pausa)                                                                        | 12/06/2025 |    00:07     |   00:14   |             |
| Autoanswer (Planejando design Mostrar Resultado)                                          | 12/06/2025 |    01:00     |   01:55   |             |
|                                                                                           | 12/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 13/06/2025 |              |           |             |
| Tempo no bloco: de 35min à 50/55min                                                       | 13/06/2025 |              |           |             |
| Autoanswer (Planejando design Mostrar Resultado)                                          | 13/06/2025 |    10:31     |   10:47   |             |
| Autoanswer (Mostrar Resultado)                                                            | 13/06/2025 |    14:57     |   14:59   |             |
| Autoanswer (Mostrar Resultado (Planejar Respostas Corretas))                              | 13/06/2025 |    21:47     |   22:12   |             |
| Autoanswer (Mostrar Resultado (Planejamento))                                             | 13/06/2025 |    22:17     |   22:34   |             |
| Autoanswer (Mostrar Resultado (Atualizando JSON))                                         | 13/06/2025 |    00:32     |   00:34   |             |
|                                                                                           | 13/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 15/06/2025 |              |           |             |
| Tempo no bloco: de 35min à 50/55min                                                       | 15/06/2025 |              |           |             |
| Autoanswer (Mostrar Resultado (Planejamento))                                             | 15/06/2025 |    16:09     |   16:14   |             |
| Autoanswer (Mostrar Resultado (Atualizando JSON))                                         | 15/06/2025 |    16:14     |   16:20   |             |
| Autoanswer (Mostrar Resultado (Atualizando JSON))                                         | 15/06/2025 |    16:14     |   16:20   |             |
| Autoanswer (Planejando próximos passos)                                                   | 15/06/2025 |    16:20     |   16:47   |             |
| Autoanswer (Pausa)                                                                        | 15/06/2025 |    16:47     |   17:19   |             |
| Autoanswer (Mostrar Resultado (Criando CollectResult))                                    | 15/06/2025 |    21:57     |   23:12   |             |
| Autoanswer (Mostrar Resultado (Melhorando CollectResult))                                 | 15/06/2025 |    23:24     |   23:52   |             |
| Autoanswer (Mostrar Resultado (Criando método Show para CollectResult))                   | 15/06/2025 |    23:52     |   23:57   |             |
|                                                                                           | 15/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 16/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                       | 16/06/2025 |              |           |             |
| Autoanswer (Mostrar Resultado (Validar por melhor forma))                                 | 16/06/2025 |    23:19     |   23:24   |             |
| Autoanswer (Mostrar Resultado (Criando método Show para CollectResult))                   | 16/06/2025 |    23:24     |   00:45   |             |
| Autoanswer (Mostrar Resultado (Melhorar o Espaçamento (coluna) do _print_group - Lógica)) | 16/06/2025 |    01:17     |   01:27   |             |
|                                                                                           | 16/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 17/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                       | 17/06/2025 |              |           |             |
| Autoanswer (Mostrar Resultado (Melhorar o Espaçamento (coluna) do _print_group - Código)) | 17/06/2025 |    12:07     |   12:37   |             |
| Autoanswer (Pausa)                                                                        | 17/06/2025 |    12:37     |   12:47   |             |
| Autoanswer (Configurando INIT Mostrar Resultado)                                          | 17/06/2025 |    12:47     |   12:57   |             |
| Autoanswer (Enviar ou Salvar como Rascunho a Atividade (Planejamento))                    | 17/06/2025 |    12:57     |   13:19   |             |
|                                                                                           | 17/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 18/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                       | 18/06/2025 |              |           |             |
| Autoanswer (Enviar ou Salvar como Rascunho a Atividade (Código))                          | 18/06/2025 |    22:01     |   23:09   |             |
| Autoanswer (Enviar atividade SdF)                                                         | 18/06/2025 |    22:01     |   23:09   |             |
| Autoanswer (Enviar ou Salvar como Rascunho a Atividade (Código))                          | 18/06/2025 |    23:57     |           |             |
|                                                                                           | 18/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 19/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                       | 19/06/2025 |              |           |             |
| Autoanswer (Enviar ou Salvar como Rascunho a Atividade (Passando dados para o Answer))    | 19/06/2025 |    13:00     |   13:15   |             |
| Autoanswer (Instalando Fira Code)                                                         | 19/06/2025 |    13:15     |   13:29   |             |
| Autoanswer (Enviar ou Salvar como Rascunho a Atividade (Passando dados para o Answer))    | 19/06/2025 |    13:30     |   14:00   |             |
| Autoanswer (Pausa)                                                                        | 19/06/2025 |    14:00     |   14:08   |             |
| Autoanswer (Enviar ou Salvar como Rascunho a Atividade (Passando dados para o Answer))    | 19/06/2025 |    14:10     |   14:17   |             |
| Autoanswer (Mostrar Resultado (Mostrar questões anuladas - DESCARTADO))                   | 19/06/2025 |    14:17     |   14:25   |             |
| Autoanswer (Pausa)                                                                        | 19/06/2025 |    14:25     |   14:47   |             |
| Autoanswer (Answer - Melhorar desing do Settings (Planejamento e atualização do design))  | 19/06/2025 |    15:03     |   15:07   |             |
|                                                                                           | 19/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 20/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                       | 20/06/2025 |              |           |             |
| Autoanswer (Answer - Melhorar desing do Settings (Planejamento e atualização do design))  | 20/06/2025 |    19:28     |   19:37   |             |
| Autoanswer (Answer - Melhorar desing do Settings (Planejamento e atualização do design))  | 20/06/2025 |    19:50     |   20:30   |             |
| Autoanswer (Pausa)                                                                        | 20/06/2025 |    20:30     |   20:50   |             |
| Autoanswer (Answer - Melhorar desing do Settings (Planejamento e atualização do design))  | 20/06/2025 |    20:50     |   21:20   |             |
| Autoanswer (Pausa)                                                                        | 20/06/2025 |    21:20     |   21:30   |             |
| Autoanswer (Commitando código)                                                            | 20/06/2025 |    23:27     |   23:42   |             |
|                                                                                           | 20/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 26/06/2025 |              |           |             |
| Tempo no bloco: de 30min à 40/45min                                                       | 26/06/2025 |              |           |             |
| Autoanswer (Answer - Melhorar desing do Settings (Planejamento e atualização do design))  | 26/06/2025 |    20:50     |   21:20   |             |
| Autoanswer (Answer - Planejamento do Answer)                                              | 26/06/2025 |    19:07     |   22:07   |             |
|                                                                                           | 26/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 27/06/2025 |              |           |             |
| Tempo no bloco: de 30min à 40/45min                                                       | 27/06/2025 |              |           |             |
| Autoanswer (Answer - Melhorar desing do Settings (Planejamento e atualização do design))  | 27/06/2025 |    20:50     |   21:20   |             |
| Autoanswer (Answer - Planejamento do Answer)                                              | 27/06/2025 |    19:07     |   22:07   |             |
|                                                                                           | 27/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 28/06/2025 |              |           |             |
| Tempo no bloco: de 30min à 40/45min                                                       | 28/06/2025 |              |           |             |
| Autoanswer (Answer - Melhorar desing do Settings (Planejamento e atualização do design))  | 28/06/2025 |    20:50     |   21:20   |             |
| Autoanswer (Answer - Planejamento do Answer)                                              | 28/06/2025 |    19:07     |   22:07   |             |
|                                                                                           | 28/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 29/06/2025 |              |           |             |
| Tempo no bloco: de 30min à 40/45min                                                       | 29/06/2025 |              |           |             |
| Autoanswer (Planejando próximos dias e Organizando dias anteriores)                       | 29/06/2025 |    00:27     |   00:43   |             |
| Autoanswer (Answer - Terminando Planejamento)                                             | 29/06/2025 |    01:17     |   01:37   |             |
| Autoanswer (Answer - Terminando Planejamento)                                             | 29/06/2025 |    01:50     |   01:55   |             |
| Autoanswer (Answer - Planejando Pastas e Arquivos necessários)                            | 29/06/2025 |    01:55     |   01:57   |             |
| Autoanswer (Commitando código)                                                            | 29/06/2025 |    01:57     |   02:05   |             |
|                                                                                           | 29/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------  | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 30/06/2025 |              |           |             |
| Tempo no bloco: de 30min à 40/45min                                                       | 30/06/2025 |              |           |             |
| Autoanswer (Answer - Criando Arquivos e Pastas do Planejamento)                           | 30/06/2025 |              |           |             |
| Autoanswer (Answer - Criando a Automação do Answer)                                       | 30/06/2025 |              |           |             |
| Autoanswer (Answer - Criando o Design do Settings)                                        | 30/06/2025 |              |           |             |
|                                                                                           | 30/06/2025 |              |           |             |
| Tempo no bloco: de 30min à 40/45min                                                       | 30/06/2025 |              |           |             |
| Autoanswer (Answer - Planejar criação do settings para prompts)                           | 30/06/2025 |              |           |             |
| Autoanswer (Answer - Criar settings para Prompts)                                         | 30/06/2025 |              |           |             |
|                                                                                           | 30/06/2025 |              |           |             |
| Tempo no bloco: de 30min à 40/45min                                                       | 30/06/2025 |              |           |             |
| Autoanswer (Melhorando o Gerenciar dados, Validar e Responder)                            | 30/06/2025 |              |           |             |
| Autoanswer (Descontinuar códigos e usar suas novas versões)                               | 30/06/2025 |              |           |             |
| Autoanswer (Pausa)                                                                        | 30/06/2025 |              |           |             |
|                                                                                           | 30/06/2025 |              |           |             |
| Tempo no bloco: de 35min à 40/45min                                                       | 30/06/2025 |              |           |             |
| Autoanswer (Planejar Dashboard para Ánalise)                                              | 30/06/2025 |              |           |             |
| Autoanswer (Criar dashboard para Ánalise)                                                 | 30/06/2025 |              |           |             |
| Autoanswer (Pausa)                                                                        | 30/06/2025 |              |           |             |
| Autoanswer (Planejar próximos passos para o Redação, Leia, Expansão, Khanacademy, Speak)  | 30/06/2025 |              |           |             |
| Autoanswer (Pausa)                                                                        | 30/06/2025 |              |           |             |
|                                                                                           | 30/06/2025 |              |           |             |
| ----------------------------------------------------------------------------------------- | ---------- | ------------ | --------- | ----------- |
|                                                                                           | 01/06/2025 |              |           |             |
| Tempo no bloco: de 25min à 30/35min                                                       | 01/06/2025 |              |           |             |
| Autoanswer (Pausa)                                                                        | 01/06/2025 |              |           |             |
| Autoanswer (Melhorando validação de Login)                                                | 01/06/2025 |              |           |             |
| Autoanswer (Exibindo mais dados (Página inicial))                                         | 01/06/2025 |              |           |             |
| Autoanswer (Consertando problema com card abertos)                                        | 01/06/2025 |              |           |             |
| Autoanswer (Pausa)                                                                        | 01/06/2025 |              |           |             |
| Autoanswer (Melhorando sistema de login para caso não entrar)                             | 01/06/2025 |              |           |             |
| Autoanswer (Melhorando sistema de realizar atividade para caso não processar os dados)    | 01/06/2025 |              |           |             |
|                                                                                           | 01/06/2025 |              |           |             |

<!--

| Autoanswer (Answer - Planejamento do Answer Criação, Exclusão e Validação de Msg Recebidas de contas temporárias, Validação para passagem de medias para IA, Login para Gmail, Reportagem de Problemas, Login e Logout das Ia, Validação de páginas funcionando, Teste de Internet Wifi, Etapas para quando página não estiver repondendo/funcionando, etc)  | 27/06/2025 |    19:07     |   22:07   |             |
| Autoanswer (Answer - Planejamento do Answer Criação, Exclusão e Validação de Msg Recebidas de contas temporárias, Validação para passagem de medias para IA, Login para Gmail, Reportagem de Problemas, Login e Logout das Ia, Validação de páginas funcionando, Teste de Internet Wifi, Etapas para quando página não estiver repondendo/funcionando, etc)  | 28/06/2025 |    19:07     |   22:07   |             |
| Autoanswer (Answer - Planejamento do Answer Criação, Exclusão e Validação de Msg Recebidas de contas temporárias, Validação para passagem de medias para IA, Login para Gmail, Reportagem de Problemas, Login e Logout das Ia, Validação de páginas funcionando, Teste de Internet Wifi, Etapas para quando página não estiver repondendo/funcionando, etc)  | 29/06/2025 |    19:07     |   22:07   |             |

-->

<!--

Estava conversando com outro Chat, sobre a melhor maneira de gerenciar algumas informações que o código irá receber, esse é o workflow


1. Class CollectQuest, irá coletar as informação da prova (Questões, etc) e para cada questão irá identificar o tipo e charmará o Extractor para coleta de informações da questão.
1.1. Com todas as questões coletadas irá criar um JSON

1. Class Answer, com base nos dados do JSON (questões) irá ir até uma IA para coletar as respostas (PyAutoGUI)
2.1. Irá atualizar o JSON agora com as repostas obtidas

1. Class AnswerFlowManager, irá gerenciar o Flow dos dados, iremos usar uma factory aqui que para as questões, ela irá chamar o service certo para o tipo da questão
3.1 Sevice irá receber os dados da questão e irá chamar o Validador da Questão e se tiver correto irá dar True se não irá dar False e irá mostrar o Erro
3.2 Depois de validar o Service irá chamar o answer da questão para responder a questão no site.

Note: No "3. " no caso estava conversando com o outro chat sobre uma forma boa, sem que necessite de ficar if, elif, etc ele me deu a alternativa de usar um factory

Esse é um exemplo de JSON

JSON

{
    "tarefas": {
        "71051809": {
            "ia": {
                "ia": "Grok 3 - Smartest",
                "prompt": "\n                ### Instruções\n                Você receberá algumas questões em formato de um JSON (dicionário Python). Seu trabalho é processar cada questão e retornar as respostas no mesmo formato JSON especificado abaixo. Algumas questões podem incluir imagens anexadas, outras podem não ter alternativas, e há casos em que a 'questão' pode ser apenas uma imagem, sem texto. Analise cada caso e preencha o JSON de acordo com as regras fornecidas. Todas as respostas devem ser em português.\n\n                ### Formato JSON Esperado\n                {\n                '0': {\n                    'type': 'TIPO DA QUESTÃO',\n                    'alternatives': {\n                        'media': {DADOS DE MÍDIA DA QUESTÃO},\n                        'alternative': ['ALTERNATIVAS']\n                    },\n                    'answer': 'RESPOSTA PARA TAREFA'\n                }\n                }\n\n                ### Regras para Preenchimento\n                - Índice: Cada questão será representada por um número sequencial começando de 0 (ex.: '0', '1', etc.).\n                - Campo `type`:\n                - Identifique o tipo da questão (ex.: 'Múltipla Escolha', 'Resposta Curta', etc.).\n                - Se o tipo não puder ser determinado (como uma imagem sem contexto), defina `type` como uma string vazia (`''`).\n                - Campo `alternatives`:\n                - Se houver alternativas, inclua um objeto `alternatives` com:\n                    - `media`: Dados da mídia, como `{ 'type': 'image', 'url': '[link ou descrição]' }` se houver imagem, ou `null` se não houver.\n                    - `alternative`: Lista de alternativas (ex.: `['A) Opção 1', 'B) Opção 2']`).\n                - Se não houver alternativas, defina `alternatives` como `null`.\n                - Campo `answer`:\n                - Para questões com alternativas, forneça a resposta correta (ex.: 'A)', 'B)', etc.).\n                - Para questões sem alternativas, forneça uma resposta curta ou descritiva adequada.\n                - Para questões que são apenas imagens, analise a imagem e forneça uma descrição ou resposta baseada na análise.\n                - Se não for possível responder a questão (ex.: falta de informações ou contexto insuficiente), deixe o campo `answer` como uma string vazia (`''`).\n\n                ### Exemplo de Entrada e Saída\n                1. **Entrada**: Questão com imagem e alternativas\n                {\n                    '0': {\n                        'question': 'Qual animal está na imagem?',\n                        'media': {'type': 'image', 'url': '[link]'},\n                        'alternatives': ['A) Cachorro', 'B) Gato']\n                    }\n                }\n                **Saída**:\n                {\n                    '0': {\n                        'type': 'Múltipla Escolha',\n                        'alternatives': {\n                            'media': {'type': 'image', 'url': '[link]'},\n                            'alternative': ['A) Cachorro', 'B) Gato']\n                        },\n                        'answer': 'B)'\n                    }\n                }\n\n                2. **Entrada**: Questão sem alternativas\n                {\n                    '0': {\n                        'question': 'Qual é a capital do Brasil?'\n                    }\n                }\n                **Saída**:\n                {\n                    '0': {\n                        'type': 'Resposta Curta',\n                        'alternatives': null,\n                        'answer': 'Brasília'\n                    }\n                }\n\n                3. **Entrada**: Apenas uma imagem\n                {\n                    '0': {\n                        'media': {'type': 'image', 'url': '[link]'}\n                    }\n                }\n                **Saída**:\n                {\n                    '0': {\n                        'type': '',\n                        'alternatives': {\n                            'media': {'type': 'image', 'url': '[link]'},\n                            'alternative': null\n                        },\n                        'answer': 'Descrição ou resposta baseada na análise da imagem'\n                    }\n                }\n\n                4. **Entrada**: Questão sem informações suficientes\n                {\n                    '0': {\n                        'question': 'Ordene as palavras.',\n                        'alternatives': ['']\n                    }\n                }\n                **Saída**:\n                {\n                    '0': {\n                        'type': '',\n                        'alternatives': {\n                            'media': null,\n                            'alternative': ['']\n                        },\n                        'answer': ''\n                    }\n                }\n\n                ### Notas Finais\n                - Retorne um único JSON com todas as questões processadas.\n                - Para tipos desconhecidos, use `type` como `''`.\n                - Analise imagens quando necessário para gerar respostas adequadas.\n                - Se não for possível responder, deixe `answer` como `''`.\n            "
            },
            "task_info": {
                "status_activity": "A Fazer",
                "site_activity_id": "71051809",
                "auto_activity_id": "",
                "activity_type": "Tarefa SP",
                "material_activity": "Matemática",
                "activity_title": "Relações métricas entre elementos de uma pirâmide",
                "user": "",
                "author": "anaselmaxavie2495862-sp",
                "class_school": "3º B EM",
                "first_access": "06/06/2025 - 00:55:29",
                "expires_in": "10/06/2025 - 00:00:00",
                "time_spent": "",
                "draft": "",
                "submitted": "",
                "text_num": 1,
                "question_types": {
                    "Radios": 2
                }
            },
            "texts": {
                "general": {
                    "secoes": {
                        "0": ""
                    },
                    "num_de_erros": 0,
                    "tipos_de_erros": {
                        "0": "",
                        "1": "",
                        "2": ""
                    },
                    "logs_de_erros": {
                        "0": {
                            "tipo": "",
                            "detalhes": "",
                            "questao": "",
                            "timestamp": ""
                        }
                    }
                },
                "0": {
                    "informative_content": {
                        "video": {},
                        "image": {
                            "0": {
                                "type": "image",
                                "src": "https://edusp-static.ip.tv/tms/edusp/tspmat8/FYQyDvcyS4XJdJONACqpw4Xp9KjgLz.png",
                                "local_path": "C:\\Users\\PC\\Desktop\\project\\FullStack\\_AutoAnswer\\auto_back\\project\\apps\\sala_do_futuro\\models\\realizar_atividades\\data\\img\\71051809 (6d)\\FYQyDvcyS4XJdJONACqpw4Xp9KjgLz.png"
                            }
                        },
                        "gif": {}
                    },
                    "secao": "",
                    "conteudo": "Veja a imagem para responder às questões: Fonte: https://es.aliexpress.com/i/1005006083913378.html.",
                    "num_de_erros": "",
                    "tipos_de_erros": [
                        "",
                        "",
                        ""
                    ],
                    "logs_de_erros": {
                        "0": {
                            "tipo": "",
                            "detalhes": "",
                            "questao": "",
                            "timestamp": ""
                        }
                    }
                }
            },
            "1": {
                "general": {
                    "activity_score": "",
                    "score_acquired": "",
                    "number_of_questions": 4,
                    "number_of_sections": 0,
                    "sections": {},
                    "number_of_guesses": "",
                    "number_of_user_responses": "",
                    "user_feedback": "",
                    "difficulty": "",
                    "history_of_attempts": {},
                    "ia": {
                        "ia1": {
                            "overall_performance": "",
                            "questions": [
                                "Identifique os triângulos presentes nas faces laterais da vela cônico-hexagonal e preencha a lacuna a seguir.",
                                "Sobre as medidas da vela cônico-hexagonal, julgue as afirmativas a seguir e as classifique como certas ou erradas.",
                                "Outra vela cônico-hexagonal foi produzida, com aresta laterais de 17 cm e altura de 15 cm. Assinale a alternativa que apresenta corretamente a medida das arestas da base dessa vela.",
                                "(Unilago, 2018) Na Figura 2, temos a representação do projeto de uma pirâmide em acrílico (Figura 1) que será utilizada na disciplina de Nutrição para discutir reeducação alimentar. A pirâmide [ABCDV], representada na Figura 2, é quadrangular regular. A Figura 2 não está desenhada em escala.Admita que, na Figura 2:a) a base [ABCD] da pirâmide pertence ao sistema cartesiano ortogonal xOy.b) o ponto A tem coordenadas (1, 1).c) o ponto B tem coordenadas (3, 1).d) a medida da altura da pirâmide é 2﻿6\\sqrt{6}6​﻿ unidades.Com base nessas informações, considere as afirmativas a seguir.I. O apótema da pirâmide mede ﻿6\\sqrt{6}6​﻿ unidades.II. A distância entre os pontos A e B mede 2 unidades.III. O raio da circunferência inscrita na base [ABCD] da pirâmide mede 1 unidade.IV. O centro da base [ABCD] da pirâmide é o centro da circunferência inscrita nesse polígono.Assinale a alternativa correta."
                            ],
                            "suggestions": {
                                "0": "",
                                "1": ""
                            }
                        },
                        "ia2": {
                            "desempenho_geral": "",
                            "questoes": [
                                "Identifique os triângulos presentes nas faces laterais da vela cônico-hexagonal e preencha a lacuna a seguir.",
                                "Sobre as medidas da vela cônico-hexagonal, julgue as afirmativas a seguir e as classifique como certas ou erradas.",
                                "Outra vela cônico-hexagonal foi produzida, com aresta laterais de 17 cm e altura de 15 cm. Assinale a alternativa que apresenta corretamente a medida das arestas da base dessa vela.",
                                "(Unilago, 2018) Na Figura 2, temos a representação do projeto de uma pirâmide em acrílico (Figura 1) que será utilizada na disciplina de Nutrição para discutir reeducação alimentar. A pirâmide [ABCDV], representada na Figura 2, é quadrangular regular. A Figura 2 não está desenhada em escala.Admita que, na Figura 2:a) a base [ABCD] da pirâmide pertence ao sistema cartesiano ortogonal xOy.b) o ponto A tem coordenadas (1, 1).c) o ponto B tem coordenadas (3, 1).d) a medida da altura da pirâmide é 2﻿6\\sqrt{6}6​﻿ unidades.Com base nessas informações, considere as afirmativas a seguir.I. O apótema da pirâmide mede ﻿6\\sqrt{6}6​﻿ unidades.II. A distância entre os pontos A e B mede 2 unidades.III. O raio da circunferência inscrita na base [ABCD] da pirâmide mede 1 unidade.IV. O centro da base [ABCD] da pirâmide é o centro da circunferência inscrita nesse polígono.Assinale a alternativa correta."
                            ],
                            "sugestoes": {
                                "0": "",
                                "1": ""
                            }
                        }
                    },
                    "error_number": 4,
                    "error_types": [
                        "",
                        "",
                        ""
                    ],
                    "error_logs": {
                        "0_0": {
                            "type": "",
                            "details": "",
                            "question": "",
                            "timestamp": ""
                        },
                        "1_0": {
                            "type": "",
                            "details": "",
                            "question": "",
                            "timestamp": ""
                        },
                        "2_0": {
                            "type": "",
                            "details": "",
                            "question": "",
                            "timestamp": ""
                        },
                        "3_0": {
                            "type": "",
                            "details": "",
                            "question": "",
                            "timestamp": ""
                        }
                    }
                },
                "0": {
                    "quest_info": {
                        "required": true,
                        "time": {
                            "day": "",
                            "start_time": "",
                            "end_time": ""
                        },
                        "activity_score": "",
                        "score": "",
                        "section": "",
                        "number_of_guesses": "",
                        "number_of_user_responses": "",
                        "user_feedback": "",
                        "difficulty": "",
                        "media": {
                            "video": {},
                            "image": {},
                            "gif": {}
                        },
                        "history_of_attempts": {},
                        "error_num": "",
                        "error_types": [
                            "",
                            "",
                            ""
                        ],
                        "error_logs": {
                            "0": {
                                "type": "",
                                "details": "",
                                "question": "",
                                "timestamp": ""
                            }
                        },
                        "ia": "",
                        "time_spent": ""
                    },
                    "quest": {
                        "type": "Unknown Type",
                        "statement": "Identifique os triângulos presentes nas faces laterais da vela cônico-hexagonal e preencha a lacuna a seguir.",
                        "alternatives": {
                            "media": {},
                            "alternative": [
                                ""
                            ]
                        },
                        "answer": ""
                    }
                },
                "1": {
                    "quest_info": {
                        "required": true,
                        "time": {
                            "day": "",
                            "start_time": "",
                            "end_time": ""
                        },
                        "activity_score": "",
                        "score": "",
                        "section": "",
                        "number_of_guesses": "",
                        "number_of_user_responses": "",
                        "user_feedback": "",
                        "difficulty": "",
                        "media": {
                            "video": {},
                            "image": {},
                            "gif": {}
                        },
                        "history_of_attempts": {},
                        "error_num": "",
                        "error_types": [
                            "",
                            "",
                            ""
                        ],
                        "error_logs": {
                            "0": {
                                "type": "",
                                "details": "",
                                "question": "",
                                "timestamp": ""
                            }
                        },
                        "ia": "",
                        "time_spent": ""
                    },
                    "quest": {
                        "type": "Unknown Type",
                        "statement": "Sobre as medidas da vela cônico-hexagonal, julgue as afirmativas a seguir e as classifique como certas ou erradas.",
                        "alternatives": {
                            "media": {},
                            "alternative": [
                                ""
                            ]
                        },
                        "answer": ""
                    }
                },
                "2": {
                    "quest_info": {
                        "required": true,
                        "time": {
                            "day": "",
                            "start_time": "",
                            "end_time": ""
                        },
                        "activity_score": "",
                        "score": "",
                        "section": "",
                        "number_of_guesses": "",
                        "number_of_user_responses": "",
                        "user_feedback": "",
                        "difficulty": "",
                        "media": {
                            "video": {},
                            "image": {},
                            "gif": {}
                        },
                        "history_of_attempts": {},
                        "error_num": "",
                        "error_types": [
                            "",
                            "",
                            ""
                        ],
                        "error_logs": {
                            "0": {
                                "type": "",
                                "details": "",
                                "question": "",
                                "timestamp": ""
                            }
                        },
                        "ia": "",
                        "time_spent": ""
                    },
                    "quest": {
                        "type": "Radios",
                        "statement": "Outra vela cônico-hexagonal foi produzida, com aresta laterais de 17 cm e altura de 15 cm. Assinale a alternativa que apresenta corretamente a medida das arestas da base dessa vela.",
                        "alternatives": {
                            "media": {},
                            "alternative": [
                                {
                                    "text": "A) 5 cm",
                                    "media": {
                                        "video": {},
                                        "image": {},
                                        "gif": {}
                                    }
                                },
                                {
                                    "text": "B) 6 cm",
                                    "media": {
                                        "video": {},
                                        "image": {},
                                        "gif": {}
                                    }
                                },
                                {
                                    "text": "C) 7 cm",
                                    "media": {
                                        "video": {},
                                        "image": {},
                                        "gif": {}
                                    }
                                },
                                {
                                    "text": "D) 8 cm",
                                    "media": {
                                        "video": {},
                                        "image": {},
                                        "gif": {}
                                    }
                                },
                                {
                                    "text": "E) 9 cm",
                                    "media": {
                                        "video": {},
                                        "image": {},
                                        "gif": {}
                                    }
                                }
                            ]
                        },
                        "answer": ""
                    }
                },
                "3": {
                    "quest_info": {
                        "required": true,
                        "time": {
                            "day": "",
                            "start_time": "",
                            "end_time": ""
                        },
                        "activity_score": "",
                        "score": "",
                        "section": "",
                        "number_of_guesses": "",
                        "number_of_user_responses": "",
                        "user_feedback": "",
                        "difficulty": "",
                        "media": {
                            "video": {},
                            "image": {
                                "0": {
                                    "type": "image",
                                    "src": "https://edusp-static.ip.tv/tms/edusp/tspmat8/1lhPauu9dF8BvKZGA3Sw2QHyHJRwoq.png",
                                    "local_path": "C:\\Users\\PC\\Desktop\\project\\FullStack\\_AutoAnswer\\auto_back\\project\\apps\\sala_do_futuro\\models\\realizar_atividades\\data\\img\\71051809 (6d)\\1lhPauu9dF8BvKZGA3Sw2QHyHJRwoq.png"
                                }
                            },
                            "gif": {}
                        },
                        "history_of_attempts": {},
                        "error_num": "",
                        "error_types": [
                            "",
                            "",
                            ""
                        ],
                        "error_logs": {
                            "0": {
                                "type": "",
                                "details": "",
                                "question": "",
                                "timestamp": ""
                            }
                        },
                        "ia": "",
                        "time_spent": ""
                    },
                    "quest": {
                        "type": "Radios",
                        "statement": "(Unilago, 2018) Na Figura 2, temos a representação do projeto de uma pirâmide em acrílico (Figura 1) que será utilizada na disciplina de Nutrição para discutir reeducação alimentar. A pirâmide [ABCDV], representada na Figura 2, é quadrangular regular. A Figura 2 não está desenhada em escala.Admita que, na Figura 2:a) a base [ABCD] da pirâmide pertence ao sistema cartesiano ortogonal xOy.b) o ponto A tem coordenadas (1, 1).c) o ponto B tem coordenadas (3, 1).d) a medida da altura da pirâmide é 2﻿6\\sqrt{6}6​﻿ unidades.Com base nessas informações, considere as afirmativas a seguir.I. O apótema da pirâmide mede ﻿6\\sqrt{6}6​﻿ unidades.II. A distância entre os pontos A e B mede 2 unidades.III. O raio da circunferência inscrita na base [ABCD] da pirâmide mede 1 unidade.IV. O centro da base [ABCD] da pirâmide é o centro da circunferência inscrita nesse polígono.Assinale a alternativa correta.",
                        "alternatives": {
                            "media": {},
                            "alternative": [
                                {
                                    "text": "A) Somente as afirmativas I e II são corretas.",
                                    "media": {
                                        "video": {},
                                        "image": {},
                                        "gif": {}
                                    }
                                },
                                {
                                    "text": "B) Somente as afirmativas I e IV são corretas.",
                                    "media": {
                                        "video": {},
                                        "image": {},
                                        "gif": {}
                                    }
                                },
                                {
                                    "text": "C) Somente as afirmativas III e IV são corretas.",
                                    "media": {
                                        "video": {},
                                        "image": {},
                                        "gif": {}
                                    }
                                },
                                {
                                    "text": "D) Somente as afirmativas I, II e III são corretas.",
                                    "media": {
                                        "video": {},
                                        "image": {},
                                        "gif": {}
                                    }
                                },
                                {
                                    "text": "E) Somente as afirmativas II, III e IV são corretas.",
                                    "media": {
                                        "video": {},
                                        "image": {},
                                        "gif": {}
                                    }
                                }
                            ]
                        },
                        "answer": ""
                    }
                }
            }
        }
    },
}

Estrutura do código (o quest_types era a forma anterior, irei tirar ele depois)

C:.
│   answerflowmanager.py
│   questions.py
│   __init__.py
│
├───answers
│       base_answer.py
│       checkbox_answer.py
│       radios_answer.py
│       __init__.py
│
├───extractor
│       base_extractor.py
│       checkbox_extractor.py
│       radios_extractor.py
│       __init__.py
│
├───quest_types
│   │   __init__.py
│   │
│   ├───checkbox
│   │   │   checkbox.py
│   │   │   __init__.py
│   │   │
│   │   ├───answer_checkbox
│   │   │   │   answer_checkbox.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           answer_checkbox.cpython-313.pyc
│   │   │           __init__.cpython-313.pyc
│   │   │
│   │   ├───get_checkbox
│   │   │   │   get_checkbox.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           get_checkbox.cpython-313.pyc
│   │   │           __init__.cpython-313.pyc
│   │   │
│   │   └───__pycache__
│   │           checkbox.cpython-313.pyc
│   │           __init__.cpython-313.pyc
│   │
│   ├───radios
│   │   │   radios.py
│   │   │   __init__.py
│   │   │
│   │   ├───answer_radios
│   │   │   │   answer_radios.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           answer_radios.cpython-313.pyc
│   │   │           __init__.cpython-313.pyc
│   │   │
│   │   ├───get_radios
│   │   │   │   get_radios.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           get_radios.cpython-313.pyc
│   │   │           __init__.cpython-313.pyc
│   │   │
│   │   └───__pycache__
│   │           radios.cpython-313.pyc
│   │           __init__.cpython-313.pyc
│   │
│   └───__pycache__
│           __init__.cpython-313.pyc
│
├───services
│       base_service.py
│       checkbox_service.py
│       radios_service.py
│       __init__.py
│
├───validations
│   │   common.py
│   │   validate_checkbox.py
│   │   validate_radios.py
│   │   __init__.py
│   │
│   └───__pycache__
│           common.cpython-313.pyc
│           validate_checkbox.cpython-313.pyc
│           validate_radios.cpython-313.pyc
│           __init__.cpython-313.pyc
│
└───__pycache__
        questions.cpython-313.pyc
        __init__.cpython-313.pyc

Esse foi o código que ele me propos

AnswerFlowManager

from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions.services import ServiceFactory

class AnswerFlowManager:
    def __init__(self, questions: dict):
        self.questions = questions

    def process_all(self):
        for qid, qdata in self.questions.items():
            q_type = qdata.get('type', '')
            try:
                service = ServiceFactory.get_service(q_type)
                is_valid, error = service.validate(qdata)
                if not is_valid:
                    print(f'Questão {qid} inválida: {error}')
                    continue
                service.answer(qdata)
            except Exception as e:
                print(f'Erro na questão {qid}: {str(e)}')

ValidateCheckbox

class ValidateCheckbox:
    def __init__(self):
        pass

    def validate(self, respostas, opcoes):
        try:
            if not isinstance(respostas, list):
                raise ValueError('As respostas devem ser uma lista.')
            if not respostas:
                raise ValueError('Pelo menos uma opção deve ser selecionada.')
            if len(respostas) > len(opcoes):
                raise ValueError('Número de respostas excede o número de opções.')
            for resposta in respostas:
                if resposta not in opcoes:
                    raise ValueError(f'\'{resposta}\' não é uma opção válida.')
            return True
        except ValueError as e:
            print(f'Erro de validação: {e}')
            return False

ValidateRadios

class ValidateRadios:
    def __init__(self):
        pass

    def validate(self, resposta, opcoes):
        try:
            if not isinstance(resposta, str):
                raise ValueError('A resposta deve ser uma string.')
            if resposta not in opcoes:
                raise ValueError(f'\'{resposta}\' não é uma opção válida.')
            return True
        except ValueError as e:
            print(f'Erro de validação: {e}')
            return False

CheckboxService

from .baseservice import BaseService
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions.validations.validate_checkbox import ValidateCheckbox #?ATUALIZAR_INIT
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions.answers import CheckboxAnswer #?ATUALIZAR_INIT

class CheckboxService(BaseService):
    def validate(self, question_data: dict):
        return ValidateCheckbox(question_data)

    def answer(self, question_data: dict):
        CheckboxAnswer().execute(question_data)

RadiosService

from .baseservice import BaseService
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions.validations import ValidateRadios #?ATUALIZAR_INIT
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions.answers import RadiosAnswer #?ATUALIZAR_INIT

class RadiosService(BaseService):
    def validate(self, question_data: dict):
        return ValidateRadios(question_data)

    def answer(self, question_data: dict):
        RadiosAnswer().execute(question_data)

ServiceFactory

from .checkbox_service import CheckboxService
from .radios_service import RadiosService

class ServiceFactory:
    _services = {
        'Radios': RadiosService,
        'Checkbox': CheckboxService,
    }

    ''''''
    @classmethod
    def get_service(cls, question_type: str):
        service_class = cls._services.get(question_type)
        if not service_class:
            raise ValueError(f'Serviço não implementado para o tipo: {question_type}')
        return service_class()

RadiosAnswer

class RadiosAnswer:
    def __init__(self):
        pass
    
    def execute(self, question_data):
        # Aqui você usaria PyAutoGUI, simulação ou IA
        print(f"[RadiosAnswer] Respondendo: {question_data['statement']}")
        # Atualiza a resposta, se for o caso:
        question_data["answer"] = "A)"  # Simulado

CheckboxAnswer

class CheckboxAnswer:
    def __init__(self):
        pass
        
    def execute(self, question_data):
        # Aqui você usaria PyAutoGUI, simulação ou IA
        print(f"[RadiosAnswer] Respondendo: {question_data['statement']}")
        # Atualiza a resposta, se for o caso:
        question_data["answer"] = "A)"  # Simulado


-->

<!--

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
