from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_section.collect_section import CollectSection
from project import types
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_media.collect_media import CollectMedia

class Text:
    def __init__(self, page, information_card_class):
        self.page = page
        self.information_card_class = information_card_class

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
        
        try:
            section_finder = CollectSection(page=self.page, elem_section_class='div.css-8atqhb h2', time_wait=250)
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter seção: {e}')
            return

        for idx, card in enumerate(cards):
            section_text = section_finder.get_section_for_element(card)

            results[str(idx)] = {
                'informative_content': CollectMedia(card, video_media='div.css-pcbmqt iframe', img_media='img').extract_media(),
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
