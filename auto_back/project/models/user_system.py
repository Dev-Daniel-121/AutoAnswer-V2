from project.utils import Display, JSONHandler
from project.config import types
import os

class Usuario:
    def __init__(self, id_usuario, nome, sobrenome, tipo_conta, ra, dg_ra, uf_ra):
        self.id_usuario = id_usuario
        self.nome = nome
        self.sobrenome = sobrenome
        self.tipo_conta = tipo_conta
        self.ra = ra
        self.dg_ra = dg_ra
        self.uf_ra = uf_ra
        self.email = f'0000{ra}{dg_ra}{uf_ra}@al.educacao.sp.gov.br'
        self.senha = f'Bp{ra[:6]}#'
        self.user = self.gerar_user()
        self.types = types

    def gerar_user(self):
        nome_part = self.nome[:5].lower()
        sobrenome_part = self.sobrenome[:5].lower()
        
        ra_part = self.ra[-9:]
        
        uf_part = self.uf_ra.lower()
        
        return f'{nome_part}{sobrenome_part}{ra_part}-{uf_part}'

    def __str__(self):
        return f'ID: {self.id_usuario} - Nome: {self.nome} - Sobrenome: {self.sobrenome} - Tipo de Conta: {self.tipo_conta}'

class SistemaUsuarios:
    def __init__(self):
        self.json_handler = JSONHandler(os.path.join('data', 'usuarios.json'))
        self.usuarios = self.carregar_usuarios()

    def carregar_usuarios(self):
        data = self.json_handler.carregar()
        usuarios = {}
        for id_usuario, info in data.items():
            usuarios[id_usuario] = Usuario(
                id_usuario,
                info['nome'],
                info['sobrenome'],
                info['tipo_conta'],
                info['ra'],
                info['dg_ra'],
                info['uf_ra']
            )
        return usuarios

    def salvar_usuarios(self):
        data = {}
        for usuario in self.usuarios.values():
            data[usuario.id_usuario] = {
                'nome': usuario.nome,
                'sobrenome': usuario.sobrenome,
                'tipo_conta': usuario.tipo_conta,
                'ra': usuario.ra,
                'dg_ra': usuario.dg_ra,
                'uf_ra': usuario.uf_ra,
                'email': usuario.email,
                'senha': usuario.senha,
                'user': usuario.user
            }
        return self.json_handler.salvar(data)

    def mostrar_usuarios(self):
        if not self.usuarios: 
            print(f'\n[{types[8]}] Nenhum usuário encontrado.')
        else:
            print('\n~~~~~~ Usuários Cadastrados ~~~~~~')
            for usuario in self.usuarios.values():
                print(f'\n[{types[5]}] - ID: [{usuario.id_usuario}]\n\t Nome: {usuario.nome} {usuario.sobrenome}\n\t Tipo de Conta: {usuario.tipo_conta}\n\t Email: {usuario.email}')
            print(f'\n{'-' * 30}')

    def converter_tipo_conta(self, tipo_conta):
        if tipo_conta.lower() in ['al', 'aluno']:
            return 'Aluno'
        elif tipo_conta.lower() in ['pr', 'professor']:
            return 'Professor'
        else:
            return tipo_conta

    def adicionar_usuario(self):
        while True:
            nome = input(f'\n[{types[9]}] Digite o nome do novo usuário: ').strip().capitalize()
            if not nome:
                print(f'[{types[4]}] O nome não pode ser vazio. Tente novamente.')
                continue
            break
        
        while True:
            sobrenome = input(f'[{types[9]}] Digite o sobrenome do novo usuário: ').strip().title()
            if not sobrenome:
                print(f'[{types[4]}] O sobrenome não pode ser vazio. Tente novamente.')
                continue
            break
        
        while True:
            tipo_conta = input(f'[{types[9]}] Digite o tipo de conta (Aluno/Professor): ').strip()
            tipo_conta = self.converter_tipo_conta(tipo_conta)
            if tipo_conta not in ['Aluno', 'Professor']:
                print(f'[{types[4]}] Tipo de conta inválido! Escolha entre \'Aluno/Al\' ou \'Professor/Pr\'.')
                continue
            break
        
        while True:
            ra = input(f'[{types[9]}] Digite o RA do novo usuário: ').strip()
            if not ra.isdigit() or len(ra) != 9:
                print(f'[{types[4]}] RA inválido! O RA deve ter 9 dígitos.')
                continue
            break
        
        while True:
            dg_ra = input(f'[{types[9]}] Digite o dígito do RA (1 dígito): ').strip()
            if not dg_ra.isdigit() or len(dg_ra) != 1:
                print(f'[{types[4]}] Dígito do RA inválido! Deve ter 1 dígito.')
                continue
            break
        
        while True:
            uf_ra = input(f'[{types[9]}] Digite a UF do RA (exemplo: SP, MG): ').strip().upper()
            if len(uf_ra) != 2 or not uf_ra.isalpha():
                print(f'[{types[4]}] UF inválida! A UF deve ter 2 letras.')
                continue
            break

        novo_id = str(max([int(id_usuario) for id_usuario in self.usuarios.keys()], default=0) + 1)
        
        novo_usuario = Usuario(
            novo_id,
            nome,
            sobrenome,
            tipo_conta,
            ra,
            dg_ra,
            uf_ra
        )
        
        self.usuarios[novo_id] = novo_usuario
        self.salvar_usuarios()
        print(f'\n[{types[7]}] Usuário {nome} {sobrenome} adicionado com sucesso!')
        input(f'\n[{types[6]}] Pressione Enter para continuar...')

    def alterar_usuario(self):
        if not self.usuarios:
            print(f'\n[{types[4]}] Não é possível alterar um usuário sem que haja pelo menos um usuário cadastrado.')
            input(f'\n[{types[6]}] Pressione Enter para continuar...')
            return

        while True:
            ids_input = input(f'\n[{types[9]}] Digite os IDs dos usuários que deseja alterar (separados por \',\' \'*\' para todos): ').strip().lower()
            
            if ids_input in ['*', 'all']:
                ids = list(self.usuarios.keys())
                break
            
            ids = [id_usuario.strip() for id_usuario in ids_input.split(',')]
            
            ids_invalidos = [id_usuario for id_usuario in ids if id_usuario not in self.usuarios]
            
            if ids_invalidos:
                print(f'[{types[4]}] Os seguintes IDs não foram encontrados: {', '.join(ids_invalidos)}. Tente novamente.')
                continue
            break

        for id_usuario in ids:
            usuario = self.usuarios[id_usuario]
            print(f'\n[{types[5]}] Alterando usuário - ID: {usuario.id_usuario}, Nome: {usuario.nome} {usuario.sobrenome}')
            
            novo_nome = input(f'[{types[9]}] Digite o novo nome para {usuario.nome} (deixe em branco para não alterar): ').strip().title()
            if novo_nome:
                usuario.nome = novo_nome
            
            novo_sobrenome = input(f'[{types[9]}] Digite o novo sobrenome para {usuario.sobrenome} (deixe em branco para não alterar): ').strip().title()
            if novo_sobrenome:
                usuario.sobrenome = novo_sobrenome
            
            novo_tipo_conta = input(f'[{types[9]}] Digite o novo tipo de conta para {usuario.tipo_conta} (deixe em branco para não alterar): ').strip()
            if novo_tipo_conta:
                novo_tipo_conta = self.converter_tipo_conta(novo_tipo_conta)
                if novo_tipo_conta not in ['Aluno', 'Professor']:
                    print(f'[{types[4]}] Tipo de conta inválido! A conta não foi alterada.')
                    continue
                usuario.tipo_conta = novo_tipo_conta
            
            novo_ra = input(f'[{types[9]}] Digite o novo RA para {usuario.ra} (deixe em branco para não alterar): ').strip()
            if novo_ra:
                if not novo_ra.isdigit() or len(novo_ra) != 9:
                    print(f'[{types[4]}] RA inválido! A alteração não foi realizada.')
                    continue
                usuario.ra = novo_ra
            
            novo_dg_ra = input(f'[{types[9]}] Digite o novo dígito do RA para {usuario.dg_ra} (deixe em branco para não alterar): ').strip()
            if novo_dg_ra:
                if not novo_dg_ra.isdigit() or len(novo_dg_ra) != 1:
                    print(f'[{types[4]}] Dígito do RA inválido! A alteração não foi realizada.')
                    continue
                usuario.dg_ra = novo_dg_ra
            
            novo_uf_ra = input(f'[{types[9]}] Digite a nova UF para {usuario.uf_ra} (deixe em branco para não alterar): ').strip().upper()
            if novo_uf_ra:
                if len(novo_uf_ra) != 2 or not novo_uf_ra.isalpha():
                    print(f'[{types[4]}] UF inválida! A alteração não foi realizada.')
                    continue
                usuario.uf_ra = novo_uf_ra
            
            usuario.email = f'0000{usuario.ra}{usuario.dg_ra}{usuario.uf_ra}@al.educacao.sp.gov.br'
            usuario.senha = f'Bp{usuario.ra[:6]}#'
            usuario.user = usuario.gerar_user()
            
            print(f'\n[{types[7]}] Usuário {usuario.nome} {usuario.sobrenome} (ID: {usuario.id_usuario}) alterado com sucesso!')
        
        self.salvar_usuarios()
        input(f'\n[{types[6]}] Pressione Enter para continuar...')

    def deletar_usuario(self):
        if not self.usuarios:
            print(f'\n[{types[4]}] Não é possível deletar um usuário sem que haja pelo menos um usuário cadastrado.')
            input(f'\n[{types[6]}] Pressione Enter para continuar...')
            return

        while True:
            ids_input = input(f'\n[{types[9]}] Digite os IDs dos usuários que deseja deletar (separados por \',\' \'*\' para todos): ').strip().lower()
            
            if ids_input in ['*', 'all']:
                ids = list(self.usuarios.keys())
                break
            
            ids = [id_usuario.strip() for id_usuario in ids_input.split(',')]
            
            ids_invalidos = [id_usuario for id_usuario in ids if id_usuario not in self.usuarios]
            
            if ids_invalidos:
                print(f'[{types[4]}] Os seguintes IDs não foram encontrados: {', '.join(ids_invalidos)}. Tente novamente.')
                continue
            break

        if ids_input in ['*', 'all']:
            confirmacao = input(f'\n[{types[4]}] Você está prestes a deletar TODOS os usuários. Tem certeza? (Y/n): ').strip().lower()
            if confirmacao == '': confirmacao = 'y'
                
            if confirmacao != 'y':
                print(f'[{types[4]}] Operação cancelada.')
                input(f'\n[{types[6]}] Pressione Enter para continuar...')
                return

        for id_usuario in ids:
            usuario = self.usuarios[id_usuario]
            print(f'\n[{types[5]}] Deletando usuário - ID: {usuario.id_usuario}, Nome: {usuario.nome} {usuario.sobrenome}')
            del self.usuarios[id_usuario]
        
        self.salvar_usuarios()
        print(f'\n[{types[7]}] Usuários deletados com sucesso!')
        input(f'\n[{types[6]}] Pressione Enter para continuar...')

    def run(self):
        while True:
            if not self.usuarios:
                print(f'\n[{types[4]}] Nenhum usuário cadastrado. Adicione um usuário antes de realizar outras operações.')
                input(f'\n[{types[6]}] Pressione Enter para continuar...')

            os.system('cls' if os.name == 'nt' else 'clear')

            self.mostrar_usuarios()

            options_data = [(2, 'Adicionar um novo usuário'), (2, 'Alterar dados de um usuário'), (2, 'Deletar um usuário'), (2, 'Voltar')]
            options = Display(options_data, 'USUÁRIOS', answer=True, user='', title_quest='', clear_enabled=False)
            user_choice = options.display()

            if user_choice == 1:
                self.adicionar_usuario()
            elif user_choice == 2:
                self.alterar_usuario()
            elif user_choice == 3:
                self.deletar_usuario()
            elif user_choice == 4:
                from project.menus import MenuSystem
                menu_system = MenuSystem()
                menu_system.settings()
                break
            else:
                print(f'[{types[4]}] Opção inválida, tente novamente.')