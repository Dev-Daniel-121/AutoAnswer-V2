from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info import TaskInfo

class CollectTaskInfo:
    def __init__(self, page, activity_status):
        self.page = page
        self.activity_status = activity_status
        self.task_infos = TaskInfo(
            page=self.page, activity_status=self.activity_status,
            activity_type_class = ':nth-match(li.MuiBreadcrumbs-li, 2)',
            material_activity_class = 'h6.css-yq44kw',
            activity_title_class = 'p.css-zscg42'
        )

    def run(self):
        self.task_infos.run()
    