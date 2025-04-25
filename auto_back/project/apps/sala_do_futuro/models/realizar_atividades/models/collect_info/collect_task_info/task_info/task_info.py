from project import types

class TaskInfo:
    def __init__(self, page, activity_status):
        self.activity_status = activity_status
        self.types = types
        self.page = page

    def get_status_activity(self):
        status_activity = self.activity_status
        return status_activity
    
    def get_auto_activity_id(self):
        pass

    def get_activity_type(self):
        try:
            activity_type_class = ':nth-match(li.MuiBreadcrumbs-li, 2)'
            activity_type = self.page.locator(f'{activity_type_class}').text_content()
            return activity_type
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter tipo da atividade: {e}')
            return
    
    def get_material_activity(self):
        try:
            material_activity_class = 'h6.css-yq44kw'
            material_activity = self.page.locator(f'{material_activity_class}').text_content()
            return material_activity
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter matéria da atividade: {e}')
            return

    def get_activity_title(self):
        try:
            activity_title_class = 'p.css-zscg42'
            activity_title = self.page.locator(f'{activity_title_class}').text_content()
            return activity_title
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter título da atividade: {e}')
            return

    def get_activity_infos(self):
        try:
            elements = self.page.query_selector_all("p.css-dyxuuh")

            extracted_texts = []

            for el in elements:
                full_text = (el.text_content()).strip()

                inner_p = el.query_selector_all("p")

                for inner in inner_p:
                    inner_text = (inner.text_content()).strip()
                    full_text = full_text.replace(inner_text, "").strip()

                extracted_texts.append(full_text)

            user, author, class_school, expires_in, site_activity_id = extracted_texts[:5]

            return user, author, class_school, expires_in, site_activity_id

        except Exception as e:
            print(f'Erro ao obter cabeçalho da atividade: {e}')
            return

    def run(self):
        status_activity = self.get_status_activity()
        activity_type = self.get_activity_type()
        material_activity = self.get_material_activity()
        activity_title = self.get_activity_title()
        user, author, class_school, expires_in, site_activity_id = self.get_activity_infos()

        print(f'Status Atividade: {status_activity}')
        print(f'Tipo Atividade: {activity_type}')
        print(f'Matéria: {material_activity}')
        print(f'Título Atividade: {activity_title}')
        print(f'Usuário: {user}')
        print(f'Autor: {author}')
        print(f'Turma: {class_school}')
        print(f'Expira em: {expires_in}')
        print(f'ID Atividade Site: {site_activity_id}\n')
