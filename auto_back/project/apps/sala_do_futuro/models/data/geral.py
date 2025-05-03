from project import types

class Geral:
    def __init__(
            self, page, values_class, 
            pendencias_box_class, pendencias_box_close_class, 
            pendencias_p_elements, pendencias_b_elements):
        self.page = page
        self.values_class = values_class
        self.pendencias_box_class = pendencias_box_class
        self.pendencias_box_close_class = pendencias_box_close_class
        self.pendencias_p_elements = pendencias_p_elements
        self.pendencias_b_elements = pendencias_b_elements

    def pendencias(self):
        try:
            self.page.wait_for_selector(self.pendencias_box_class, state='visible', timeout=5000)

            pendencias_box = self.page.locator(self.pendencias_box_class)
            pendencias_box.click()

            self.page.wait_for_timeout(1000)

            pendencias_tarefas, pendencias_redacoes, pendencias_provas, pendencias_total = self.pendencias_activities()

            pendencias_box_close = self.page.locator(self.pendencias_box_close_class)
            pendencias_box_close.click()

            return {
                'pendencias_tarefas': pendencias_tarefas,
                'pendencias_redacoes': pendencias_redacoes,
                'pendencias_provas': pendencias_provas,
                'pendencias_total': pendencias_total
            }
        except Exception as e:
            print(f'[{types[4]}] Tempo excedido ao tentar interagir com a caixa de pendências.')
            return None

    def pendencias_activities(self):
        try:
            self.page.wait_for_selector(self.pendencias_p_elements, timeout=5000)

            pendencias_tarefas = int(self.page.locator(f':nth-match({self.pendencias_p_elements} > {self.pendencias_b_elements}, 1)').inner_text())
            pendencias_redacoes = int(self.page.locator(f':nth-match({self.pendencias_p_elements} > {self.pendencias_b_elements}, 2)').inner_text())
            pendencias_provas = int(self.page.locator(f':nth-match({self.pendencias_p_elements} > {self.pendencias_b_elements}, 3)').inner_text())
            pendencias_total = pendencias_tarefas + pendencias_redacoes + pendencias_provas

            return pendencias_tarefas, pendencias_redacoes, pendencias_provas, pendencias_total
        except Exception as e:
            print(f'[{types[4]}] Erro ao extrair pendências: {e}')
            return 0, 0, 0, 0

    def mensagem_nao_lida(self):
        try:
            mensagem_nao_lida_num = self.page.locator(f':nth-match({self.values_class}, 2)').inner_text()
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter o número de mensagems não lidas: {e}')

        return mensagem_nao_lida_num

    def faltas(self):
        try:
            faltas_num = self.page.locator(f':nth-match({self.values_class}, 3)').inner_text()

            if faltas_num == '''Boletim

e Avaliações''':
                return 'Sem faltas'
            
        except Exception as e:
            print(f'[{types[4]}] Erro ao o número de faltas: {e}')

        return faltas_num

    def boletim(self, faltas_num):
        try:
            if faltas_num == 'Sem faltas': 
                boletim_num = self.page.locator(f':nth-match({self.values_class}, 3)').inner_text()
            else: 
                boletim_num = self.page.locator(f':nth-match({self.values_class}, 4)').inner_text()
        except Exception as e:
            print(f'[{types[4]}] Erro ao obter o status do boletim: {e}')
            
        return 'Indisponível' if boletim_num == 'Boletim' else 'Boletim Disponível para Visualização'

    def run(self):
        pendencias = self.pendencias()
        if pendencias:
            pendencias_tarefas = pendencias['pendencias_tarefas']
            pendencias_redacoes = pendencias['pendencias_redacoes']
            pendencias_provas = pendencias['pendencias_provas']
            pendencias_total = pendencias['pendencias_total']
        else:
            pendencias_tarefas = pendencias_redacoes = pendencias_provas = pendencias_total = 0

        mensagem_nao_lida_num = self.mensagem_nao_lida()
        faltas_num = self.faltas()
        boletim_num = self.boletim(faltas_num=faltas_num)

        print(f'\n~~~~~~ Geral ~~~~~~\n')
        print(f'[{types[9]}] Pendências: \t\t{pendencias_total}')
        print(f'[{types[9]}]    Tarefas: \t\t{pendencias_tarefas}')
        print(f'[{types[9]}]    Redação: \t\t{pendencias_redacoes}')
        print(f'[{types[9]}]    Provas:  \t\t{pendencias_provas}')
        print(f'[{types[9]}] Faltas: \t\t\t{faltas_num}')
        print(f'[{types[9]}] Mensagem não lida: \t{mensagem_nao_lida_num}')
        print(f'[{types[9]}] Boletim: \t\t{boletim_num}')

        return {
            'pendencias_total': pendencias_total,
            'tarefas': pendencias_tarefas,
            'redacoes': pendencias_redacoes,
            'provas': pendencias_provas,
            'mensagem_nao_lida': mensagem_nao_lida_num,
            'faltas': faltas_num,
            'boletim': boletim_num
        }