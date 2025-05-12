from project import LogType, SistemaUsuarios

class UserService:
    def __init__(self):
        self.sistema_usuarios = SistemaUsuarios()

    def criar_usuario(self, nome, sobrenome, tipo_conta, ra, dg_ra, uf_ra):
        self.sistema_usuarios.adicionar_usuario(nome, sobrenome, tipo_conta, ra, dg_ra, uf_ra)
        print(f'[{LogType.SUCCESS}] Usuário {nome} {sobrenome} criado com sucesso!')

    def listar_usuarios(self):
        usuarios = self.sistema_usuarios.carregar_usuarios()
        if not usuarios:
            print(f'[{LogType.WARNING}] Nenhum usuário cadastrado.')
        else:
            for usuario in usuarios.values():
                print(f'[{LogType.USER}] ID: {usuario.id_usuario}, Nome: {usuario.nome} {usuario.sobrenome}')

    def atualizar_usuario(self, id_usuario, **kwargs):
        if id_usuario not in self.sistema_usuarios.usuarios:
            print(f'[{LogType.ERROR}] Usuário com ID {id_usuario} não encontrado.')
            return False

        usuario = self.sistema_usuarios.usuarios[id_usuario]
        for key, value in kwargs.items():
            if hasattr(usuario, key):
                setattr(usuario, key, value)
            else:
                print(f'[{LogType.ERROR}] Atributo \'{key}\' não existe no usuário.')
                return False

        self.sistema_usuarios.salvar_usuarios()
        print(f'[{LogType.SUCCESS}] Usuário {usuario.nome} {usuario.sobrenome} atualizado com sucesso!')
        return True

    def deletar_usuario(self, id_usuario):
        if id_usuario not in self.sistema_usuarios.usuarios:
            print(f'[{LogType.ERROR}] Usuário com ID {id_usuario} não encontrado.')
            return False

        usuario = self.sistema_usuarios.usuarios[id_usuario]
        del self.sistema_usuarios.usuarios[id_usuario]
        self.sistema_usuarios.salvar_usuarios()
        print(f'[{LogType.SUCCESS}] Usuário {usuario.nome} {usuario.sobrenome} deletado com sucesso!')
        return True