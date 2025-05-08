from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info import CollectMedia
from project import types

class GetRadios:
    def __init__(self, page, has_radios_class, radios_alternative_class, actual_quest, video_media_selector, img_media_selector):
        self.page = page
        self.types = types
        self.has_radios_class = has_radios_class
        self.radios_alternative_class = radios_alternative_class
        self.actual_quest = actual_quest
        self.video_media_selector = video_media_selector
        self.img_media_selector = img_media_selector

    def get_alternatives(self):
        try:
            alternatives = []
            alternatives_container = self.actual_quest.locator(f'{self.has_radios_class}')
            alternatives_elements = alternatives_container.locator(f'{self.radios_alternative_class}')

            count = alternatives_elements.count()
            for i in range(count):
                alternative_element = alternatives_elements.nth(i)

                # Coleta texto
                alt_text = self._extract_text_from_alternative(alternative_element)

                # Coleta mídia
                alt_media = self._extract_media_from_alternative(alternative_element)

                alternatives.append({
                    'text': alt_text,
                    'media': alt_media
                })

            return alternatives

        except Exception as e:
            print(f'[{self.types[4]}] Erro ao obter alternativas: {e}')
            return []

    def _extract_text_from_alternative(self, alternative_element):
        paragraphs = alternative_element.locator('p').all_text_contents()
        return ' '.join(paragraphs).strip()

    def _extract_media_from_alternative(self, alternative_element):
        media_collector = CollectMedia(alternative_element, self.video_media_selector, self.img_media_selector)
        return media_collector.extract_media()
