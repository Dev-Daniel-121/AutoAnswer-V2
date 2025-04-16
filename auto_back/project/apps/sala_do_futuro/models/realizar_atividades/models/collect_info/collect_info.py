from .collect_tarefas import CollectTarefas, CollectTaskInfos
from .collect_json import CollectJson
from project import Display, types

class CollectInfo:
    def __init__(self, page):
        self.page = page
        self.display = Display
        self.collect_json = CollectJson()
        self.collect_tarefas = CollectTarefas()
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
        component, title_activity, user_activity, author_activity, class_activity, expire_activity, id_activity = self.collect_task_infos.run()

        options = self.display(data='', title=f'{component} - {id_activity}', answer=False, user=f'{user}', title_quest='')
        options.display()
        
        self.collect_json.run(component='tarefa', id_activity=id_activity)

        print(f'[{types[9]}] Coletando informações da Atividade...\n')

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