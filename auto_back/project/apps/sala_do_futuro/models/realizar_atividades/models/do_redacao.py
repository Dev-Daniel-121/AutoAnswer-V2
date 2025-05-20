from project.apps.sala_do_futuro.models import Go
from project import Display, LogType
import os

class DoRedacao:
    def __init__(self, page):
        self.page = page
        self.display = Display
        self.go = Go(page=self.page, get_title_class='span.css-14ra0qi', btn_go_redacoes_class=':nth-match(a.css-lumvx8, 3)', go_btn_class=':nth-match(div.css-39ukww, 2)', go_list_class='li.css-4dqmvd')

    def process_user_choice(self, choice_input, task_infos):
        choices = []
        
        choice_input = choice_input.strip().lower()
        
        if choice_input in ('*', 'all'):
            return list(range(1, len(task_infos)))
        
        for part in choice_input.split(','):
            part = part.strip()
            if not part:
                continue
            try:
                choice = int(part)
                if 1 <= choice <= len(task_infos):
                    if choice != len(task_infos):
                        choices.append(choice)
                else:
                    print(f'[{LogType.ERROR}] Opção inválida: {choice}. As opções devem estar entre 1 e {len(task_infos)}.')
                    return None
            except ValueError:
                print(f'[{LogType.ERROR}] Valor inválido: {part}. Deve ser um número inteiro.')
                return None
        
        return sorted(list(set(choices)))

    def run_aFazer(self, RealizarAtividades, user):
        print('')
        self.go.go_aFazer()

        while True:
            try:
                choice_input = RealizarAtividades.show_task_infos(user=user)
                task_infos = RealizarAtividades.get_task_infos()
                
                user_choices = self.process_user_choice(choice_input, task_infos)
                if user_choices is None:
                    continue
                
                if not user_choices:
                    print(f'[{LogType.ERROR}] Nenhuma opção válida selecionada.')
                    continue
                
                print(f'[{LogType.ANSWER}] Sua escolha foi: {user_choices}')

                for choice in user_choices:
                    print(f'\n[{LogType.INFO}] Executando escolha: {choice}\n')
                
                input('\nPressione Enter para continuar...')
                return
                
            except Exception as e:
                print(f'[{LogType.ERROR}] Erro ao obter escolha do Usuário: {e}')
                continue

    def run_expiradas(self, RealizarAtividades, user):
        self.go.go_expiradas()

        while True:
            try:
                choice_input = RealizarAtividades.show_task_infos(user=user)
                task_infos = RealizarAtividades.get_task_infos()
                
                user_choices = self.process_user_choice(choice_input, task_infos)
                if user_choices is None:
                    continue
                
                if not user_choices:
                    print(f'[{LogType.ERROR}] Nenhuma opção válida selecionada.')
                    continue
                
                print(f'[{LogType.ANSWER}] Sua escolha foi: {user_choices}')

                for choice in user_choices:
                    print(f'\n[{LogType.INFO}] Executando escolha: {choice}\n')
                
                input('\nPressione Enter para continuar...')
                return
                
            except Exception as e:
                print(f'[{LogType.ERROR}] Erro ao obter escolha do Usuário: {e}')
                continue

    def run(self, user, id_usuario):
        from project.apps import RealizarAtividades
        RealizarAtividades = RealizarAtividades(page=self.page)

        os.system('cls' if os.name == 'nt' else 'clear')

        self.go.go_redacoes()

        self.run_aFazer(RealizarAtividades=RealizarAtividades, user=user)

        print(f'\n{'-' * 30}\n')

        self.run_expiradas(RealizarAtividades=RealizarAtividades, user=user)
