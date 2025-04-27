from project.apps.sala_do_futuro.models.realizar_atividades.models import CollectInfo
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.collect_task_info import CollectTaskInfo
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions.questions import Questions

class RealizarTarefa:
    def __init__(self, page):
        self.page = page
        self.collect_info = CollectInfo(page=self.page)
        self.collect_task_info = CollectTaskInfo(page=self.page, activity_status='A Fazer')
        self.question = Questions(page=self.page)

    def run(self, user, id_usuario):
        self.collect_info.run(user=user, id_usuario=id_usuario)
        self.collect_task_info.run()
        self.question.run()



        input(f'\n\nPrecione\n\n')