from project.apps.sala_do_futuro.models.realizar_atividades.models import CollectInfo, CollectTaskInfo, Questionarie

class RealizarTarefa:
    def __init__(self, page):
        self.page = page
        self.collect_info = CollectInfo(page=self.page, activity_status='A Fazer', component='tarefa')
        self.collect_task_info = CollectTaskInfo(page=self.page, activity_status='A Fazer')
        self.questionarie = Questionarie(
            page=self.page, elem_section_class='div.css-8atqhb h2', 
            can_get_points='div.css-18oghjr', btn_end_activity='button.css-1wjnhbh',
            btn_save_as_draft_activity='button.css-19d44l7', question='div.css-b200pa'
        )

    def run(self, user, id_usuario):
        self.collect_info.run(user=user, id_usuario=id_usuario)
        # self.collect_task_info.run()
        # self.questionarie.run()

        input(f'\n\nPrecione\n\n')