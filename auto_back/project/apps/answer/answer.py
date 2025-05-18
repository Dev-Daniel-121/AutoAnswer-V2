from project.apps.answer import MenuSystem

class Answer:
    def __init__(self, user):
        self.user = user

    def run(self):
        if self.open_in_new_terminal:
            self.open_in_new_terminal_func()
        else:
            menu = MenuSystem(user=self.user)
            menu.menu()


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

1. Grok
2. ChatGPT
3. Voltar

~~~~~~ Prompt {IA} (USER) ~~~~~~

[1]. NOME DO PROMPT             A: 100 C: 70% W: 30%
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlk...

TENDENCIA:           Mate: 50%  Hist: 45%  Mult: 20%
ANSWERS: +99.999 - CORRECTS: +9.999 - WRONGS: +9.999

[2]. NOME DO PROMPT            A: 100% C: 70% W: 30%
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlk...

TENDENCIA:           ----: --%  ----: --%  ----: --%
ANSWERS: 000.000 - CORRECTS: 00.000 - WRONGS: 00.000

[3]. NOME DO PROMPT            A: 100% C: 70% W: 30%
asdf asdf asf asdf asfd asdf asdf asdf asdf asdf as-
fasdfasdfa asdfas asd fasdf asdfasdf asdfasdf çlk...

TENDENCIA:        Quim: 010%  Biol: 004%  Reda: 001%
ANSWERS: 100 - CORRECTS: 70 - WRONGS: 30

[Task] Escolha apenas 1 prompt: 

~~~~~~ Working - CollectAutoGUI - {IA} (USER) ~~~~~~

Etapa 1 de 5 - TÍTULO DA ETAPA

Duração:
Total    5s
Retante  0s

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
