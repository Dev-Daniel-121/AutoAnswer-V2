from project import types

class Sections:
    def __init__(self, page, sections_turmas_class='', sections_status_class='', sections_componentes_class=''):
        self.page = page
        self.sections_turmas_class = sections_turmas_class
        self.sections_status_class = sections_status_class
        self.sections_componentes_class = sections_componentes_class

    def sections_turmas(self):
        try:
            sections_turmas = self.page.locator(f'{self.sections_turmas_class}')
            sections_turmas = sections_turmas.inner_text()
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter informações das turmas: {e}')

        return sections_turmas
    
    def sections_status(self):
        try:
            sections_status = self.page.locator(f'{self.sections_status_class}')
            sections_status = sections_status.inner_text()
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter o status: {e}')

        return sections_status
    
    def sections_componentes(self):
        try:
            sections_componentes = self.page.input_value(f'{self.sections_componentes_class}')
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter os componentes: {e}')

        return sections_componentes

    def run(self):
        sections_turmas = self.sections_turmas()
        sections_status = self.sections_status()
        sections_componentes = self.sections_componentes()

        print(f'\n[{types[9]}] Turmas: {sections_turmas} | Status: {sections_status} | Componente: {sections_componentes}\n')