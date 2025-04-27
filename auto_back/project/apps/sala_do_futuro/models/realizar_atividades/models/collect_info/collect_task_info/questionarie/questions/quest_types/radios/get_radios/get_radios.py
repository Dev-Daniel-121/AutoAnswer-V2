from project import types

class GetRadios:
    def __init__(
            self, page,
            alternative_class='div.css-10zfeld',
        ):
        self.page = page
        self.types = types
        self.alternative_class = alternative_class,
        self.quest_container = self.page.locator(':nth-match(div.css-b200pa, 1)')

    def get_alternatives(self):
        try:
            alternatives = []
            elements = self.quest_container.query_selector_all(self.alternative_class)
            for el in elements:
                p = el.query_selector("div.css-1p78i1z p")
                if p:
                    text = p.inner_text().strip()
                    alternatives.append(text)
            return alternatives
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter alternatvias da questão: {e}')
            input('Precione')
            return
