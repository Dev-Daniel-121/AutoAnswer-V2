from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_section.collect_section import CollectSection
from project import types

class Text:
    def __init__(self, page, information_card_class):
        self.page = page
        self.information_card_class = information_card_class

    def get_informative_content(self, card):
        content = {
            'video': {},
            'image': {},
            'gif': {}
        }

        try:
            video_elements = card.query_selector_all('div.css-pcbmqt iframe')
            for idx, iframe in enumerate(video_elements):
                src = iframe.get_attribute('src')
                if src:
                    content['video'][str(idx)] = {'type': 'video', 'src': src}
        except Exception as e:
            print(f'[{types[4]}] Erro ao coletar vídeos: {e}')

        try:
            img_elements = card.query_selector_all('img')
            for idx, img in enumerate(img_elements):
                src = img.get_attribute('src')
                if src and src.endswith('.gif'):
                    content['gif'][str(idx)] = {'type': 'gif', 'src': src}
                elif src:
                    content['image'][str(idx)] = {'type': 'image', 'src': src}
        except Exception as e:
            print(f'[{types[4]}] Erro ao coletar imagens: {e}')

        return content

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
                'informative_content': self.get_informative_content(card),
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
