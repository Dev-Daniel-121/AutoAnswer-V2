from project.apps.answer import IAHandler
from project import Display, LogType
import textwrap

class MenuSystem:
    def __init__(self, user, close_terminal_flag=False):
        self.user = user
        self.close_terminal_flag = close_terminal_flag
        self.ia_handler = IAHandler()

    def menu(self):
        options_data = [
            (LogType.OPTION, 'Start'),
            (LogType.OPTION, 'Settings'),
            (LogType.OPTION, 'Sair')
        ]
        options = Display(options_data, 'Answer', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if user_choice == 1:
            self.start()
        elif user_choice == 2:
            self.settings()
        elif user_choice == 3:
            self.close()
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')

    def start(self):
        self.ias = self.ia_handler.get_ias()
        options_data = []

        for ia in self.ias:
            status_geral, _ = ia.get_status_detalhado()
            options_data.append((LogType.OPTION, status_geral))

        options_data.append((LogType.OPTION, 'Voltar'))

        options = Display(options_data, 'IAs Disponíveis', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if user_choice == len(self.ias) + 1:
            self.menu()
        elif 1 <= user_choice <= len(self.ias):
            ia_escolhida = self.ias[user_choice - 1]
            self.show_metodos(ia_escolhida)
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')

    def show_metodos(self, ia_escolhida):
        _, status_por_metodo = ia_escolhida.get_status_detalhado()

        options_data = [(LogType.OPTION, status) for status in status_por_metodo]
        options_data.append((LogType.OPTION, 'Voltar'))

        options = Display(options_data, f'{ia_escolhida.nome} - Métodos', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if 1 <= user_choice <= len(status_por_metodo):
            metodo_escolhido = list(ia_escolhida.metodos.keys())[user_choice - 1]
            print(f'[{LogType.INFO}] {metodo_escolhido} selecionado')
            input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')
            self.show_prompts(ia_escolhida)

            self.show_metodos(ia_escolhida)
        elif user_choice == len(status_por_metodo) + 1:
            self.start()
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')

    def show_prompts(self, ia_escolhida):
        options = Display('', f'Prompt {ia_escolhida.nome}', answer=False, user=self.user, title_quest='', clear_enabled=True)
        options.display()

        print()

        prompts = ia_escolhida.get_prompts()
        if not prompts:
            print(f'[{LogType.ERROR}] Nenhum prompt encontrado para IA: {ia_escolhida.nome}')
            return

        for idx, (prompt_id, prompt_data) in enumerate(prompts.items(), start=1):
            title = prompt_data.get('title', 'Sem título')
            prompt_text = prompt_data.get('prompt', 'Sem conteúdo')

            performance = prompt_data.get('results', {}).get('general', {}).get('performance', {})
            components = prompt_data.get('results', {}).get('general', {}).get('components', {})

            a = performance.get('answers', 0)
            c = performance.get('corrects', 0)
            w = performance.get('wrongs', 0)

            def format_num(val):
                return f'+{val}' if val > 9_999_999 else str(val)

            a_str = f'A: {format_num(a)}'
            c_str = f'C: {format_num(c)}'
            w_str = f'W: {format_num(w)}'
            stats_str = f'{a_str} {c_str} {w_str}'

            prefix = f'[{idx}]. '
            max_line_width = 52
            prefix_len = len(prefix)
            stats_len = len(stats_str)

            max_title_len = max_line_width - prefix_len - stats_len - 1 
            trimmed_title = title if len(title) <= max_title_len else title[:max_title_len - 3] + '...'

            header = f'{prefix}{trimmed_title:<{max_title_len}} {stats_str}'
            print(header[:52])

            max_chars = 208
            truncated = prompt_text[:205] + '...' if len(prompt_text) > max_chars else prompt_text
            lines = textwrap.wrap(truncated, width=52)

            for line in lines:
                print(line)

            if not lines:
                print()

            sorted_comps = sorted(components.items(), key=lambda x: x[1], reverse=True)[:3]
            total = sum(v for _, v in sorted_comps)
            tendencia_data = [
                f'{name[:4].capitalize()}: {int((value / total) * 100)}%' if total > 0 else f'{name[:4].capitalize()}: --%'
                for name, value in sorted_comps
            ]
            tendencia_str = '  '.join(tendencia_data)

            left = 'TENDÊNCIA:'
            space = 52 - len(left) - len(tendencia_str)
            space = max(space, 1)

            print(f'\n{left}{' ' * space}{tendencia_str}\n')

        choice = input(f'[{LogType.TASK}] Escolha apenas 1 prompt: ')
        if choice.isdigit():
            print(f'\n[{LogType.INFO}] Executando prompt {choice}')
        else:
            print(f'\n[{LogType.ERROR}] Entrada inválida.')
        
    def settings(self):
        options_data = [
            (LogType.OPTION, 'IA'),
            (LogType.OPTION, 'Etapas da Automação'),
            (LogType.OPTION, 'Localização dos circulos'),
            (LogType.OPTION, 'Voltar')
        ]
        options = Display(options_data, 'Settings', answer=True, user=self.user, title_quest='', clear_enabled=True)
        user_choice = options.display()

        if user_choice == 1:
            print(f'[{LogType.INFO}] IA')
            input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')
        elif user_choice == 2:
            print(f'[{LogType.INFO}] Etapas da Automação')
            input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')
        elif user_choice == 3:
            print(f'[{LogType.INFO}] Localização dos Circulos')
            input(f'[{LogType.MSG}] Pressione qualquer tecla para continuar...')
        elif user_choice == 4:
            self.menu()
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')

    def close(self):
        print(f'[{LogType.WARNING}] Finalizando processos...\n')
        print(f'[{LogType.WARNING}] Fechando terminal\n')
        if self.close_terminal_flag:
            from project import Answer
            answer = Answer(user=self.user)
            answer.close_terminal()
