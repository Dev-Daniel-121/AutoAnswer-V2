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
        print(f'[{types[9]}] Coletando informações da Lição...\n')

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
            print(f'[{types[4]}] Componente "{component}" não encontrado nas respostas.')
            return
        
        component_data = data['answers'][component]
        
        if id_activity in component_data:
            print(f'[{types[7]}] Encontrado \'Respostas Salvas\' para essa Atividade!')

            resposta = input(f'[{types[0]}] Usar "data.json"? (Y/n): ').strip().upper()
            if resposta == '': 
                resposta = 'Y'
            
            if resposta == 'Y':
                print('Usando "data.json"')
            else:
                print('"data.json" não será utilizado')
        else:
            print(f'[{types[4]}] Nenhum \'Respostas Salvas\' encontrado para essa Atividade!.')

        """
        
        Quero que essa função vá para '../data/' onde se encontra 1 arquivo JSON (data.json), por enquanto esse arquivo está como testes

        O programa deve entrar no Json na aba de answers validar o "component" recebido e verficar se é 1 desses 3 tipos possíveis de "component"
        
            1. Tarefa
            2. Redacao
            3. Prova

        Se for "TAREFA" ele deve ir para a aba tarefa no Json e verificar cada id tarefa se for igual ao id_activity recebido pela função
            Se ele achar o id da atividade no JSON:
                print(f'[{types[7]}] Encontrado JSON respostas para essa Atividade!')

                resposta = input(f'[{types[0]}] Usar "nomeDoArqJson.json"? (Y/n): ').strip().upper()
                if resposta == '': resposta = 'Y'
                    
                if resposta == 'Y':
                    print('Usando "nomeDoArqJson.json"')
                else:
                    print('"nomeDoArqJson.json" não será ultilizado')
            Se ele não achar o id da atividade no JSON:
                print(f'[{types[4]}] Nenhum JSON resposta existente para essa Atividade.')
        
        Se for "REDACAO" ele deve ir para a aba tarefa no Json e verificar cada id tarefa se for igual ao id_activity recebido pela função
            Se ele achar o id da atividade no JSON:
                print(f'[{types[7]}] Encontrado JSON respostas para essa Atividade!')

                resposta = input(f'[{types[0]}] Usar "nomeDoArqJson.json"? (Y/n): ').strip().upper()
                if resposta == '': resposta = 'Y'
                    
                if resposta == 'Y':
                    print('Usando "nomeDoArqJson.json"')
                else:
                    print('"nomeDoArqJson.json" não será ultilizado')
            Se ele não achar o id da atividade no JSON:
                print(f'[{types[4]}] Nenhum JSON resposta existente para essa Atividade.')
        
        Se for "PROVA" ele deve ir para a aba tarefa no Json e verificar cada id tarefa se for igual ao id_activity recebido pela função
            Se ele achar o id da atividade no JSON:
                print(f'[{types[7]}] Encontrado JSON respostas para essa Atividade!')

                resposta = input(f'[{types[0]}] Usar "nomeDoArqJson.json"? (Y/n): ').strip().upper()
                if resposta == '': resposta = 'Y'
                    
                if resposta == 'Y':
                    print('Usando "nomeDoArqJson.json"')
                else:
                    print('"nomeDoArqJson.json" não será ultilizado')
            Se ele não achar o id da atividade no JSON:
                print(f'[{types[4]}] Nenhum JSON resposta existente para essa Atividade.')

        Esse é o JSON

        "answers": {
            "tarefas": {
                "66120137": { Id da tarefa
                    "quest_1": {
                        "time": {
                            "day": "02/05/2025",
                            "start_time": "12:00",
                            "end_time": "12:05"
                        },
                        "quest_type": "Radio",
                        "quest": "Escolha alteranativa correta",
                        "alters": {
                            "A": "Alternativa A",
                            "B": "Alternativa B",
                            "C": "Alternativa C",
                            "D": "Alternativa D"
                        },
                        "answer": {
                            "A": "Alternativa A"
                        }
                    },
                    "quest_2": {
                        "time": {
                            "day": "02/05/2025",
                            "start_time": "12:00",
                            "end_time": "12:05"
                        },
                        "quest_type": "Check",
                        "quest": "Escolha alteranativa correta",
                        "alters": {
                            "A": "Alternativa A",
                            "B": "Alternativa B",
                            "C": "Alternativa C",
                            "D": "Alternativa D"
                        },
                        "answer": {
                            "A": "Alternativa A",
                            "C": "Alternativa C",
                            "D": "Alternativa D"
                        }
                    }
                },
                "66120135" {
                    ...
                }
            },
            "redacao": {
                Para redação e prova é o mesmo esquema
            },
            "prova": {
                Para redação e prova é o mesmo esquema
            }
        }

        """

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