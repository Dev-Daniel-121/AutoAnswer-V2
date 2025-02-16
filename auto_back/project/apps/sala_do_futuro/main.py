from playwright.sync_api import sync_playwright
from project.apps.sala_do_futuro.classes._global.menu_system.menusystem import MenuSystem

class SalaDoFuturo:
    def __init__(self):
        pass
        self.nome = "Sala do Futuro"

    def printa(self):
        print(f"Bem-vindo à {self.nome}!")

    def iniciar(self):
        print(f"Iniciando {self.nome}...")

    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('https://saladofuturo.educacao.sp.gov.br/')

            menu_system = MenuSystem()
            menu_system.run()

def printa():
    sala = SalaDoFuturo()
    sala.printa()
