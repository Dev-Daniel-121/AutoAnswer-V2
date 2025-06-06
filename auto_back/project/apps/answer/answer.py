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

1. Grok       (Em funcionamento - pronto para ajudar)
2. ChatGPT    (Em funcionamento - pronto para ajudar)
3. DeepSeak   (Fora de serviço - Sistema temporariamente inativo)
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

Etapa 1 de 5- TÍTULO DA ETAPA

Duração:
Total:  195s  -  Retante:  0s
Acrés: +999s  -  Descrés: -999s

Atalhos:
[a] Aumenta o tempo em {5s}             [d] Diminui o tempo em {5s}
[c] Cancela a Automação                 [s] Pausa e Despausa a Automação
[f] Sair da Automação CollectAutoGUI

Progresso:
Etapa Atual  ( ======================================== ) 100% - 10s
Geral        ( ======================================== ) 100% - 60s

~~~~~~ Settings ~~~~~~

1. Etapas da Automação          <- Exibir as Etapas da Automação
2. Localização dos circulos     <- Mostra a localização nos Circulos na Tela para se o User quise, ele alterar
3. Voltar                       <- Volta para Menu Principal

~~~~~~ Etapas da Automação ~~~~~~

[1]. Entrar no Chrome
[2]. Pesquisar por https://{IA}
[3]. Usar {PROMPT} na IA
    [3.1]. Passar MÍdia para {IA}
[4]. Coletar Resposta

1. Voltar
[Answser] 

~~~~~~ Localização dos circullos ~~~~~~

1. Coleta de Media
2. Coleta de Resposta
3. Voltar

~~~~~~ Localização dos circullos (Search) ~~~~~~

* [1]. (x: 00, y: 00)
  [2]. (x: 00, y: 00)
  [3]. (x: 00, y: 00)

Mova os circulospar o Lugares desejados (O '*' mostra o circulo atual que você está movendo, o número é a ordem que eles irão ser acionados)

1. Voltar
[Answser] 

~~~~~~ Localização dos circullos (Media) ~~~~~~

* [1]. (x: 00, y: 00)
  [2]. (x: 00, y: 00)
  [3]. (x: 00, y: 00)
  [4]. (x: 00, y: 00)
  [5]. (x: 00, y: 00)

Mova os circulospar o Lugares desejados (O '*' mostra o circulo atual que você está movendo, o número é a ordem que eles irão ser acionados)

1. Voltar
[Answser] 

"""
