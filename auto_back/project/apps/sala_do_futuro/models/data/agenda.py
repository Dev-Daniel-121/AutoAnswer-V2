class Agenda:
    def __init__(self, page, row_class, day_class, day_of_the_week_class, day_content_class):
        self.page = page
        self.row_class = row_class
        self.day_class = day_class
        self.day_of_the_week_class = day_of_the_week_class
        self.day_content_class = day_content_class

    def agenda(self):
        rows = self.page.locator(self.row_class).all()
        
        agenda_data = []

        for row in rows:
            day = row.locator(f':nth-match({self.day_class}, 1)').text_content()
            day_of_the_week = row.locator(f':nth-match({self.day_of_the_week_class}, 1)').text_content()
            day_content = row.locator(f':nth-match({self.day_content_class}, 1)').text_content()

            if len(day_content) > 48:
                day_content = day_content[:48] + "..."

            agenda_data.append((day, day_of_the_week, day_content))

        return agenda_data

    def run(self):
        print('Agenda')
        agenda_data = self.agenda()
        
        for day, day_of_the_week, day_content in agenda_data:
            print(f'{day} - {day_of_the_week} \t[{day_content}]')