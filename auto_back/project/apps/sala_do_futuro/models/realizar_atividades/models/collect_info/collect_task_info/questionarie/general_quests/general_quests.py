from collections import defaultdict

class GeneralQuests:
    def __init__(self, questionarie_data: dict):
        self.data = questionarie_data

    def run(self):
        general = {
            'activity_score': '',
            'score_acquired': '',
            'number_of_questions': len(self.data),
            'number_of_sections': 0,
            'sections': {},
            'number_of_guesses': '',
            'number_of_user_responses': '',
            'user_feedback': '',
            'difficulty': '',
            'history_of_attempts': {},
            'ia': {
                'ia1': {
                    'overall_performance': '',
                    'questions': [],
                    'suggestions': {
                        '0': '',
                        '1': ''
                    }
                },
                'ia2': {
                    'desempenho_geral': '',
                    'questoes': [],
                    'sugestoes': {
                        '0': '',
                        '1': ''
                    }
                }
            },
            'error_number': '',
            'error_types': ['', '', ''],
            'error_logs': {}
        }

        section_counter = defaultdict(int)

        for idx, item in self.data.items():
            quest_info = item.get('quest_info', {})
            quest = item.get('quest', {})

            section = quest_info.get('section', '').strip()
            if section:
                section_counter[section] += 1

            for e_idx, elog in quest_info.get('error_logs', {}).items():
                general['error_logs'][f'{idx}_{e_idx}'] = {
                    'type': elog.get('type', ''),
                    'details': elog.get('details', ''),
                    'question': elog.get('question', ''),
                    'timestamp': elog.get('timestamp', '')
                }

            for h_idx, attempt in quest_info.get('history_of_attempts', {}).items():
                general['history_of_attempts'][f'{idx}_{h_idx}'] = {
                    'quest': quest.get('statement', ''),
                    'author': attempt.get('author', ''),
                    'result': attempt.get('result', ''),
                    'time': attempt.get('time', '')
                }

            general['ia']['ia1']['questions'].append(quest.get('statement', ''))
            general['ia']['ia2']['questoes'].append(quest.get('statement', ''))

        general['sections'] = dict(section_counter)
        general['number_of_sections'] = len(section_counter)
        general['error_types'] = self._coletar_tipos_de_erro()
        general['error_number'] = len(general['error_logs'])

        resultado = {'general': general}
        resultado.update(self.data)
        return resultado

    def _coletar_tipos_de_erro(self):
        tipos = set()
        for item in self.data.values():
            erros = item.get('quest_info', {}).get('error_types', [])
            tipos.update([e for e in erros if e])
        lista = list(tipos)
        while len(lista) < 3:
            lista.append('')
        return lista[:3]
