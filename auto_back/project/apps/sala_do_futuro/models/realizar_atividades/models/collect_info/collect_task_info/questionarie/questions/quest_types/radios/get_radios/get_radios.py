from project import types

class GetRadios:
    def __init__(self, page, has_radios_class, radios_alternative_class, actual_quest):
        self.page = page
        self.types = types
        self.has_radios_class = has_radios_class
        self.radios_alternative_class = radios_alternative_class
        self.actual_quest = actual_quest

    def get_alternatives(self):
        try:
            alternatives = []
            alternatives_container = self.actual_quest.locator(f'{self.has_radios_class}')
            alternatives_elements = alternatives_container.locator(f'{self.radios_alternative_class}')

            count = alternatives_elements.count()
            for i in range(count):
                paragraphs = alternatives_elements.nth(i).locator('p').all_text_contents()
                alt_text = ' '.join(paragraphs).strip()
                alternatives.append(alt_text)
            
            return alternatives

        except Exception as e:
            print(f'[{self.types[4]}] Erro ao obter alternativas: {e}')
            return []

