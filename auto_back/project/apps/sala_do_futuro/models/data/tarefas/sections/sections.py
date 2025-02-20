from project import types

class Sections:
    def __init__(self, page):
        self.page = page

    def sections_turmas(self):
        sections_turmas_class = ':nth-match(div.css-39ukww, 1)'
        sections_turmas = self.page.locator(f'{sections_turmas_class}')
        sections_turmas = sections_turmas.inner_text()

        return sections_turmas
    
    def sections_status(self):
        sections_status_class = ':nth-match(div.css-39ukww, 2)'
        sections_status = self.page.locator(f'{sections_status_class}')
        sections_status = sections_status.inner_text()

        return sections_status
    
    def sections_componentes(self):
        sections_componentes_class = 'input.css-scvshb'
        sections_componentes = self.page.input_value(f'{sections_componentes_class}')

        return sections_componentes

    def run(self):
        sections_turmas = self.sections_turmas()
        sections_status = self.sections_status()
        sections_componentes = self.sections_componentes()

        print(f'\n[{types[9]}] Turmas: {sections_turmas} | Status: {sections_status} | Componente: {sections_componentes}')