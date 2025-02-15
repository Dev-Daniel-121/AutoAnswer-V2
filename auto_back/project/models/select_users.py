from project.config import types
from project.models import SistemaUsuarios

class SelecionarUsuarios:
    from project.models import SistemaUsuarios
    def __init__(self):
        self.sistema_usuarios = SistemaUsuarios()
        self.usuarios_selecionados = []
        self.types = types

    def run(self):
        while True:
            self.sistema_usuarios.carregar_usuarios()
            usuarios = self.sistema_usuarios.usuarios
            if not usuarios:
                print(f"\n[{types[8]}] Nenhum usuário cadastrado.")
                resposta = input(f"[{types[0]}] Deseja adicionar um novo usuário agora? (Y/n): ").strip().upper()
                if resposta == "":
                    resposta = "Y"
                    
                if resposta == "Y":
                    self.sistema_usuarios.adicionar_usuario()
                    self.sistema_usuarios.salvar_usuarios()
                    continue
                else:
                    from project.menus import MenuSystem
                    menu_system = MenuSystem()
                    menu_system.run()
                    return

            self.sistema_usuarios.mostrar_usuarios()

            escolha = input(f"\n[{types[9]}] Digite os IDs dos usuários separados por vírgula ou '*' para todos: ").strip()
            
            if escolha.lower() in ("*", "all"):
                self.usuarios_selecionados = list(usuarios.keys())
                break
            
            try:
                ids_selecionados = [id_usuario.strip() for id_usuario in escolha.split(",")]

                for id_usuario in ids_selecionados:
                    id_usuario = str(id_usuario).strip()

                    if id_usuario not in usuarios:
                        print(f"[{types[4]}] ID {id_usuario} não encontrado. Tente novamente.")
                        break
                else:
                    self.usuarios_selecionados = ids_selecionados
                    print(f"[{types[7]}] Usuários selecionados com sucesso:", self.usuarios_selecionados)
                    input(f"\n[{types[6]}] Pressione Enter para continuar...")
                    break
            except Exception as e:
                print(f"[{types[4]}] Entrada inválida. Erro: {e}. Tente novamente.")

    def get_usuarios_selecionados(self):
        return self.usuarios_selecionados