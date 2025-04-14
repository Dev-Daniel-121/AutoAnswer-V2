from project import types

class CollectInfo:
    def __init__(self, page, 
                btn_open_collapse_class = "button.css-13ponum"
            ):
        self.page = page
        self.btn_open_collapse_class = btn_open_collapse_class

    def collect_task_info(self):
        open_collapse = self.page.locator(f'{self.btn_open_collapse_class}')
        open_collapse.click()

        """
        
        Essa função tem que verificar:
            Se (dentro da div.css-1jyoemj há a div.css-a0y2e3) {
                open_collapse = self.page.locator(f'{btn_open_collapse_class}').click() # Clica para Abrir o Collapse
                ID activity
            }

        """

    def collect_quest(self):
        pass

    def collect_text(self):
        pass

    def collect_img(self):
        pass

    def collect_mp4(self):
        pass

    def run_collect(self):
        print(f'[{types[9]}] Coletando informações da Lição...')
        input('\n\nHey OH!\n\n')

    def run(self):
        pass

"""

    Infomações
    * Quantas questões (Count div.css-b200pa)
    * Quantos Textos (Count div.css-1mpla7o > p)
    * Quantas Imgs (Count div.css-1mpla7o > p > img)
    * Quantos Mp4 (Count div.css-1mpla7o > div.css-pcbmqt)
    ? Quantos Gifs

    Coletar informações das questões

    ? Radio
        Tipo de Questão                 (div.css-b200pa > div.MuiRadioGroup-root)
        Questão atual                   (div.css-b200pa > p.css-m576f2 > b)
        Obrigatória                     (div.css-b200pa > p.css-sz9ejl)
        Pontuação Possivel da Questão   (div.css-b200pa > p.css-1wgaj9w)
        Titulo da questão               (div.css-b200pa > div.css-1a4wlpz > p)
        Alternativas                    (div.css-b200pa > div.css-9whsf3)
        Conteúdo da Alternativa         (div.css-b200pa > div.css-9whsf3 > div.css-1p78i1z > p)
        Resposta                        (div.css-b200pa > div.css-9whsf3 > input.css-1m9pwf3).click

    ? Right Wrong
        Tipo de Questão                 (div.css-b200pa > div.css-70qvj9)
        Questão atual                   (div.css-b200pa > p.css-m576f2 > b)
        Obrigatória                     (div.css-b200pa > p.css-sz9ejl)
        Pontuação Possivel da Questão   (div.css-b200pa > p.css-1wgaj9w)
        Titulo da questão               (div.css-b200pa > div.css-1a4wlpz > p)
        Alternativas                    (div.css-b200pa > div.css-70qvj9)
        Título da Alternativa           (div.css-b200pa > div.css-70qvj9 > div.css-8atqhb > p)
        Título da opção da Alternativa  (div.css-b200pa > div.css-70qvj9 > label.css-geqbjm > span.css-1h7gjlg)
        Resposta                        (div.css-b200pa > div.css-70qvj9 > label.css-geqbjm > input.css-1m9pwf3).click

"""