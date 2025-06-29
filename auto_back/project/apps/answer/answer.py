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

[1]. Executar Naveagdor(User, url)
        [1]. Executar IA.run()

---

? Navegador (navegador, url, user, anonymous=True/False)
[1]. Validar se o navegar está instalado
    [1]. Caso esteja instalado 
        [1]. Validar se há o perfil com o User
            [1]. Caso sim
                [1]. Iniciar Navegador no Perfil do User e entrar na url
                [2]. Executar is_enter_in_the_page()
            [2]. Caso não
                [1]. Gerar erro
                [2]. Solicitar criação de um perfil ou Fechar Automação
                    [1]. Caso aceita a solicitação
                        [1]. Exectuar create_profile(user)
    [2]. Caso não esteja instalado
        [1]. Gerar Erro
        [2]. Listar Navegadores instalados
        [3]. Solicitar escolha de outro Navegador ou Fechar Automação
    [3]. Caso houver algum problema
        [1]. Executar Reportar Problema? Login

* is_enter_in_the_page()
[1]. Validar se conseguiu entrar na URL
    [1]. Caso tenha dado certo
        [1]. Retornar True
    [1]. Caso tenha dado errado
        [1]. Gerar Erro

* create_profile(user)
[1]. Validar se há arquivo de Login rápido
    [1]. Caso tenha
        [1]. Validar se o User está cadastrado no arquivo de Login rápido
            [1]. Caso esteja cadastrado
                [1]. Executar automação de login com os dados no arquivo de Login rápido
            [2]. Caso não esteja cadastrado
                [1]. Gerar Erro
                [2]. Executar cadastrar usuário
    [2]. Caso não tenha
        [1]. Solicitar Email e Senha do Usuário
        [2]. Executar automação de login

* Automação de login
[1]. Digitar Gmail
    [1]. Validar se deu certo
        [1]. Caso esteja tudo certo
            [1]. Continuar com a automação
        [2]. Caso não funcionar ou der algum erro
            [1]. Executar Reportar Problema
[2]. Digitar Senha
    [1]. Validar se deu certo
        [1]. Caso esteja tudo certo
            [1]. Continuar com a automação
        [2]. Caso não funcionar ou der algum erro
            [1]. Executar Reportar Problema

? ia(ia)
* run(media)
[1]. Validar se há mídia
    [1]. Caso tenha Mídia
        [1]. Executar IA.is_it_possible_to_pass_media()
            [1]. Caso True
                [1]. Usar PROMPT na IA
                [2]. Passar MÍdia para IA
            [2]. Caso False
                [1]. Realizar a automação em outro Perfil
    [2]. Caso não tenha Mídia
        [1]. Usar PROMPT na IA
    [3]. Validar se não deu erro na coleta de resposta
        [1]. Caso a resposta esteja aparecendo normal e esteja tudo completo
            [1]. Coletar Resposta
        [2]. Caso a resposta não esteja aparecendo ou deu algum erro
            [1]. Executar Reportar problema
            [2]. Reinicar a página e passar os dados novamente
[2]. Caso não conseguiu ou der algum erro
    [1]. Executar Reportar Problema

* is_connect(ia)
[1]. Validar se o usuário está conectado na IA
    [1]. Caso esteja conectado
        [1]. Validar se o User conectado é o User correto
            [1]. Caso Sim
                [1]. Continuar com a automação
            [2]. Caso não
                [1]. Executar connect_base(User, disconnect_user=True)
    [2]. Caso não esteja conectado
        [1]. Executar connect_base(User)

* disconnect_base(user_position, exit_position)
[1]. Clicar no user
[2]. Clicar em sair

* connect_base(user, ia, disconnect_user=False, enter_positions, connect_positions)
[2]. Clicar em Entrar
[3]. Clicar em Conectar com LOGIN
    [1]. Executar Login Google

* is_it_possible_to_pass_media()
[1]. Validar se pode enviar mídia para a IA

? Reportar problema
[1]. Título do problema
[2]. Selecionar tipo problema
[3]. Descrição do erro

========

? Navegador (navegador, url, user, ia)
* run()
[1]. Validar se o navegar está instalado
    [1]. Caso esteja instalado 
        [1]. Executar temp_account.create_account()
        [2]. Iniciar Navegador no Perfil visitante e entrar na url
        [3]. Executar is_page_working()
            [1]. Caso False
                [1]. Gerar erro
                [2]. Executar page_doesnt_working()
            [2]. Caso True
                [1]. Continuar com o código
        [4]. Executar ia.run(ia, media)
    [2]. Caso não esteja instalado
        [1]. Gerar Erro
        [2]. Listar Navegadores instalados e colocar '*' aqueles que a automação funcione
        [3]. Solicitar escolha de outro Navegador Compativel ou Fechar Automação
            [1]. Caso outro navegador for escolhido, validar se a automação poderá ocorrer nesse navegador
                [1]. Caso sim
                    [1]. Executar Navegador() com o navegador escolhido
                [2]. Caso não
                    [1]. Gerar Erro
                    [2]. Refazer o '[2]. Caso não esteja instalado'
    [3]. Caso houver algum problema
        [1]. Gerar Erro
        [2]. Executar o Reportar problema

* is_page_working()
[1]. Validar se conseguiu entrar na URL
    [1]. Caso tenha dado certo
        [1]. Retornar True
    [1]. Caso tenha dado errado
        [1]. Gerar Erro
        [2]. Retornar False

* page_doesnt_working()
[1]. Loop de execuções da função reload_page() (3x, espera 5s entre tentativas)
[2]. Executar is_page_working() após o Loop
    [1]. Caso False
        [1]. Gerar Erro
        [2]. Executar test_wifi()
            [1]. Caso 'Boa'
                [1]. Executar reload_page()
                [2]. Executar is_page_working()
                    [1]. Caso True
                        [1]. Continuar com o código
                    [2]. Caso False
                        [1]. Gerar Erro
                        [2]. Solicitar ao Usuário a troca para uma conexão estavel, Tentar novamente, Sair da Automação
                            [1]. Caso Trocar conexão
                                [1]. Solicitar ao User para que após a troca precione Enter para Refazer o teste de Wifi na conexão nova
                                [2]. Executar test_wifi()
                            [2]. Caso Tentar novamente
                                [1]. Executar o ciclo do page_doesnt_working() denovo
                            [3]. Caso Sair da Automação
                                [1]. Sair da automação
            [2]. Caso 'Ruim'
                [1]. Gerar Erro
                [2]. Executar '[2]. Solicitar ao Usuário a troca para uma conexão estavel, Tentar novamente, Sair da Automação'
    [2]. Caso True
        [1]. Contiuar com o código

* test_wifi()
[1]. Testa velocidade (download/upload/ping speedtest)
[2]. Testa ping (latência média, jitter, perda de pacotes)
[3]. Compara resultados com limites aceitáveis
[4]. Gera relatório detalhado com OK/RUIM e explicações
[5]. Mostra diagnóstico para o usuário e retorna { status: 'Boa/Ruim' }
        
* reload_page()
[1]. Recarregar página
                
? temp_account()
* create_account()
[1]. Obter e mostrar domínios disponíveis
[2]. Gerar nome, sobrenome, email e senha forte
[3]. Criar conta na API
[4]. Loop de tentativas para obter token (5x, espera 2s entre tentativas)
    [1]. Se token obtido:
        [1]. Usar token para buscar mensagens
    [2]. Senão:
        [1]. Abortar com erro
[5]. Retornar { success: bool, id: str, f_name: str, l_name: str, pass: str }

* verify_msg(id)
[1]. Usar token para verificar mensagens
[2]. Retornar { has_msg: bool, data: dict }

? ia(ia, user)
* run(media)
[1]. Executar is_logged()
    [1]. Caso False
        [1]. Executar connect_base(user)
        [2]. Executar handler(is_page_working, retry=3, error_message="Página inacessível", on_fail=page_doesnt_working)
        [3]. Executar media()
            [1]. Caso True
                [1]. Executar can_to_pass_media()
                    [1]. Caso True
                        [1]. Usar PROMPT na IA
                        [2]. Passar Mídia para IA
                        [3]. Retornar answers = { REPOSTA_IA }
                    [2]. Caso False
                        [1]. Executar disconnect_base()
                        [2]. 
            [2]. Caso False
                [1]. Usar PROMPT na IA
                    [2]. Retornar answers = { REPOSTA_IA }
        [4]. Validar se não deu erro na coleta de resposta
            [1]. Caso a resposta esteja aparecendo normal e esteja tudo completo
                [1]. Retornar answers = { REPOSTA_IA }
            [2]. Caso a resposta não esteja aparecendo ou deu algum erro
                [1]. Executar Reportar problema
                [2]. Reinicar a página e passar os dados novamente
    [1]. Caso True
        [1]. Executar disconnect_base()
            [1]. Executar handler(is_page_working, retry=3, error_message="Página inacessível", on_fail=page_doesnt_working)
        [2]. Executar connect_base(user)
            [1]. Executar handler(is_page_working, retry=3, error_message="Página inacessível", on_fail=page_doesnt_working)
        [3]. Executar media()

* handler(func, *args, retry=0, error_message="", on_fail=None)
[1]. try:
    [1]. for attempt in range(retry + 1):
        [1]. result = func(*args)
        [2]. if result: return result
        [3]. raise Exception(error_message)
[2]. except Exception as e:
    [1]. if on_fail: on_fail(e)
    [2]. raise e
        
* media
[1]. Validar se há mídia
    [1]. Caso tenha Mídia
        [1]. Retornar True
    [2]. Caso não tenha Mídia
        [1]. Retornar False
[2]. Caso não conseguiu ou der algum erro
    [1]. Executar Reportar Problema

* can_to_pass_media()
[1]. Validar se pode enviar mídia para a IA
    [1]. Caso der:
        [1]. Retornar True
    [2]. Caso não der:
        [1]. Retornar False

* disconnect_base()
[1]. Clicar no incone do user
[2]. Clicar em sair
[3]. Clicar em sair (pop Up)

* connect_base(user, id)
[1]. Clicar em "Cadastra-se gratuitamente"
[2]. Verificar se Enderço de e-mail está selecionado e pronto para digitar
    [1]. Caso sim
        [1]. Digitar user['email']
    [2]. Caso não
        [1]. Clicar em Enderço de e-mail
        [2]. Digitar user['email']
[3]. Precionar enter
[4]. Executar is_page_working()
[4]. Verificar se Senha está selecionado e pronto para digitar
    [1]. Caso sim
        [1]. Digitar user['pass']
    [2]. Caso não
        [1]. Clicar em Senha
        [2]. Digitar user['pass']
[5]. Precionar enter
[4]. Executar is_page_working()
[5]. Executar loop de 3 tentativas com pausa de 2s executando o has_msg, data = temp_account.verify_msg(id) até que o has_msg == True ou data != null/empty
    [1]. Caso has_msg == True
        [1]. Coletar código
    [2]. Caso has_msg == False
        [1]. Clicar em reenviar
        [2]. Executar loop de 3 tentativas com pausa de 2s executando o has_msg, data = temp_account.verify_msg(id) até que o has_msg == True ou data != null/empty
            [1]. Caso has_msg == True
                [1]. Coletar código
            [2]. Caso has_msg == False
                [1]. Gerar Erro
[6]. Verificar se Código está selecionado e pronto para digitar
    [1]. Caso sim
        [1]. Digitar código
    [2]. Caso não
        [1]. Clicar em Senha
        [2]. Digitar código
[7]. Executar is_page_working()
[8]. Verificar se Nome Completo está selecionado e pronto para digitar
    [1]. Caso sim
        [1]. Digitar f'{user['f_name']} {user['l_name']}
    [2]. Caso não
        [1]. Clicar em Senha
        [2]. Digitar f'{user['f_name']} {user['l_name']}
[9]. Verificar se Data de Nascimento está selecionado e pronto para digitar
    [1]. Caso sim
        [1]. Digitar user['born']
    [2]. Caso não
        [1]. Clicar em Senha
        [2]. Digitar user['born']
[10]. Precionar Continuar
[11]. Executar is_page_working()
[12]. Clicar no btn para fechar popup
[13]. Retornar Login realizado com sucesso
        
        
? gmail
* login(gmail, senha)
[1]. Digitar Gmail
    [1]. Validar se deu certo
        [1]. Caso esteja tudo certo
            [1]. Continuar com a automação
        [2]. Caso não funcionar ou der algum erro
            [1]. Gerar Erro
            [2]. Executar reportar_problema()
[2]. Digitar Senha
    [1]. Validar se deu certo
        [1]. Caso esteja tudo certo
            [1]. Continuar com a automação
        [2]. Caso não funcionar ou der algum erro
            [1]. Executar Reportar Problema
[3]. Validar se há verificação em 2 etapas
    [1]. Caso houver
        [1]. Retornar two_step_verification = True
        [2]. Soliciar ao User realizar a verificação em 2 etapas
    [2]. Caso não houver
        [1]. Retornar two_step_verification = False
[4]. Validar se há captcha
    [1]. Caso houver
        [1]. Retornar captch = True
        [2]. Soliciar ao User realizar o captch
    [2]. Caso não houver
        [1]. Retornar captch = False

? reportar_problema()
[1]. Título do problema
[2]. Selecionar tipo problema
[3]. Descrição do erro

------------------------------
-------- VERSÃO FINAL --------
------------------------------

? Navegador (navegador, url, user, ia)
* run()
    [1]. Validar se o navegador está instalado
        [1]. Caso esteja instalado
            [1]. Executar temp_account.create_account()
            [2]. Iniciar o navegador no perfil visitante e entrar na URL
            [3]. Executar is_page_working()
                [1]. Caso False
                    [1]. Gerar erro
                    [2]. Executar page_doesnt_working()
                [2]. Caso True
                    [1]. Continuar com o código
            [4]. Executar ia.run(media)
        [2]. Caso não esteja instalado
            [1]. Gerar erro
            [2]. Listar navegadores instalados e colocar '*' aqueles que a automação funcione
            [3]. Solicitar ao usuário a escolha de outro navegador compatível ou fechar a automação
                [1]. Caso outro navegador for escolhido, validar se a automação poderá ocorrer nesse navegador
                    [1]. Caso sim
                        [1]. Executar Navegador() com o navegador escolhido
                    [2]. Caso não
                        [1]. Gerar erro
                        [2]. Refazer o '[2]. Caso não esteja instalado'
        [3]. Caso houver algum problema
            [1]. Gerar erro
            [2]. Executar o "Reportar problema"
            
* is_page_working()
    [1]. Validar se conseguiu entrar na URL
        [1]. Caso tenha dado certo
            [1]. Retornar {"status": "ok", "error": null, "data": {}}
        [2]. Caso tenha dado errado
            [1]. Gerar erro
            [2]. Retornar {"status": "fail", "error": "Página inacessível", "data": null}
            
* page_doesnt_working()
    [1]. Loop de execuções da função reload_page() (3x, espera 5s entre tentativas)
    [2]. Executar is_page_working() após o Loop
        [1]. Caso False
            [1]. Gerar erro
            [2]. Executar test_wifi()
                [1]. Caso 'Boa'
                    [1]. Executar reload_page()
                    [2]. Executar is_page_working()
                        [1]. Caso True
                            [1]. Continuar com o código
                        [2]. Caso False
                            [1]. Gerar erro
                            [2]. Solicitar ao usuário a troca para uma conexão estável, Tentar novamente, Sair da automação
                                [1]. Caso Trocar conexão
                                    [1]. Solicitar ao User para que após a troca pressione Enter para Refazer o teste de Wifi
                                    [2]. Executar test_wifi()
                                [2]. Caso Tentar novamente
                                    [1]. Executar o ciclo do page_doesnt_working() novamente
                                [3]. Caso Sair da automação
                                    [1]. Sair da automação
                [2]. Caso 'Ruim'
                    [1]. Gerar erro
                    [2]. Executar '[2]. Solicitar ao Usuário a troca para uma conexão estável, Tentar novamente, Sair da automação'
        [2]. Caso True
            [1]. Continuar com o código

* test_wifi()
    [1]. Testa a velocidade (download/upload/ping speedtest)
    [2]. Testa o ping (latência média, jitter, perda de pacotes)
    [3]. Compara resultados com limites aceitáveis
    [4]. Gera relatório detalhado com "OK"/"RUIM" e explicações
    [5]. Mostra diagnóstico para o usuário e retorna { "status": "Boa" | "Ruim" }

* reload_page()
    [1]. Recarregar página

? temp_account()
* create_account()
    [1]. Obter e mostrar domínios disponíveis
    [2]. Gerar nome, sobrenome, e-mail e senha forte
    [3]. Criar conta na API
    [4]. Loop de tentativas para obter token (5x, espera 2s entre tentativas)
        [1]. Se token obtido:
            [1]. Usar token para buscar mensagens
        [2]. Senão:
            [1]. Abortar com erro
    [5]. Retornar { "success": bool, "id": str, "f_name": str, "l_name": str, "pass": str }

* verify_msg(id)
    [1]. Usar token para verificar mensagens
    [2]. Retornar { "has_msg": bool, "data": dict }

? ia(ia, user)
* run(media)
    [1]. Validar se está logado com is_logged()
        [1]. Caso não esteja logado:
            [1]. Executar connect_base(user)
            [2]. Executar handler(is_page_working, retry=3, error_message="Página inacessível", on_fail=page_doesnt_working)
            [3]. Executar media()
                [1]. Caso True
                    [1]. Executar can_to_pass_media()
                        [1]. Caso True
                            [1]. Usar prompt na IA
                            [2]. Passar mídia para a IA
                            [3]. Retornar answers = { "REPOSTA_IA" }
                        [2]. Caso False
                            [1]. Executar disconnect_base()
                [2]. Caso False
                    [1]. Usar prompt na IA
                    [2]. Retornar answers = { "REPOSTA_IA" }
        [2]. Validar se não deu erro na coleta de resposta
            [1]. Caso a resposta esteja aparecendo normal e esteja completa
                [1]. Retornar answers = { "REPOSTA_IA" }
            [2]. Caso a resposta não esteja aparecendo ou haja erro
                [1]. Executar "Reportar problema"
                [2]. Recarregar a página e passar os dados novamente

* handler(func, *args, retry=0, error_message="", on_fail=None)
    [1]. try:
        [1]. for attempt in range(retry + 1):
            [1]. result = func(*args)
            [2]. if result: return result
            [3]. raise Exception(error_message)
    [2]. except Exception as e:
        [1]. if on_fail: on_fail(e)
        [2]. raise e

* media
    [1]. Validar se há mídia
        [1]. Caso tenha mídia
            [1]. Retornar True
        [2]. Caso não tenha mídia
            [1]. Retornar False
    [2]. Caso não consiga ou der erro
        [1]. Executar "Reportar Problema"

* can_to_pass_media()
    [1]. Validar se pode enviar mídia para a IA
        [1]. Caso sim
            [1]. Retornar True
        [2]. Caso não
            [1]. Retornar False

* disconnect_base()
    [1]. Clicar no ícone do usuário
    [2]. Clicar em "Sair"
    [3]. Clicar novamente em "Sair" (pop-up)

* connect_base(user, id)
    [1]. Clicar em "Cadastrar-se gratuitamente"
    [2]. Verificar se o campo "Endereço de e-mail" está selecionado e pronto para digitar
        [1]. Caso sim
            [1]. Digitar user['email']
        [2]. Caso não
            [1]. Clicar em "Endereço de e-mail"
            [2]. Digitar user['email']
    [3]. Pressionar Enter
    [4]. Executar is_page_working()
    [5]. Verificar se o campo "Senha" está selecionado e pronto para digitar
        [1]. Caso sim
            [1]. Digitar user['pass']
        [2]. Caso não
            [1]. Clicar em "Senha"
            [2]. Digitar user['pass']
    [6]. Pressionar Enter
    [7]. Executar is_page_working()
    [8]. Executar loop de 3 tentativas com pausa de 2s executando has_msg, data = temp_account.verify_msg(id) até que has_msg == True ou data != null/empty
        [1]. Caso has_msg == True
            [1]. Coletar código
        [2]. Caso has_msg == False
            [1]. Clicar em "Reenviar"
            [2]. Executar o loop de 3 tentativas novamente até has_msg == True ou data != null/empty
                [1]. Caso has_msg == True
                    [1]. Coletar código
                [2]. Caso has_msg == False
                    [1]. Gerar erro
    [9]. Verificar se o campo "Código" está selecionado e pronto para digitar
        [1]. Caso sim
            [1]. Digitar o código
        [2]. Caso não
            [1]. Clicar em "Código"
            [2]. Digitar o código
    [10]. Executar is_page_working()
    [11]. Verificar se o campo "Nome Completo" está selecionado e pronto para digitar
        [1]. Caso sim
            [1]. Digitar f'{user['f_name']} {user['l_name']}'
        [2]. Caso não
            [1]. Clicar em "Nome Completo"
            [2]. Digitar f'{user['f_name']} {user['l_name']}'
    [12]. Verificar se o campo "Data de Nascimento" está selecionado e pronto para digitar
        [1]. Caso sim
            [1]. Digitar user['born']
        [2]. Caso não
            [1]. Clicar em "Data de Nascimento"
            [2]. Digitar user['born']
    [13]. Pressionar "Continuar"
    [14]. Executar is_page_working()
    [15]. Clicar no botão para fechar o pop-up
    [16]. Retornar "Login realizado com sucesso"

------------------------------
----- ESTRUTURA DE PASTAS ----
------------------------------

C:.
│   answer.py
│   __init__.py
│
├───data
│       answer_data.json
│       prompt_status.md
│
├───models
│   │   __init__.py
│   │
│   ├───ia
│   │   │   ia.py
│   │   │   ia_handler.py
│   │   │   __init__.py
│   │   │
│   │   ├───chatgpt
│   │   │   │   chatgpt.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   ├───models
│   │   │   │   │   __init__.py
│   │   │   │   │
│   │   │   │   ├───AutoGUIGPT
│   │   │   │   │   │   autoguigpt.py
│   │   │   │   │   │   __init__.py
│   │   │   │   │   │
│   │   │   │   │   └───__pycache__
│   │   │   │   │           autoguigpt.cpython-313.pyc
│   │   │   │   │           __init__.cpython-313.pyc
│   │   │   │   │
│   │   │   │   ├───AutoStealphGPT
│   │   │   │   │   │   autostealphgpt.py
│   │   │   │   │   │   __init__.py
│   │   │   │   │   │
│   │   │   │   │   └───__pycache__
│   │   │   │   │           autostealphgpt.cpython-313.pyc
│   │   │   │   │           __init__.cpython-313.pyc
│   │   │   │   │
│   │   │   │   └───__pycache__
│   │   │   │           __init__.cpython-313.pyc
│   │   │   │
│   │   │   └───__pycache__
│   │   │           chatgpt.cpython-313.pyc
│   │   │           __init__.cpython-313.pyc
│   │   │
│   │   ├───grok
│   │   │   │   grok.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   ├───models
│   │   │   │   │   __init__.py
│   │   │   │   │
│   │   │   │   ├───AutoGUIGROK
│   │   │   │   │   │   autoguigrok.py
│   │   │   │   │   │   __init__.py
│   │   │   │   │   │
│   │   │   │   │   └───__pycache__
│   │   │   │   │           autoguigrok.cpython-313.pyc
│   │   │   │   │           __init__.cpython-313.pyc
│   │   │   │   │
│   │   │   │   ├───AutoStealphGROK
│   │   │   │   │   │   autostealphgrok.py
│   │   │   │   │   │   __init__.py
│   │   │   │   │   │
│   │   │   │   │   └───__pycache__
│   │   │   │   │           autostealphgrok.cpython-313.pyc
│   │   │   │   │           __init__.cpython-313.pyc
│   │   │   │   │
│   │   │   │   └───__pycache__
│   │   │   │           __init__.cpython-313.pyc
│   │   │   │
│   │   │   └───__pycache__
│   │   │           grok.cpython-313.pyc
│   │   │           __init__.cpython-313.pyc
│   │   │
│   │   ├───utils
│   │   │   │   answer_data_json.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           answer_data_json.cpython-313.pyc
│   │   │
│   │   └───__pycache__
│   │           ia.cpython-313.pyc
│   │           ia_handler.cpython-313.pyc
│   │           __init__.cpython-313.pyc
│   │
│   └───__pycache__
│           __init__.cpython-313.pyc
│
├───utils
│   │   menu_system.py
│   │   __init__.py
│   │
│   ├───navegador
│   │   │   navegador.py      # Implementação do módulo "Navegador"
│   │   │   __init__.py
│   │   │   page_utils.py     # Funções auxiliares para o navegador
│   │   │
│   │   ├───__pycache__
│   │   │       navegador.cpython-313.pyc
│   │   │       __init__.cpython-313.pyc
│   │   │
│   └───__pycache__
│           menu_system.cpython-313.pyc
│           __init__.cpython-313.pyc
│
└───__pycache__
        answer.cpython-313.pyc
        __init__.cpython-313.pyc

------------------------------
------------------------------

UPDATE

Sua atualização trouxe ainda **mais robustez e detalhamento**, o que é ótimo! A separação dos fluxos como `is_logged()`, `connect_base()`, e `media()` ajuda a modularizar a automação. A estrutura geral está bastante sólida. Dito isso, realmente há espaço para pequenas melhorias, especialmente com **handlers de erro**, **padronização de decisões** e **clareza de fluxo principal**.

---

## ✅ Pontos fortes dessa versão

* **Estrutura modular e detalhada**, com boas divisões de responsabilidade entre IA, navegador e conta temporária.
* **Tratamento de erros está bem pensado**, com fallback, validação e tentativa de recuperação.
* **Fluxo de mídia e checagem de sessão IA** adiciona lógica prática que costuma ser ignorada em muitas automações.

---

## 🔧 Sugestões de melhoria

### 1. **Implementar um `handler()` centralizado**

Hoje, cada função lida com seus próprios erros, o que pode repetir muita lógica. Seria melhor ter um **handler genérico** para:

```python
def handler(func, *args, retry=0, error_message="", on_fail=None):
    try:
        for attempt in range(retry + 1):
            result = func(*args)
            if result: return result
        raise Exception(error_message)
    except Exception as e:
        if on_fail: on_fail(e)
        raise e
```

Assim, em vez de repetir:

```txt
[1]. Executar is_page_working()
    [1]. Caso False
        [1]. Gerar erro
        [2]. Executar page_doesnt_working()
```

Você poderia fazer:

```python
handler(is_page_working, retry=3, error_message="Página inacessível", on_fail=page_doesnt_working)
```

---

### 2. **Padronizar estados de erro e sucesso**

Considere sempre retornar objetos padronizados, como:

```json
{
  "status": "ok" | "fail",
  "error": "string | null",
  "data": {}
}
```

Isso permite criar funções reutilizáveis que tomam decisão com base no `status`, reduzindo blocos de decisão duplicados.

---

### 3. **Separar os fluxos de UI vs. lógicas técnicas**

Se a automação vai interagir com usuários (prompt, espera de ações), considere encapsular isso em:

```txt
? user_prompt
* solicitacao_troca_conexao()
* aguardar_enter_apos_troca()
* escolher_navegador()
* mostrar_diagnostico_wifi()
```

Hoje essas interações estão “espalhadas” em várias funções. Separá-las melhora manutenção e facilita testes (mock de interação).

---

### 4. **Revisar a lógica do `ia.run()`**

Atualmente o `ia.run()` está com ramificações aninhadas demais (especialmente no tratamento de `is_logged()`), o que pode ser difícil de manter.

Sugestão de simplificação do fluxo:

```txt
1. Validar sessão com is_logged()
    - Se não logado:
        - connect_base()
        - validar página
2. Validar mídia
    - Se há mídia e pode enviar:
        - prompt + enviar mídia
    - Se há mídia e **não pode enviar**:
        - mudar de perfil ou logar com outro
    - Se **não há mídia**:
        - apenas prompt
3. Validar resposta
    - Se falhou:
        - reportar erro
        - recarregar e tentar novamente
4. Retornar resposta final
```

---

### 5. **Pequenos ajustes de nomenclatura/estrutura**

* `PassarM Ídia` tem espaço e acento estranho.
* `[2].` dentro de `connect_base()` está desorganizado.
* A função `media()` deveria talvez se chamar `has_media()` para ser mais clara, já que retorna boolean.

---

### ✅ Exemplo de fluxo com handler aplicado

```python
def run():
    if not navegador_instalado():
        return handler(escolher_navegador, retry=1)

    conta = handler(temp_account.create_account, retry=2)
    abrir_navegador()

    handler(is_page_working, retry=2, on_fail=page_doesnt_working)

    resposta = handler(ia.run, media)
    return resposta
```

---

## ✅ Conclusão

Você está num ótimo caminho. Essa automação já está bastante completa, e agora o foco é:

* Reduzir duplicações com handlers e retorno padronizado;
* Clarear fluxos aninhados (especialmente dentro de IA);
* Modularizar interações com o usuário.

Se quiser, posso:

* **Gerar um pseudocódigo funcional completo**;
* **Criar um fluxograma visual**;
* **Transformar em código Python estruturado**.

Só dizer como você quer seguir!

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
