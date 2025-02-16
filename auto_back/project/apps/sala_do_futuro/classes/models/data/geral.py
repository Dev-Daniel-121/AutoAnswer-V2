class Geral:
    def __init__(self, page, values_class):
        self.page = page
        self.values_class = values_class

    def pendencias(self):
        pendencias_value = self.page.locator(f':nth-match({self.values_class}, 1)').text_content()
        pendencias = self.page.locator(f':nth-match({self.values_class}, 1)')
        pendencias.click()

        pendencias_values_p = self.page.query_selector_all('p.css-1f9zvnk')
        pendencias_values = []

        for pendencias_value_p in pendencias_values_p:
            pendencias_value_b = pendencias_value_p.query_selector('b')
            if pendencias_value_b:
                pendencias_values.append(pendencias_value_b.text_content())
            else:
                pendencias_values.append(None)

        return pendencias_value, pendencias_values
    
    def mensagem_nao_lida(self):
        mensagem_nao_lida_num = self.page.locator(f':nth-match({self.values_class}, 2)').text_content()
        return mensagem_nao_lida_num
    
    def faltas(self):
        faltas_num = self.page.locator(f':nth-match({self.values_class}, 3)').text_content()
        return faltas_num
    
    def boletim(self):
        boletim_num = self.page.locator(f':nth-match({self.values_class}, 4)').text_content()
        return 'Indisponível' if boletim_num == 'Boletim' else boletim_num

    def run(self):
        pendencias_value, pendencias_values = self.pendencias()
        mensagem_nao_lida_num = self.mensagem_nao_lida()
        faltas_num = self.faltas()
        boletim_num = self.boletim()

        print(f'Geral')
        print(f'Pendências: \t\t{pendencias_value}')
        print(f'\tTarefas: \t{pendencias_values[0]}')
        print(f'\tRedação: \t{pendencias_values[1]}')
        print(f'\tProvas: \t{pendencias_values[2]}')
        print(f'Faltas: \t\t{faltas_num}')
        print(f'Mensagem não lida: \t\t{mensagem_nao_lida_num}')
        print(f'Boletim: \t\t{boletim_num}')

        return {
            'pendencias_value': pendencias_value,
            'pendencias_values': pendencias_values,
            'mensagem_nao_lida': mensagem_nao_lida_num,
            'faltas': faltas_num,
            'boletim': boletim_num
        }