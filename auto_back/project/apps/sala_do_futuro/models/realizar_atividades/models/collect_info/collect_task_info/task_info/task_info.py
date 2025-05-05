from project import types
import re

class TaskInfo:
    def __init__(
            self, page, activity_status,
            activity_type_class,
            material_activity_class,
            activity_title_class
        ):
        self.activity_status = activity_status
        self.activity_type_class = activity_type_class
        self.material_activity_class = material_activity_class
        self.activity_title_class = activity_title_class
        self.types = types
        self.page = page

    def get_status_activity(self):
        status_activity = self.activity_status
        return status_activity
    
    def get_auto_activity_id(self):
        pass

    def get_activity_type(self):
        try:
            activity_type = self.page.locator(f'{self.activity_type_class}').text_content()
            return activity_type
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter tipo da atividade: {e}')
            return
    
    def get_material_activity(self):
        try:
            material_activity = self.page.locator(f'{self.material_activity_class}').text_content()
            subject_name = re.sub(r'\s*-\s*\d+$', '', material_activity.strip())
            
            return subject_name
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter matéria da atividade: {e}')
            return

    def get_activity_title(self):
        try:
            activity_title = self.page.locator(f'{self.activity_title_class}').text_content()
            return activity_title
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter título da atividade: {e}')
            return

    def get_activity_infos(self):
        try:
            elements = self.page.query_selector_all('p.css-dyxuuh')

            extracted_texts = []

            for el in elements:
                full_text = (el.text_content()).strip()

                inner_p = el.query_selector_all('p')

                for inner in inner_p:
                    inner_text = (inner.text_content()).strip()
                    full_text = full_text.replace(inner_text, '').strip()

                extracted_texts.append(full_text)

            user, author, class_school, expires_in, site_activity_id = extracted_texts[:5]

            return user, author, class_school, expires_in, site_activity_id

        except Exception as e:
            print(f'Erro ao obter cabeçalho da atividade: {e}')
            return

    def run(self):
        task_info = {}

        status_activity = self.get_status_activity()
        activity_type = self.get_activity_type()
        material_activity = self.get_material_activity()
        activity_title = self.get_activity_title()
        user, author, class_school, expires_in, site_activity_id = self.get_activity_infos()
        auto_activity_id = self.get_auto_activity_id()

        # print(f'Status Atividade: {status_activity}')
        # print(f'Tipo Atividade: {activity_type}')
        # print(f'Matéria: {material_activity}')
        # print(f'Título Atividade: {activity_title}')
        # print(f'Usuário: {user}')
        # print(f'Autor: {author}')
        # print(f'Turma: {class_school}')
        # print(f'Expira em: {expires_in}')
        # print(f'ID Atividade Site: {site_activity_id}\n')

        task_info = {
            # 'task_info': {
            'status_activity': status_activity or '',
            'site_activity_id': site_activity_id or '',
            'auto_activity_id': auto_activity_id or '',
            'activity_type': activity_type or '',
            'material_activity': material_activity or '',
            'activity_title': activity_title or '',
            'user': user or '',
            'author': author or '',
            'class_school': class_school or '',
            'expires_in': expires_in or '',
            'time_spent': '',
            'draft': '',
            'submitted': '',
            'question_types': {}
            # }
        }

        return task_info