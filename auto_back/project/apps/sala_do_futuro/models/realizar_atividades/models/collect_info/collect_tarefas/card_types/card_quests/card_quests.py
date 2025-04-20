from project import types

class CardQuests:
    def __init__(self, page, quests_card_class):
        self.page = page
        self.quests_card_class = quests_card_class

    def count_quest_types(self):
        try:
            elements = self.page.query_selector_all(self.quests_card_class)

            radios = 0
            checkboxes = 0
            right_wrong = 0
            unknown_type_indexes = []

            for idx, element in enumerate(elements):
                has_radio = element.query_selector('div.css-1h7anqn')
                has_checkbox = element.query_selector('div.css-107ow6p')
                has_right_wrong = element.query_selector('div.css-70qvj9')

                if has_radio:
                    radios += 1
                if has_checkbox:
                    checkboxes += 1
                if has_right_wrong:
                    right_wrong += 1

                if not (has_radio or has_checkbox or has_right_wrong):
                    unknown_type_indexes.append(idx + 1)

            return radios, checkboxes, right_wrong, len(elements), unknown_type_indexes

        except Exception as e:
            print(f'[{types[4]}] Erro ao contar os tipos de questões: {e}')
            return
