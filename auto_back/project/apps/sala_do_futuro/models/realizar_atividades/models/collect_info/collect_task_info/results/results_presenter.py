from project import LogType, Display

class ResultsPresenter:
    def __init__(self, data, user, material_activity, activity_id):
        self.data = data
        self.user = user
        self.display = Display
        self.activity_id = activity_id
        self.material_activity = material_activity
        self.questions = data['tarefas'][user][user]
        self.categorized = self._classify_answers()

    def _classify_answers(self):
        correct_answers = {}
        wrong_answers = {}
        answered_by_user = {}
        answered_by_guess = {}

        for key, content in self.questions.items():
            if not key.isdigit():
                continue

            quest_info = content.get('quest_info', {})
            quest_data = content.get('quest', {})

            answer = quest_data.get('answer', '')
            answer_key = quest_data.get('answer_key', '')
            user_guess = quest_info.get('user_guess', False)
            answered = quest_info.get('answered_by_user', False)

            if answer and answer_key:
                if answer == answer_key:
                    correct_answers[key] = content
                else:
                    wrong_answers[key] = content

            if answered:
                answered_by_user[key] = content

            if user_guess:
                answered_by_guess[key] = content

        return {
            'Respostas Corretas': correct_answers,
            'Respostas Erradas': wrong_answers,
            'Respondida pelo Usuário': answered_by_user,
            'Respondida por Chutes (Sorteio)': answered_by_guess
        }

    def display_results(self):
        options = self.display(data='', title=f'{self.material_activity} - {self.activity_id}', answer=False, user=f'{self.user}', title_quest='')
        options.display()

        for category, questions in self.categorized.items():
            print(f'\n~~~~~~ {category} - [{len(questions)}] ~~~~~~')
            self._print_group(questions)

    def calculate_score_spaces(self, info, quest):
        score = str(info.get('score', ''))
        answer = str(quest.get('answer', ''))

        len_score = len(score)
        len_answer = len(answer)

        if len_score < 4:
            space_score = len_score - 10
            return space_score
        elif len_score == 4:
            return
        elif len_score > 4 and len_score <= len_answer:
            more_characters = len_score - 4
            space_score = len_answer - more_characters
            return space_score
        elif len_score > len_answer:
            characters_to_remove = len_score - len_answer
            new_score = '+' + score[(characters_to_remove + 2):]
            return new_score

    def _print_group(self, questions, fixed_space=3):
        previous_section = None

        for num_quest, content in sorted(questions.items(), key=lambda x: int(x[0])):
            quest = content.get('quest', {})
            info = content.get('quest_info', {})
            section = info.get('section', 'Sem Seção')

            if section != previous_section:
                print(f'---- {section}')
                previous_section = section

            space_fixed = ' ' * fixed_space
            space_for_score = self.calculate_score_spaces(info=info, quest=quest)

            if isinstance(space_for_score, str):
                score_value = space_for_score
                score_space = ''
            else:
                score_value = info.get('score', '')
                score_space = ' ' * space_for_score

            print(f'[{LogType.INFO}] Questão {num_quest} - {quest.get('type', '')}')
            print(f'[{LogType.INFO}] Nota: {score_value}{score_space}{space_fixed}Pontos: {info.get('activity_score', '')}')
            print(f'[{LogType.INFO}] Resposta: {quest.get('answer', '')}{space_fixed}Gabarito: {quest.get('answer_key', '')}\n')

'''

Se a quantidade de caracteres do info.get('score', '') for < 4 caracteres:
    return espaço_notas = quantidade de caracteres info.get('score', '') - 10
    
Se a quantidade de caracteres info.get('score', '') for == 4 caracteres:
    return

Se a quantidade de caracteres info.get('score', '') for > 4 caracteres:
    caracteres_a_mais = descobrir quantos caracteres do info.get('score', '') há a mais do que 4
    return espaço_notas = quantidade de caracteres quest.get('answer', '') - caracteres_a_mais

Se a quantidade de caracteres info.get('score', '') for > quantidade de caracteres quest.get('answer', ''):
    caracteres_a_retirar = quantidade de caracteres quest.get('answer', '') - quantidade de caracteres do info.get('score', '')
    retirar quantidade de caracteres_a_retirar + 2 e adicionar '+' no inicio do texto de info.get('score', '')

correct_answers
wrong _answers
answered_by_user
answered_by_guesses


'''

'''

~~~~~~ MATERIA - ID MATERIA (USER) ~~~~~~

   ~~~~~~ Respostas Corretas - [2] ~~~~~~
   ---- Matemática
   [Info] Questão 1 - Radios
   [Info] Nota: 10      Pontos: 10
   [Info] Resposta: B   Gabarito: B

   ---- Portugues
   [Info] Questão 2 - Checkbox
   [Info] Nota: 10            Pontos: 10
   [Info] Resposta: A, B, C   Gabarito: A, B, C

   ~~~~~~ Respostas Erradas - [1] ~~~~~~
   --- Portugues
   [Info] Questão 3 - Checkbox
   [Info] Nota: 5          Pontos: 10
   [Info] Resposta: A, B   Gabarito: B, D

   ~~~~~~ Respondida pelo Usuário - [1] ~~~~~~
   --- Quimica
   [Info] Questão 4 - Checkbox
   [Info] Nota: 5             Pontos: 10
   [Info] Resposta: A, B, C   Gabarito: B

   ~~~~~~ Respondida por Chutes (Sorteio) - [1] ~~~~~~
   --- História
   [Info] Questão 5 - Checkbox
   [Info] Nota: 5             Pontos: 10
   [Info] Resposta: A, B, C   Gabarito: B


[Info] Tempo:
[Info]    Coleta de informações  ( ==                                       ) 5% - 3s
[Info]    Coleta de resposta     (   ============                           ) 30% - s
[Info]    Pondo respostas        (               ====                       ) 10% - s
[Info]    Espera                 (                   ====================== ) 55% - s
[Info]    Total                  ( ======================================== ) 100% - 60s

[Info] Composição e Resultado das Seções:
[Info]    Matemática  ( ========                                 ) 5% - (1/1)
[Info]    Portugues   (         ================                 ) 30% - (1/2)
[Info]    Quimica     (                         ========         ) 10% - (0.5/1)
[Info]    História    (                                 ======== ) 10% - (0.5/1)
[Info]    Total       ( ======================================== ) 100% - (3/5)

[Info] Progresso:
[Info]    Corretas  ( ============================             ) 70% - 7 questões
[Info]     Erradas  (                             ============ ) 30% - 3 questões
[Info]       Total  ( ======================================== ) 100% - 10 questões

'''
