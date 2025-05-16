from project import Display, LogType

class Answer:
    def __init__(self, user):
        self.user = user

    def run(self):
        options_data = [(LogType.OPTION, 'Start'), (LogType.OPTION, 'Settings'), (LogType.OPTION, 'Sair')]
        options = Display(options_data, 'Answer', answer=True, user=self.user, title_quest='', clear_enabled=False)
        user_choice = options.display()

        if user_choice == 1:
            print('Start')
            input('al')
        elif user_choice == 2:
            print('Settings')
            input('al')
        elif user_choice == 3:
            return
        else:
            print(f'[{LogType.ERROR}] Opção inválida, tente novamente.')



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

~~~~~~ Start ~~~~~~

Etapa 1 de 5 - TÍTULO DA ETAPA

Duração: 5s
Duração restante: 0s

Atalhos:
[a] Aumenta o tempo em {5s}             [d] Diminui o tempo em {5s}
[c] Cancela a Automação                 [s] Pausa e Despausa a Automação
[f] Sair da Automação CollectAutoGUI

Progresso: ( ==================== ) 100%

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
