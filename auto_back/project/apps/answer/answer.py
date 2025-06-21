from project.apps.answer import MenuSystem
import subprocess, sys, pyautogui
from project import LogType

class Answer:
    def __init__(self, user, open_in_new_terminal=False):  
        self.user = user
        self.open_in_new_terminal = open_in_new_terminal
        self.close_terminal_flag = open_in_new_terminal

    def run(self):
        if self.open_in_new_terminal:
            print(f'[{LogType.INFO}] Abrindo novo terminal...')
            self.process = self.open_in_new_terminal_func()
        else:
            print(f'[{LogType.INFO}] Executando o menu normalmente...')
            menu = MenuSystem(user=self.user, close_terminal_flag=self.close_terminal_flag)
            menu.menu()

    def open_in_new_terminal_func(self):
        try:
            if sys.platform == 'win32':
                command = f'python -c "from project.apps.answer import MenuSystem; MenuSystem(user=\'{self.user}\', close_terminal_flag={self.close_terminal_flag}).menu()"'
                return subprocess.Popen(f'start cmd /k {command}', shell=True)
            elif sys.platform == 'darwin':
                command = f'osascript -e \'tell application "Terminal" to do script "python3 -c \"from project.apps.answer import MenuSystem; MenuSystem(user=\"{self.user}\", close_terminal_flag={self.close_terminal_flag}).menu()\""\''
                return subprocess.Popen(command, shell=True)
            elif sys.platform in ['linux', 'linux2']:
                command = f'gnome-terminal -- bash -c "python3 -c \"from project.apps.answer import MenuSystem; MenuSystem(user=\'{self.user}\', close_terminal_flag={self.close_terminal_flag}).menu()\""'
                return subprocess.Popen(command, shell=True)
            else:
                print(f'[{LogType.WARNING}] Sistema operacional não suportado para abrir terminal automaticamente.')
                return None
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao tentar abrir o terminal: {e}')
            return None


    def close_terminal(self):
        try:
            if sys.platform == 'win32':
                pyautogui.hotkey('alt', 'f4')
                print(f'[{LogType.INFO}] Fechando terminal no Windows...')
            elif sys.platform == 'darwin':
                osascript_command = 'osascript -e "tell application \\"Terminal\\" to quit"'
                subprocess.run(osascript_command, shell=True)
                print(f'[{LogType.INFO}] Fechando terminal no macOS...')
            elif sys.platform in ['linux', 'linux2']:
                if self.process:
                    self.process.terminate()
                    print(f'[{LogType.INFO}] Fechando terminal no Linux...')
                else:
                    print(f'[{LogType.WARNING}] Processo do terminal não encontrado.')
            else:
                print(f'[{LogType.WARNING}] Sistema operacional não suportado para fechar terminal automaticamente.')
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao tentar fechar o terminal: {e}')


"""

? O QUE ELA DEVE FAZER

^   Abrir um novo  Terminal
^   Realizar as Etapas

& ETAPAS

~   1. Exibir Menu Inicial
~   2. Com base no que o User selecionar no Menu Inicial realizar
~   3. Iniciar a automação
~   4. Terminal INFOS
~       4.1. Exibir Etapa atual da automação
~       4.2. Exibir Duração da etap
~       4.3. Exibir Duração restante 
~       4.4. Exibir barra de progresso
~       4.5. Exibir Atalhos

todo ATALHOS

^   1. 'a' Acrescenta {5s}                  // Esse é o valor em segundo recebido pela class (Ele pode ser alterado)
^   2. 'd' Diminui {5s}                     // Esse é o valor em segundo recebido pela class (Ele pode ser alterado)
^   3. 'c' Cancelar a Automação             // Cancela a Automação e volta para o Menu Inicial
^   4. 's' Pausa e Despausa a Automação     // Pausa e Despausa a Automação
^   5. 'f' Sair do CollectAutoGUI           // Saí da Automação CollectAutoGUI

----------------------------------------------------------------------------------------------------

~~~~~~ CollectAutoGUI (USER) ~~~~~~

1. Start        <- Inicia Automação
2. Settings     <- Abri configurações
3. Sair         <- Sair da Automação

~~~~~~ IA (USER) ~~~~~~

1. Grok (Em funcionamento - pronto para ajudar)
2. ChatGPT (Em funcionamento - pronto para ajudar)
3. DeepSeak (Fora de serviço - Sistema temporariamente inativo)
3. Voltar

~~~~~~ Prompt {IA} (USER) ~~~~~~

----------------------------------------------------
[1]. NOME DO PROMPT               A: 100 C: 70 W: 30
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlklj-
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlklj-
asdf gasdgasdf ashasdçlk jasçkldf asçdlkfjaçlsdka...

TENDENCIA:              Mat: 50%  His: 45%  Mul: 20%
ANSWERS: +99.999 - CORRECTS: +9.999 - WRONGS: +9.999

[2]. NOME DO PROMPT...       A: ---- C: ---- W: ----
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlklj-
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
asdf gasdgasdf ashasdçlk jasçkldf asçdlkfjaçlsdka...

TENDENCIA:           ----: --%  ----: --%  ----: --%
ANSWERS: 00.0  -   CORRECTS: 00.0   -   WRONGS: 00.0

[3]. NOME DO PROMPT               A: 100 C: 70 W: 30
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlklj-
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
asdf gasdgasdf ashasdçlk jasçkldf asçdlkfjaçlsdka...

TENDENCIA:                Qui: 10%  Bio: 4%  Red: 1%
ANSWERS: 100    -    CORRECTS: 70    -    WRONGS: 30

[30]. NOME DO PROMPT MUITO LO...   A: -- C: -- W: --
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlklj-
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
asdf gasdgasdf ashasdçlk jasçkldf asçdlkfjaçlsdka...

TENDENCIA:           ----: --%  ----: --%  ----: --%
ANSWERS: 00.0  -   CORRECTS: 00.0   -   WRONGS: 00.0
 
[Task] Escolha apenas 1 prompt: 
[Answer] 1

[Info] Executando prompt {USER_CHOICE}

~~~~~~ Working - CollectAutoGUI - {IA} (USER) ~~~~~~

Etapa 1 de 5 - TÍTULO DA ETAPA

Duração:
Total:  195s  -  Retante:  0s
Acrés: +999s  -  Decrésc: -999s

Atalhos:
[a] Aumenta o tempo em {5s}             [d] Diminui o tempo em {5s}
[c] Cancela a Automação                 [s] Pausa e Despausa a Automação
[f] Sair da Automação CollectAutoGUI

Progresso:
Etapa Atual  ( ======================================== ) 100% - 10s
Geral        ( ======================================== ) 100% - 60s

~~~~~~ Settings ~~~~~~

1. IA              <- Configuração das IA
2. Automações      <- Exibir as Etapas da Automação
4. Voltar

~~~~~~ Automações ~~~~~~

1. Coleta de respostas (ChatGpt - AutoGui)
1. Coleta de respostas (Grok - AutoGui)
2. Voltar

~~~~~~ Coleta de respostas ~~~~~~

1. Test
2. Settings
3. Voltar

~~~~~~ Coleta de respostas (Settings) ~~~~~~

1. Etapas da automação
2. Nome
3. Voltar

~~~~~~ Coleta de respostas (Settings) ~~~~~~

[1]. Entrar no Chrome
[2]. Pesquisar por https://{IA}
[3]. Usar {PROMPT} na IA
    [3.1]. Passar MÍdia para {IA}
[4]. Coletar Resposta

------------------------------

~~~~~~ ETAPAS DA AUTOMAÇÃO ~~~~~~

1. Adicionar Etapa
2. Editar Etapa
3. Deletar Etapa
4. Voltar

[Task] Digite a opção: 
[Answer] 1

[Task] Será uma Etapa ou Subetapa de uma etapa existente? ([N] - nova etapa, [S] - subetapa)
[Answer] N

[Info] Digite o nome da nova etapa: 
[Info] Coloque a URL ou o PATH para uma img que irá auxiliar você a configurar a ação (OPCIONAL): 

~~~~~~ AÇÕES COM O MOUSE ~~~~~~
1. Click (esquerdo, direito ou meio)
2. Clique duplo
3. Arrasta o mouse até a posição especificada
4. Rola a tela para cima ou para baixo

~~~~~~ AÇÕES COM O TECLADO ~~~~~~
5. Digita texto como se fosse teclado
6. Pressiona uma tecla (ex: 'enter', 'tab', 'ctrl')
7. Pressiona ou solta uma tecla (útil para atalhos)
8. Pressiona uma combinação de teclas

[Info] Selecione a ação que será usada (Digite mais de 1 ação separada por ',' para mais de 1 ação): 

~~~~~~ AÇÕES SELECIONADAS ~~~~~~

* [1]. MOUSE (x: 00, y: 00)
  [2]. TECLADO ()

[Info] Mova o circulo da ação [1] para a posição que a ação será executada

[Info] Digite a(s) tecla(s) que serão precionadas

[Info] Digite a ordem com que as ações serão realizadas (deixe em branco se a ordem de AÇÕES SELECIONADAS está correto)

[Success] Etapa [ID] NOME ETEPA adicionada com Sucesso!

===

[Task] Será uma Etapa ou Subetapa de uma etapa existente? ([N] - nova etapa, [S] - subetapa)
[Answer] S

[Task] Digite o ID da etapa ou subetapa que será adiciona essa nova subetapa
[USA O MESMO PROCESSO DE CRIAR, troque apenas etapa para subetapa]

---

[Task] Digite a opção: 
[Answer] 2

[Task] Digite os IDs das etapas ou subetapas separadas por ',' que seram atualizados

[USA O MESMO PROCESSO DE CRIAR porém para atualizar]

---

[Task] Digite a opção: 
[Answer] 3

[Task] Digite os IDs das etapas separadas por ',' que serão deletadas

~~~~~~ IA ~~~~~~

1. ChatGPT - Operação parcial
2. Grok - Operando normalmente

~~~~~~ ChatGpt ~~~~~~

1. Prompts
2. Métodos
3. Voltar

~~~~~~ ChatGPT - Métodos ~~~~~~

1. ChatGPT - AutoGUI: Operando normalmente
2. ChatGPT - AutoStealph: Indisponível

~~~~~~ ChatGPT - AutoGUI ~~~~~~

Descrição

[MSG] Precione ENTER para voltar...

~~~~~~ ChatGPT - Prompts ~~~~~~

[1]. NOME DO PROMPT               A: 100 C: 70 W: 30
[2]. NOME DO PROMPT               A: 100 C: 70 W: 30
[3]. NOME DO PROMPT               A: 100 C: 70 W: 30
[4]. NOME DO PROMPT               A: 100 C: 70 W: 30

------------------------------

~~~~~~ PROMPT ~~~~~~

1. Adicionar Prompt
2. Editar Prompt
3. Deletar Prompt
4. Visualizar informações completa
5. Voltar

[Task] Digite a opção: 
[Answer] 1

[Info] Digite o nome do Prompt
[Info] Digite o prompt

[Success] Prompt [ID] NOME PROMPT adicionado com Sucesso!

---

[Task] Digite a opção: 
[Answer] 2

[Task] Digite os IDs dos prompts separadas por ',' que seram atualizados
2

[USA O MESMO PROCESSO DE CRIAR porém para atualizar]

---

[Task] Digite a opção: 
[Answer] 3

[Task] Digite os IDs das etapas separadas por ',' que serão deletadas

"""
