from project import types
import json, os

class CollectInfo:
    def __init__(self, page, 
                component_class = 'h6.css-yq44kw',
                title_activity_class = 'p.css-zscg42',
                user_activity_class = ':nth-match(p.css-dyxuuh, 1)',
                author_activity_class = ':nth-match(p.css-dyxuuh, 2)',
                class_activity_class = ':nth-match(p.css-dyxuuh, 3)',
                expire_activity_class = ':nth-match(p.css-dyxuuh, 4)',
                id_activity_class = ':nth-match(p.css-dyxuuh, 5)'
            ):
        self.page = page
        self.component_class = component_class
        self.title_activity_class = title_activity_class
        self.user_activity_class = user_activity_class
        self.author_activity_class = author_activity_class
        self.class_activity_class = class_activity_class
        self.expire_activity_class = expire_activity_class
        self.id_activity_class = id_activity_class

    def collect_task_info(self):
        print(f'[{types[9]}] Coletando informações da Atividade...\n')
        
        def extract_clean_text(selector):
            return self.page.locator(selector).evaluate(
                '''
                node => {
                    const label = node.querySelector("p");
                    return node.textContent.replace(label?.textContent || "", "").trim();
                }
                '''
            )

        component = self.page.locator(self.component_class).inner_text()
        title_activity = self.page.locator(self.title_activity_class).inner_text()
        user_activity = extract_clean_text(self.user_activity_class)
        author_activity = extract_clean_text(self.author_activity_class)
        class_activity = extract_clean_text(self.class_activity_class)
        expire_activity = extract_clean_text(self.expire_activity_class)
        id_activity = extract_clean_text(self.id_activity_class)

        return component, title_activity, user_activity, author_activity, class_activity, expire_activity, id_activity

    def collect_quest(self):
        pass

    def collect_text(self):
        pass

    def collect_img(self):
        pass

    def collect_mp4(self):
        pass

    def collect_json(self, component, id_activity):
        print(f'[{types[9]}] Vericando se há JSON respostas para essa Atividade...')

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(base_dir, 'data', 'data.json')

        if not os.path.exists(json_path):
            print(f'[{types[4]}] O arquivo JSON não foi encontrado em {json_path}')
            return

        with open(json_path, 'r') as file:
            data = json.load(file)

        if component not in data['answers']:
            print(f'[{types[4]}] Componente \'{component}\' não encontrado nas respostas.')
            return
        
        component_data = data['answers'][component]
        
        if id_activity in component_data:
            print(f'[{types[7]}] Encontrado \'Respostas Salvas\' para essa Atividade!')

            resposta = input(f'[{types[0]}] Usar \'data.json\'? (Y/n): ').strip().upper()
            if resposta == '': 
                resposta = 'Y'
            
            if resposta == 'Y':
                print('Usando \'data.json\'')
            else:
                print('\'data.json\' não será utilizado')
        else:
            print(f'[{types[4]}] Nenhum \'Respostas Salvas\' encontrado para essa Atividade!')

    def run_collect(self):
        pass

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