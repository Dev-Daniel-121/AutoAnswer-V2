from project.apps.sala_do_futuro.models.realizar_atividades.realizar_atividades import RealizarAtividades
from project.apps.sala_do_futuro.models.login_user.login_user import LoginUser
from project.apps.sala_do_futuro.models.data.data import Data
from project import types, Display
import os

class MenuSystem:
    def __init__(self, page):
        self.display = Display
        self.types = types
        self.logged_in = False
        self.usuario = None
        self.page = page

    def menu(self):
        while True:
            options_data = [(2, 'Efetuar login'), (2, 'Exibir dados escolares'), (2, 'Realizar Atividades'), (2, 'Sair')]
            options = self.display(options_data, 'MENU', answer=False, user=f'{self.usuario.nome} {self.usuario.sobrenome}', title_quest='')
            options.display()
            user_choice = input(f'\n[{types[1]}] Digite a opção desejada: ')

            try:
                choice = int(user_choice.strip())
            except ValueError:
                print(f'[{types[4]}] Entrada inválida. Por favor, digite um número válido.')
                input(f'\n[{types[6]}] Pressione Enter para continuar...')
                continue

            if choice < 1 or choice > 4:
                print(f'[{types[4]}] Opção inválida. As opções devem estar entre 1 e 4.')
                input(f'\n[{types[6]}] Pressione Enter para continuar...')
                continue

            if choice == 1:
                if self.logged_in:
                    print(f'[{types[3]}] Você já está logado.')
                else:
                    login_user = LoginUser(
                        page=self.page,
                        tipo=self.usuario.tipo_conta,
                        ra=self.usuario.ra,
                        dg_ra=self.usuario.dg_ra,
                        uf_ra=self.usuario.uf_ra,
                        senha=self.usuario.senha
                    )
                    login_user.run()
                    self.logged_in = True
            elif choice == 2:
                if not self.logged_in:
                    print(f'[{types[4]}] Você precisa estar logado para exibir dados escolares.')
                    input(f'\n[{types[6]}] Pressione Enter para continuar...')
                    continue
                data = Data(page=self.page)
                data.run()
            elif choice == 3:
                if not self.logged_in:
                    print(f'[{types[4]}] Você precisa estar logado para realizar atividades.')
                    input(f'\n[{types[6]}] Pressione Enter para continuar...')
                    continue
                realizar = RealizarAtividades()
                realizar.run(self.usuario)
            elif choice == 4:
                print(f'[{types[4]}] Saindo...')
                break
            else:
                print(f'[{types[4]}] Opção inválida: {choice}')
                continue

    def run(self, usuario):
        self.usuario = usuario
        self.menu()