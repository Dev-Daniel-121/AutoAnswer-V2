from .collect_task_info.collect_task_info import TaskInfo
from .collect_task_info.questionarie import Questionarie

from .collect_tarefas import CollectTarefas, CollectTaskInfos
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
        self.questionarie = Questionarie(page=self.page)

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


    def run(self, user, id_usuario):
        task_info = self.task_info.run()

        # component, title_activity, user_activity, author_activity, class_activity, expire_activity, id_activity = self.collect_task_infos.run()

        options = self.display(data='', title=f'{task_info['material_activity']} - {task_info['site_activity_id']}', answer=False, user=f'{user}', title_quest='')
        options.display()

        self.time.timer(seconds=60)

        self.collect_json.run(component=self.component, id_activity=task_info['site_activity_id'])

        print(f'\n\n\n{task_info}\n\n\n')

        questionarie = self.questionarie.run()
        print(questionarie)

        # self.collect_tarefas.run()

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