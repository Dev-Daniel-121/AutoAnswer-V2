from .baseservice import BaseService
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions.validations import ValidateRadios #?ATUALIZAR_INIT
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions.answers import RadiosAnswer #?ATUALIZAR_INIT

class RadiosService(BaseService):
    def validate(self, question_data: dict):
        return ValidateRadios(question_data)

    def answer(self, question_data: dict):
        RadiosAnswer().execute(question_data)
