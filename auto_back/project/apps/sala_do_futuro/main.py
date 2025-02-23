from project.apps.sala_do_futuro.menus import MenuSystem
from playwright.sync_api import sync_playwright
from project import SistemaUsuarios, types

class SalaDoFuturo:
    def __init__(self):
        self.sistema_usuarios = SistemaUsuarios()

    def run(self, id_usuario):
        usuarios = self.sistema_usuarios.carregar_usuarios()
        usuario = usuarios.get(str(id_usuario))

        if not usuario:
            print(f'[{types[4]}] Usuário com ID {id_usuario} não encontrado.')
            return

        print(f'\n[{types[9]}] Iniciando automação para {usuario.nome} {usuario.sobrenome} ({usuario.tipo_conta})')

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('https://saladofuturo.educacao.sp.gov.br/')
            
            print(f'Usando email: {usuario.email}, RA: {usuario.ra}')
            
            menu_system = MenuSystem(page)
            menu_system.run(usuario)

