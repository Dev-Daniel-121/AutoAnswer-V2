from .submission import SubmissionManager
from .services import ServiceFactory
from project import LogType

class AnswerFlowManager:
    def __init__(
            self, page, questions: dict,
            btn_end_activity_class, btn_save_as_draft_activity_class,
            unanswered_questions_class, num_question_current_class
        ):
        self.page = page
        self.questions = questions

        self.btn_end_activity_class = btn_end_activity_class,
        self.btn_save_as_draft_activity_class = btn_save_as_draft_activity_class,
        self.unanswered_questions_class = unanswered_questions_class,
        self.num_question_current_class = num_question_current_class,

        self.SubmissionManager = SubmissionManager(
            page=page,
            btn_end_activity_class=self.btn_end_activity_class,
            btn_save_as_draft_activity_class=self.btn_save_as_draft_activity_class,
            unanswered_questions_class=self.unanswered_questions_class,
            num_question_current_class=self.num_question_current_class
        )

    def process_all(self, only_questions: list = None):
        questions_to_process = (
            {qid: self.questions[qid] for qid in only_questions}
            if only_questions else self.questions
        )
        
        for qid, qdata in questions_to_process.items():
            q_type = qdata.get('type', '')
            try:
                service = ServiceFactory.get_service(q_type)
                is_valid, error = service.validate(qdata)
                if not is_valid:
                    print(f'[{LogType.ERROR}] Questão {qid} inválida: {error}')
                    continue
                service.answer(qdata)
            except Exception as e:
                print(f'[{LogType.ERROR}] Erro na questão {qid}: {str(e)}')
    
    def submit(self):
        action = self._ask_action()
        result = self.SubmissionManager.run(action)

        if result['success']:
            print(f'[{LogType.SUCCESS}] {result['message']}')
        else:
            print(f'[{LogType.WARNING}] {result['message']}')
            if result['unanswered_questions']:
                print(f'[{LogType.WARNING}] Reprocessando questões não respondidas: {result['unanswered_questions']}')
                self.process_all(only_questions=result['unanswered_questions'])

                print(f'[{LogType.INFO}] Tentando submeter novamente...')
                second_result = self.SubmissionManager.run(action)

                if second_result['success']:
                    print(f'[{LogType.SUCCESS}] Submissão realizada com sucesso na segunda tentativa.')
                else:
                    print(f'[{LogType.ERROR}] Ainda há questões sem resposta: {second_result['unanswered_questions']}')

    def _ask_action(self) -> str:
        while True:
            resposta = input(f'[{LogType.MSG}] Deseja finalizar (F) ou salvar como rascunho (D)? (F/d) ').strip().lower()
            if resposta in ['', 'f', 'finalizar']:
                return 'finalizar'
            elif resposta in ['d', 'rascunho']:
                return 'rascunho'
            print(f'[{LogType.WARNING}] Opção inválida. Digite \'F\' para finalizar ou \'D\' para rascunho.')
