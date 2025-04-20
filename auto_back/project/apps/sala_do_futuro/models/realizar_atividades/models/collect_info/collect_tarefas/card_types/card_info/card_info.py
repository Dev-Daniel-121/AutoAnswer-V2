from project import types

class CardInfo:
    def __init__(self, page, info_card_class):
        self.page = page
        self.info_card_class = info_card_class

    def count(self):
        try:
            elements = self.page.query_selector_all(self.info_card_class)
            return len(elements)
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter contagem dos Card Informativos: {e}')
            return
