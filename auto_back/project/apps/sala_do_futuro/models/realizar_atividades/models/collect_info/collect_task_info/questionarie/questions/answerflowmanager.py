from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info.questionarie.questions.services import ServiceFactory

class AnswerFlowManager:
    def __init__(self, questions: dict):
        self.questions = questions

    def process_all(self):
        for qid, qdata in self.questions.items():
            q_type = qdata.get('type', '')
            try:
                service = ServiceFactory.get_service(q_type)
                is_valid, error = service.validate(qdata)
                if not is_valid:
                    print(f'Questão {qid} inválida: {error}')
                    continue
                service.answer(qdata)
            except Exception as e:
                print(f'Erro na questão {qid}: {str(e)}')
