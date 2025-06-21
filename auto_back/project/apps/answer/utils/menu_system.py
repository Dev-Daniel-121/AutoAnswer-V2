from project.apps.answer import IAHandler
from datetime import datetime, timezone
from project import Display, LogType
import math, textwrap

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

    def parse_utc(self, dt_str):
        return datetime.strptime(dt_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)

    def get_prompt_status(self, prompt_data, now=None):
        if now is None:
            now = datetime.now(timezone.utc)
        
        usage_history = prompt_data.get('usage_history', [])
        created_at_str = prompt_data.get('created_at')

        performance = prompt_data.get('results', {}).get('summary', {}).get('performance', {})
        total_answers = performance.get('total_answers', 0)
        correct = performance.get('correct', 0)
        wrong = performance.get('wrong', 0)

        accuracy = (correct / total_answers) * 100 if total_answers > 0 else None

        if usage_history:
            last_used_str = max(use.get('used_at') for use in usage_history if use.get('used_at'))
            last_used = self.parse_utc(last_used_str)
            days_since_last_use = (now - last_used).days
            if days_since_last_use < 0:
                return 'ERRO: data de uso futura'
        else:
            days_since_last_use = None

        if created_at_str:
            created_at = self.parse_utc(created_at_str)
            days_since_creation = (now - created_at).days
        else:
            days_since_creation = None

        history = prompt_data.get('history', [])
        if history:
            last_update_str = max(entry.get('updated_at') for entry in history if entry.get('updated_at'))
            updated_at = self.parse_utc(last_update_str)
            days_since_update = (now - updated_at).days
        else:
            days_since_update = None

        uso_mes = sum(
            1 for use in usage_history
            if (parsed := self.parse_utc(use.get('used_at'))).month == now.month and parsed.year == now.year
        )

        if total_answers == 0 and usage_history == [] and days_since_creation is not None and days_since_creation <= 30:
            return f'Novo - criado há {days_since_creation} dias'
        
        if total_answers == 0 and not usage_history:
            return 'Nunca Usado - 0x nesse mês'

        if uso_mes <= 2:
            return f'Pouco Usado - {uso_mes}x nesse mês'

        if days_since_last_use is not None:
            if days_since_last_use < 0:
                return 'ERRO: data de uso futura'
            elif days_since_last_use <= 15:
                return f'Uso Recente - último uso há {days_since_last_use} dias'
            else:
                return f'Uso antigo - último uso há {days_since_last_use} dias'

        if days_since_update is not None and days_since_update <= 7:
            return f'Atualizado - atualizado há {days_since_update} dias'

        if accuracy is None:
            return f'Sem dados de acerto'

        if accuracy >= 80:
            if uso_mes > 20:
                return f'Em Destaque - alta frequência e alta precisão ({int(accuracy)}% acertos)'
            else:
                return f'Alta Precisão - {int(accuracy)}% acertos'
        elif accuracy < 50:
            if uso_mes > 10:
                return f'Revisar - alta frequência com baixa precisão ({int(accuracy)}% acertos)'
            else:
                return f'Baixa Precisão - {int(accuracy)}% acertos'
        else:
            return f'Estável - {int(accuracy)}% acertos'


    def show_prompts(self, ia_escolhida):
        options = Display('', f'Prompt {ia_escolhida.nome}', answer=False, user=self.user, title_quest='', clear_enabled=True)
        options.display()
        print()

        prompts = ia_escolhida.get_prompts()
        if not prompts:
            print(f'[{LogType.ERROR}] Nenhum prompt encontrado para IA: {ia_escolhida.nome}')
            return

        now = datetime.now(timezone.utc)

        ranking_data = []
        for prompt_data in prompts:
            prompt_id = prompt_data.get('id')
            performance = prompt_data.get('results', {}).get('summary', {}).get('performance', {})
            corrects = performance.get('correct', 0)
            total_answers = performance.get('total_answers', 0)
            score = (corrects / total_answers) * 0.7 + math.log10(total_answers + 1) * 0.3 if total_answers > 0 else 0
            ranking_data.append((prompt_id, score))

        ranking_data.sort(key=lambda x: x[1], reverse=True)
        prompt_rank_map = {pid: idx + 1 for idx, (pid, _) in enumerate(ranking_data)}
        total_prompts = len(ranking_data)

        for idx, prompt_data in enumerate(prompts, start=1):
            prompt_id = prompt_data.get('id', f'prompt_{idx}')
            title = prompt_data.get('title', 'Sem título')
            prompt_text = prompt_data.get('text', 'Sem conteúdo')

            performance = prompt_data.get('results', {}).get('summary', {}).get('performance', {})
            components = prompt_data.get('results', {}).get('summary', {}).get('components', {})

            a = performance.get('total_answers', 0)
            c = performance.get('correct', 0)
            w = performance.get('wrong', 0)

            def format_num(val):
                return f'+{val}' if val > 9_999_999 else str(val)

            stats_str = f'A: {format_num(a)} C: {format_num(c)} W: {format_num(w)}'
            prefix = f'[{idx}]. '
            max_line_width = 52
            max_title_len = max_line_width - len(prefix) - len(stats_str) - 1
            trimmed_title = title if len(title) <= max_title_len else title[:max_title_len - 3] + '...'

            header = f'{prefix}{trimmed_title:<{max_title_len}} {stats_str}'
            print(header[:max_line_width])

            max_chars = 208
            truncated = prompt_text[:205] + '...' if len(prompt_text) > max_chars else prompt_text
            lines = textwrap.wrap(truncated, width=max_line_width)
            for line in lines:
                print(line)
            if not lines:
                print()

            sorted_comps = sorted(components.items(), key=lambda x: x[1], reverse=True)[:3]
            total_comp = sum(v for _, v in sorted_comps)
            tendencia_data = [
                f'{name[:4].capitalize()}: {int((value / total_comp) * 100)}%' if total_comp > 0 else f'{name[:4].capitalize()}: --%'
                for name, value in sorted_comps
            ]
            tendencia_str = '  '.join(tendencia_data)
            print(f'\nTENDÊNCIA:{' ' * (max_line_width - len('TENDÊNCIA:') - len(tendencia_str))}{tendencia_str}')

            status_str = self.get_prompt_status(prompt_data, now)
            rank_pos = prompt_rank_map.get(prompt_id, '?')
            space_len = max_line_width - len(status_str) - len(f'Rank: {rank_pos}º de {total_prompts}')
            space_len = max(space_len, 1)
            print(f'{status_str}{' ' * space_len}Rank: {rank_pos}º de {total_prompts}\n')

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
