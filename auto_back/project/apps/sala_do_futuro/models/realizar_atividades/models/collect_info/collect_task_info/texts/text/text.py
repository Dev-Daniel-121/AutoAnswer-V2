from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info import CollectSection, CollectMedia
from project import types

class Text:
    def __init__(self, page, information_card_class, elem_section_class):
        self.page = page
        self.information_card_class = information_card_class
        self.elem_section_class = elem_section_class

    def get_content(self, card):
        try:
            return card.text_content() or ''
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter informações do texto: {e}')
            return ''

    def run(self):
        results = {}
        try:
            cards = self.page.query_selector_all(f'.{self.information_card_class}')
        except Exception as e:
            print(f'[{types[4]}] Erro ao localizar os cards: {e}')
            return results

        section_finder = None
        use_sections = False
        section_selector = self.elem_section_class

        try:
            locator = self.page.locator(section_selector)
            if locator.count() > 0:
                use_sections = True
                section_finder = CollectSection(
                    page=self.page,
                    elem_section_class=section_selector,
                    time_wait=250
                )
        except Exception as e:
            print(f'[{types[4]}] Erro ao verificar seções: {e}')

        for idx, card in enumerate(cards):
            section_text = ''
            if use_sections and section_finder:
                try:
                    section_text = section_finder.get_section_for_element(card)
                except Exception as e:
                    print(f'[{types[4]}] Erro ao obter seção do card: {e}')

            results[str(idx)] = {
                'informative_content': CollectMedia(card, video_media_selector='div.css-pcbmqt iframe', img_media_selector='img').extract_media(),
                'secao': section_text or '',
                'conteudo': self.get_content(card),
                'num_de_erros': '',
                'tipos_de_erros': ['', '', ''],
                'logs_de_erros': {
                    '0': {
                        'tipo': '',
                        'detalhes': '',
                        'questao': '',
                        'timestamp': ''
                    }
                }
            }

        return results
