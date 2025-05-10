class GeneralText:
    def __init__(self, page: dict):
        self.page = page

    def run(self):
        secoes = {}
        tipos_de_erros = {}
        logs_de_erros = {}
        num_de_erros = 0

        for idx, key in enumerate(self.page):
            item = self.page[key]

            secoes[str(idx)] = item.get('secao', '')

            erros = item.get('tipos_de_erros', ['', '', ''])
            for e_idx, erro in enumerate(erros):
                tipos_de_erros[str(e_idx)] = erro

            for log_key, log_val in item.get('logs_de_erros', {}).items():
                logs_de_erros[log_key] = log_val

            if isinstance(item.get('num_de_erros', ''), int):
                num_de_erros += item['num_de_erros']

        result = {
            'geral': {
                'secoes': secoes,
                'num_de_erros': num_de_erros,
                'tipos_de_erros': tipos_de_erros,
                'logs_de_erros': logs_de_erros
            }
        }

        return result
