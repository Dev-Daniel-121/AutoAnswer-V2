class SalaDoFuturo:
    def __init__(self):
        self.nome = "Sala do Futuro"

    def printa(self):
        print(f"Bem-vindo à {self.nome}!")

    def iniciar(self):
        print(f"Iniciando {self.nome}...")

def printa():
    sala = SalaDoFuturo()
    sala.printa()