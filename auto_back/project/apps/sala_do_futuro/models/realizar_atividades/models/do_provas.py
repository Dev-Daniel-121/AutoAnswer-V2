from project.apps.sala_do_futuro.models.data.tarefas import Go
from project import Display, types
import os

class DoProvas:
    def __init__(self, page):
        self.page = page
        self.display = Display
        self.go = Go(
            page=self.page, get_title_class='span.css-14ra0qi', btn_go_provas_class=':nth-match(a.css-lumvx8, 4)', go_btn_class=':nth-match(div.css-39ukww, 2)', go_list_class='li.css-4dqmvd')
        
    def run_aFazer(self, RealizarAtividades, user):
        print('')
        
        self.go.go_aFazer()

        while True:
            try:
                user_choice = int(RealizarAtividades.show_task_infos(user=user))
            except ValueError:
                print(f'[{types[4]}] A escolha deve ser um número inteiro.')
                continue
            except Exception as e:
                print(f'[{types[4]}] Erro ao obter escolha do Usuário: {e}')
                continue

            task_infos = RealizarAtividades.get_task_infos()

            if 1 <= user_choice <= len(task_infos):
                if user_choice == len(task_infos):
                    return
                else:
                    print(f'Sua escolha foi: {user_choice}')
                    input('\nPressione Enter para continuar...')
                    return
            else:
                print(f'[{types[4]}] Opção inválida: {user_choice}. As opções devem estar entre 1 e {len(task_infos)}.')
                continue

    def run_expiradas(self, RealizarAtividades, user):
        self.go.go_expiradas()

        while True:
            try:
                user_choice = int(RealizarAtividades.show_task_infos(user=user))
            except ValueError:
                print(f'[{types[4]}] A escolha deve ser um número inteiro.')
                continue
            except Exception as e:
                print(f'[{types[4]}] Erro ao obter escolha do Usuário: {e}')
                continue

            task_infos = RealizarAtividades.get_task_infos()

            if 1 <= user_choice <= len(task_infos):
                if user_choice == len(task_infos):
                    break
                else:
                    print(f'Sua escolha foi: {user_choice}')
                    input('\nPressione Enter para continuar...')
                    break
            else:
                print(f'[{types[4]}] Opção inválida: {user_choice}. As opções devem estar entre 1 e {len(task_infos)}.')
                continue

    def run(self, user, id_usuario):
        from project.apps.sala_do_futuro.models import RealizarAtividades
        RealizarAtividades = RealizarAtividades(page=self.page)

        os.system('cls' if os.name == 'nt' else 'clear')

        self.go.go_provas()

        self.run_aFazer(RealizarAtividades=RealizarAtividades, user=user)
        print(f'\n{'-' * 30}\n')
        self.run_expiradas(RealizarAtividades=RealizarAtividades, user=user)
