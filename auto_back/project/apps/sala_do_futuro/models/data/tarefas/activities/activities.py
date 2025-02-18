class Activities:
    def __init__(
            self, page,
            container_activities_class, box_activities_class, activities_component_class, activities_dates_class):
        self.page = page
        self.container_activities_class = container_activities_class
        self.box_activities_class = box_activities_class
        self.activities_component_class = activities_component_class
        self.activities_dates_class = activities_dates_class

    def get_activities_component(self):
        container_activities = self.page.locator(self.container_activities_class).all()
        activities_component = []

        for box in container_activities:
            component = box.locator(self.activities_component_class).text_content()
            activities_component.append(component)

        return activities_component

    def get_activities_num(self):
        activities_component = self.get_activities_component()
        from collections import defaultdict

        materia_count = defaultdict(int)
        for materia in activities_component:
            materia_count[materia] += 1

        return materia_count

    def get_activities_date(self):
        from collections import defaultdict
        container_activities = self.page.locator(self.container_activities_class).all()
        materia_dates = defaultdict(list)

        for box in container_activities:
            materia = box.locator(self.activities_component_class).text_content()
            date = box.locator(self.activities_dates_class).text_content()
            if date:
                materia_dates[materia].append(date)

        from datetime import datetime

        materia_closest_date = {}
        for materia, dates in materia_dates.items():
            closest_date = min(
                [datetime.strptime(date, "%d/%m/%Y") for date in dates],
                default=None
            )
            if closest_date:
                materia_closest_date[materia] = closest_date.strftime("%d/%m/%Y")

        return materia_closest_date

    def run(self, exibir_datas=True):
        materia_count = self.get_activities_num()
        materia_closest_date = self.get_activities_date()

        print("Atividades por Matéria:")
        for materia, count in materia_count.items():
            if exibir_datas and materia in materia_closest_date:
                print(f"{materia}: \t{count} (Data mais próxima: {materia_closest_date[materia]})")
            else:
                print(f"{materia}: \t{count}")