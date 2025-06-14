from project.apps.sala_do_futuro.models.data.tarefas import Sections
from project.apps.sala_do_futuro.config import status
from collections import defaultdict
from project import LogType

class Activities:
    def __init__(self, page, total_activities_class='', get_component_name_class='', get_component_day_class='', get_component_date_class=''):
        self.page = page
        self.status = status
        self.sections = Sections(page=self.page, sections_status_class=':nth-match(div.css-39ukww, 2)')
        self.total_activities_class = total_activities_class
        self.get_component_name_class = get_component_name_class
        self.get_component_day_class = get_component_day_class
        self.get_component_date_class = get_component_date_class

    def wait_for_element(self, selector, timeout=5):
        try:
            self.page.wait_for_selector(selector, timeout=timeout * 1000)
            return True
        except Exception:
            print(f'[{LogType.INFO}] Elemento {selector} não encontrado após {timeout} segundos.')
            return False
    
    def enter_activity(self, activity_class='', btn_enter_activity_class=''):
        try:
            activity = self.page.locator(f'{activity_class}')
            btn_enter_activity = self.page.locator(f'{btn_enter_activity_class}')

            if activity.is_visible():
                activity.hover()

                btn_enter_activity.wait_for(state='visible')
                btn_enter_activity.click()
            else:
                print(f'[{LogType.ERROR}] Atividade não está visível: {activity_class}')

        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao tentar entrar na atividade: {e}')

    def total_activities(self):
        if not self.wait_for_element(self.total_activities_class):
            return []

        try:
            total_activities = self.page.locator(self.total_activities_class).all()
            return total_activities if total_activities else []
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter total de atividades: {e}')
            return []
        
    def get_component_name(self, materia):
        get_component_name_class = self.get_component_name_class

        try:
            name = materia.locator(get_component_name_class).inner_text()
            return name if name else 'Desconhecido'
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter o nome da atividade: {e}')
            return 'Desconhecido'

    def get_component_day(self, materia):
        get_component_day_class = self.get_component_day_class

        try:
            day = materia.locator(get_component_day_class).inner_text()
            return day if day else 'Data não disponível'
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter o dia de expiração da atividade: {e}')
            return 'Data não disponível'


    def get_component_date(self, materia):
        get_component_date_class = self.get_component_date_class
        try:
            dates = materia.locator(get_component_date_class).all()
            if len(dates) >= 2:
                return dates[0].inner_text(), dates[1].inner_text()
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter o Dia Inicial - Dia Final da atividade: {e}')
        
        return 'Data inicial não disponível', 'Data final não disponível'

    def run_aFazer(self):
        atividades = self.total_activities()
        if not atividades:
            print(f'[{LogType.INFO}] Não há lições disponíveis.')
            return {}, {}

        materias_count = defaultdict(int)
        datas = defaultdict(list)

        for materia in atividades:
            nome = self.get_component_name(materia)
            materias_count[nome] += 1
            dia = self.get_component_day(materia)

            if dia and dia != 'Data não disponível':
                datas[nome].append(dia)

        for nome in datas:
            datas[nome].sort()

        return materias_count, datas

    def run_expiradas(self):
        atividades = self.total_activities()
        if not atividades:
            print(f'[{LogType.INFO}] Não há lições disponíveis.')
            return {}, {}

        materias_count = defaultdict(int)
        datas = defaultdict(list)

        for materia in atividades:
            nome = self.get_component_name(materia)
            materias_count[nome] += 1
            start_date, end_date = self.get_component_date(materia)
            datas[nome].append((start_date, end_date))

        for nome in datas:
            datas[nome].sort(key=lambda x: (x[0], x[1]))

        return materias_count, datas

    def run_entregues(self):
        atividades = self.total_activities()
        if not atividades:
            print(f'[{LogType.INFO}] Não há lições disponíveis.')
            return {}

        materias_count = defaultdict(int)
        for materia in atividades:
            nome = self.get_component_name(materia)
            materias_count[nome] += 1

        return materias_count

    def display(self, status, materias_count, datas=None):
        if not materias_count:
            print(f'[{LogType.INFO}] Nenhuma atividade encontrada.')
            return

        for nome, quantidade in materias_count.items():
            if status == f'{self.status[0]}':
                if datas[nome]:
                    print(f'[{LogType.INFO}] {nome}: {quantidade} ({datas[nome][0]})')
                else:
                    print(f'[{LogType.INFO}] {nome}: {quantidade} (Sem data disponível)')
            elif status == f'{self.status[2]}':
                data_inicial, data_final = datas[nome][-1]
                print(f'[{LogType.INFO}] {nome}: {quantidade} ({data_inicial} - {data_final})')
            else:
                print(f'[{LogType.INFO}] {nome}: {quantidade}')

    def run(self):
        status = self.sections.sections_status()
        if status == f'{self.status[0]}':
            materias_count, datas = self.run_aFazer()
            self.display(status, materias_count, datas)
        elif status == f'{self.status[2]}':
            materias_count, datas = self.run_expiradas()
            self.display(status, materias_count, datas)
        elif status == f'{self.status[1]}':
            materias_count = self.run_entregues()
            self.display(status, materias_count)
            