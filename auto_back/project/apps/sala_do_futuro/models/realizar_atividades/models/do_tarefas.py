from project.apps.sala_do_futuro.models.realizar_atividades.models.tarefas import RealizarTarefa
from project.apps.sala_do_futuro.models.data.tarefas import Activities, Go
from project import Display, types
import os

class DoTarefas:
    def __init__(self, page):
        self.page = page
        self.display = Display
        self.go = Go(page=self.page, get_title_class='span.css-14ra0qi', btn_go_tarefas_class=':nth-match(a.css-lumvx8, 2)', go_btn_class=':nth-match(div.css-39ukww, 2)', go_list_class='li.css-4dqmvd')
        self.activities = Activities(page=self.page)
        self.realizarTarefa = RealizarTarefa(page=self.page)

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
                    print(f'[{types[4]}] Opção inválida: {choice}. As opções devem estar entre 1 e {len(task_infos)}.')
                    return None
            except ValueError:
                print(f'[{types[4]}] Valor inválido: {part}. Deve ser um número inteiro.')
                return None
        
        return sorted(list(set(choices)))

    def run_aFazer(self, RealizarAtividades, user, id_usuario):
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
                    print(f'[{types[4]}] Nenhuma opção válida selecionada.')
                    continue
                
                print(f'[{types[3]}] Sua escolha foi: {user_choices}')

                for choice in user_choices:
                    print(f'\n[{types[9]}] Executando escolha: {choice}\n')
                    self.activities.enter_activity(activity_class=f':nth-match(div.css-fm7u1u, {choice})', btn_enter_activity_class='button.css-g82asz')
                    self.realizarTarefa.run(user=user, id_usuario=id_usuario)
                
                input(f'\n[{types[6]}] Pressione Enter para continuar...')
                return
                
            except Exception as e:
                print(f'[{types[4]}] Erro ao obter escolha do Usuário: {e}')
                continue

    def run_expiradas(self, RealizarAtividades, user, id_usuario):
        self.go.go_expiradas()

        while True:
            try:
                choice_input = RealizarAtividades.show_task_infos(user=user)
                task_infos = RealizarAtividades.get_task_infos()
                
                user_choices = self.process_user_choice(choice_input, task_infos)
                if user_choices is None:
                    continue
                
                if not user_choices:
                    print(f'[{types[4]}] Nenhuma opção válida selecionada.')
                    continue
                
                print(f'[{types[3]}] Sua escolha foi: {user_choices}')

                for choice in user_choices:
                    print(f'\n[{types[9]}] Executando escolha: {choice}\n')
                
                input(f'\n[{types[6]}] Pressione Enter para continuar...')
                return
                
            except Exception as e:
                print(f'[{types[4]}] Erro ao obter escolha do Usuário: {e}')
                continue

    def run(self, user, id_usuario):
        from project.apps.sala_do_futuro.models import RealizarAtividades
        RealizarAtividades = RealizarAtividades(page=self.page)

        os.system('cls' if os.name == 'nt' else 'clear')

        self.go.go_tarefas()

        self.run_aFazer(RealizarAtividades=RealizarAtividades, user=user, id_usuario=id_usuario)

        print(f'\n{'-' * 30}\n')

        self.run_expiradas(RealizarAtividades=RealizarAtividades, user=user, id_usuario=id_usuario)
