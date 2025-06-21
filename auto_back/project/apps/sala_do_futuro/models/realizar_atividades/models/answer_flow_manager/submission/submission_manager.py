from .submission_action_handler import SubmissionActionHandler
from .response_validator import ResponseValidator
from project import LogType

class SubmissionManager:
    def __init__(
            self, page,
            btn_end_activity_class, btn_save_as_draft_activity_class,
            unanswered_questions_class, num_question_current_class
        ):
        self.page = page

        self.action_handler = SubmissionActionHandler(
            page=page,
            btn_end_activity_class=btn_end_activity_class,
            btn_save_as_draft_activity_class=btn_save_as_draft_activity_class
        )

        self.validator = ResponseValidator(
            page=page.content(),
            unanswered_questions_class=unanswered_questions_class,
            num_question_current_class=num_question_current_class
        )

    def run(self, action: str) -> dict:
        result = {
            'success': False,
            'unanswered_questions': [],
            'message': ''
        }

        try:
            if action not in ['finalizar', 'rascunho']:
                raise ValueError(f'[{LogType.ERROR}] Ação inválida. Use \'finalizar\' ou \'rascunho\'.')

            self.action_handler.handle(action)

            self.validator.page = self.page.content()
            unanswered = self.validator.validate()

            if unanswered:
                result['unanswered_questions'] = unanswered
                result['message'] = f'[{LogType.WARNING}] Existem questões não respondidas.'
                return result

            result['success'] = True
            result['message'] = f'[{LogType.SUCCESS}] Submissão finalizada com sucesso.'
            return result

        except Exception as e:
            result['message'] = f'[{LogType.ERROR}] Erro durante a submissão: {e}'
            return result
