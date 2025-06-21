from .baseservice import BaseService
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions.validations.validate_checkbox import ValidateCheckbox #?ATUALIZAR_INIT
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions.answers import CheckboxAnswer #?ATUALIZAR_INIT

class CheckboxService(BaseService):
    def validate(self, question_data: dict):
        return ValidateCheckbox(question_data)

    def answer(self, question_data: dict):
        CheckboxAnswer().execute(question_data)
