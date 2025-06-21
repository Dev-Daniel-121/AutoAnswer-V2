from project import LogType

class SubmissionActionHandler:
    def __init__(
            self, page, btn_end_activity_class, btn_save_as_draft_activity_class
        ):
        self.page = page
        self.btn_end_activity_class = btn_end_activity_class
        self.btn_save_as_draft_activity_class = btn_save_as_draft_activity_class

    def handle(self, action: str):
        if action == 'finalizar':
            try:
                self._click_submit()
            except Exception as e:
                print(f'[{LogType.ERROR}] Erro ao ultilizar a função _click_submit: {e}')
                input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')
        elif action == 'rascunho':
            try:
                self._click_save_draft()
            except Exception as e:
                print(f'[{LogType.ERROR}] Erro ao ultilizar a função _click_save_draft: {e}')
                input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')
        else:
            raise ValueError(f'Ação desconhecida: {action}')

    def _click_submit(self):
        try:
            btn_end_activity = self.page.locator(self.btn_end_activity_class)
            btn_end_activity.click()
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao tentar finalizar a atividade: {e}')
            input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')

    def _click_save_draft(self):
        try:
            btn_save_as_draft_activity = self.page.locator(self.btn_save_as_draft_activity_class)
            btn_save_as_draft_activity.click()
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao tentar salvar como rascunho a atividade: {e}')
            input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')
