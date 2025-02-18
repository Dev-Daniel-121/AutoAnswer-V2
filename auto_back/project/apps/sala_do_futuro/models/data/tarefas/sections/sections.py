class Sections:
    def __init__(self, page, container_sec_class, text_sec_class, component_sec_class):
        self.page = page
        self.container_sec_class = container_sec_class
        self.text_sec_class = text_sec_class
        self.component_sec_class = component_sec_class

    def run(self):
        container_sec = self.page.locator(self.container_sec_class).all()
        content_sec_class = []

        for item in container_sec:
            text = item.locator(self.text_sec_class).text_content()
            content_sec_class.append(text)

        component_sec = self.page.locator(self.component_sec_class)
        componente = component_sec.get_attribute('value')

        print(f'Turmas: {content_sec_class[0]} | Status: {content_sec_class[1]} | Componente: {componente}')