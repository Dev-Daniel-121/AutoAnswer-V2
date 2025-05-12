from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_tarefas.card_types import CardInfo, CardQuests
from project import LogType

class CollectTarefas:
    def __init__(self, page):
        self.page = page
        self.card_info = CardInfo(page=self.page, info_card_class='div.css-1mpla7o')
        self.card_quests = CardQuests(page=self.page, quests_card_class='div.css-b200pa')

    def run(self):
        num_card_info = self.card_info.count()
        radios, checkboxes, right_wrong, total, unknown_type_indexes = self.card_quests.count_quest_types()

        print(f'[{LogType.INFO}] Número de Cards Informativos: {num_card_info}')
        print(f'[{LogType.INFO}] Número de questões: {total}\n')

        print(f'[{LogType.INFO}] Tipos de questões encontradas: ')
        if radios > 0: print(f'[{LogType.INFO}]   Radios: {radios}')
        if checkboxes > 0: print(f'[{LogType.INFO}]   Checkbox: {checkboxes}')
        if right_wrong > 0: print(f'[{LogType.INFO}]   Right Wrong: {right_wrong}')

        if unknown_type_indexes != []:
            print(f'\n[{LogType.INFO}] Questões desconhecidas encontradas: ')
            print(f'[{LogType.INFO}]    Questões {unknown_type_indexes}')

        print('')