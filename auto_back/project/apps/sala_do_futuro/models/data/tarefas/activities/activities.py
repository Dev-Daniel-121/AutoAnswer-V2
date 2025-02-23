from project import types
from collections import defaultdict

class Activities:
    def __init__(self, page):
        self.page = page

    def total_activities(self):
        return self.page.locator('div.css-fm7u1u').all()

    def get_component_name(self, materia):
        return materia.locator('p.css-9kams2').inner_text()

    def get_component_day(self, materia):
        return materia.locator('p.css-1d78sd9').inner_text()

    def get_component_date(self, materia):
        dates = materia.locator('p.css-1gwkyaz').all()
        if len(dates) >= 2:
            return dates[0].inner_text(), dates[1].inner_text()
        return None, None

    def run_aFazer(self):
        atividades = self.total_activities()
        if not atividades:
            print('Não há lições disponíveis.')
            return {}, {}
        
        materias_count = defaultdict(int)
        datas = defaultdict(list)

        for materia in atividades:
            nome = self.get_component_name(materia)
            materias_count[nome] += 1
            datas[nome].append(self.get_component_day(materia))

        for nome in datas:
            datas[nome].sort()

        return materias_count, datas

    def run_expiradas(self):
        atividades = self.total_activities()
        if not atividades:
            print(f'[{types[8]}] Não há lições disponíveis.')
            return {}, {}
        
        materias_count = defaultdict(int)
        datas = defaultdict(list)

        for materia in atividades:
            nome = self.get_component_name(materia)
            materias_count[nome] += 1
            start_date, end_date = self.get_component_date(materia)
            if start_date and end_date:
                datas[nome].append((start_date, end_date))

        for nome in datas:
            datas[nome].sort(key=lambda x: (x[0], x[1]))

        return materias_count, datas

    def run_entregues(self):
        atividades = self.total_activities()
        if not atividades:
            print(f'[{types[8]}] Não há lições disponíveis.')
            return {}
        
        materias_count = defaultdict(int)

        for materia in atividades:
            nome = self.get_component_name(materia)
            materias_count[nome] += 1

        return materias_count

    def display(self, status, materias_count, datas=None):
        if not materias_count:
            print(f'[{types[8]}] Nenhuma atividade encontrada.')
            return
        
        for nome, quantidade in materias_count.items():
            if status == 'A fazer':
                print(f'{nome}: [{quantidade}] ({datas[nome][0]})')
            elif status == 'Expiradas':
                data_inicial, data_final = datas[nome][-1]
                print(f'{nome}: [{quantidade}] ({data_inicial} - {data_final})')
            else:
                print(f'{nome}: [{quantidade}]')

    def run(self, status):
        if status == 'A fazer':
            materias_count, datas = self.run_aFazer()
            self.display(status, materias_count, datas)
        elif status == 'Expiradas':
            materias_count, datas = self.run_expiradas()
            self.display(status, materias_count, datas)
        elif status == 'Entregues':
            materias_count = self.run_entregues()
            self.display(status, materias_count)
