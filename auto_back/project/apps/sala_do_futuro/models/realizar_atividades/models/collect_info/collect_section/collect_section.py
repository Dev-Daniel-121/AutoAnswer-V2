from project import types

class CollectSection:
    def __init__(self, page, elem_section_class, time_wait):
        self.page = page
        self.elem_section_class = elem_section_class
        self.time_wait = time_wait

    def get_section_for_element(self, target_element):
        try:
            if not self.elem_section_class:
                return ''

            locator = self.page.locator(self.elem_section_class)

            locator.first.wait_for(state='attached', timeout=self.time_wait)

            count = locator.count()
            if count == 0:
                return ''

            section_elements = locator
            target_box = target_element.bounding_box()

            if not target_box:
                print(f'[{types[4]}] Bounding box do elemento alvo não encontrada.')
                return ''

            closest_section = None
            closest_section_top = float('-inf')

            for i in range(count):
                section = section_elements.nth(i)
                section_box = section.bounding_box()

                if section_box and section_box['y'] <= target_box['y']:
                    if section_box['y'] > closest_section_top:
                        closest_section_top = section_box['y']
                        closest_section = section

            return closest_section.text_content() if closest_section else ''

        except Exception as e:
            print(f'[{types[8]}] Não encontrada seção do elemento: {e}')
            return ''
