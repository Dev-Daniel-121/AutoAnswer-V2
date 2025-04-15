from project import Display, types
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_info import CollectInfo

class RealizarTarefa:
    def __init__(self, page):
        self.page = page
        self.display = Display
        self.collectInfo = CollectInfo(page=self.page)

    def run(self, user, id_usuario):
        
        component, title_activity, user_activity, author_activity, class_activity, expire_activity, id_activity = self.collectInfo.collect_task_info()

        options = self.display(data='', title=f'{component} - {id_activity}', answer=False, user=f'{user}', title_quest='')
        options.display()
        
        # print(f'[{types[9]}] Coletando informações da Atividade...\n')

        # print(f'[{types[9]}] Título Atividade: {title_activity}\n[{types[9]}] Usuário da atividade: {user_activity}\n[{types[9]}] Autor da atividade: {author_activity}\n[{types[9]}] Turma: {class_activity}\n[{types[9]}] Expira em: {expire_activity}\n[{types[9]}] ID: {id_activity}')

        self.collectInfo.collect_json(component='tarefa', id_activity=id_activity)

        print(f'[{types[9]}] Coletando informações da Atividade...\n')

        self.collectInfo.collect_quest()

        input(f'\n\nPrecione\n\n')