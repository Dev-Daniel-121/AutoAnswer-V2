from .collect_tarefas import CollectTarefas, CollectTaskInfos
from .collect_task_info.collect_task_info import TaskInfo
from .collect_task_info.questionarie import Questionarie
from .collect_task_info.texts import Text
from .collect_json import CollectJson
from project import Display, types
from .collect_time import Time

class CollectInfo:
    def __init__(self, page, activity_status, component):
        self.page = page
        self.types = types
        self.display = Display
        self.activity_status = activity_status
        self.component = component

        self.task_info = TaskInfo(
            page=self.page, activity_status=self.activity_status,
            activity_type_class = ':nth-match(li.MuiBreadcrumbs-li, 2)',
            material_activity_class = 'h6.css-yq44kw',
            activity_title_class = 'p.css-zscg42'
        )
        self.text = Text(page=self.page, information_card_class='css-1mpla7o', elem_section_class='div.css-8atqhb h2')

        self.questionarie = Questionarie(
            page=self.page, elem_section_class='div.css-8atqhb h2',
            can_get_points='div.css-18oghjr', btn_end_activity='button.css-1wjnhbh',
            btn_save_as_draft_activity='button.css-19d44l7', question='div.css-b200pa')

        self.time = Time()
        self.collect_json = CollectJson()
        self.collect_tarefas = CollectTarefas(page=self.page)
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

    def display_info(self, texts, quests):
        type_counter = {}
        unknown_type_questions = []

        for quest_num, quest_data in quests.items():
            quest_type = quest_data.get('quest', {}).get('type', '').strip()
            if not quest_type or quest_type == 'Unknown Type':
                unknown_type_questions.append(str(int(quest_num) + 1))
            else:
                type_counter[quest_type] = type_counter.get(quest_type, 0) + 1

        print(f'[{types[9]}] Número de textos: {len(texts)}')
        print(f'[{types[9]}] Número de questões: {len(quests)}\n')

        print(f'[{types[9]}] Tipos de questões encontradas:')
        for qtype, count in type_counter.items():
            print(f'   [{types[9]}] {qtype}: {count}')

        if unknown_type_questions:
            print(f'\n[{types[9]}] Questões desconhecidas encontradas:')
            print(f'   [{types[9]}] Questões: {', '.join(unknown_type_questions)}\n')


    def run(self, user, id_usuario):
        task_info = self.task_info.run()

        # component, title_activity, user_activity, author_activity, class_activity, expire_activity, id_activity = self.collect_task_infos.run()

        options = self.display(data='', title=f'{task_info['material_activity']} - {task_info['site_activity_id']}', answer=False, user=f'{user}', title_quest='')
        options.display()

        self.time.timer(seconds=60)

        self.collect_json.run(component=self.component, id_activity=task_info['site_activity_id'])

        text = self.text.run()
        questionarie = self.questionarie.run()

        self.display_info(texts=text, quests=questionarie)

        """
        self.collect_tarefas.run()

        print(f'\n\n\n{task_info}\n\n\n')
        print(f'{text}\n\n\n')
        """
        print(questionarie)

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

'''
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

### Notas Finais
- Retorne um único JSON com todas as questões processadas.
- Para tipos desconhecidos, use `type` como `''`.
- Analise imagens quando necessário para gerar respostas adequadas.

'''
