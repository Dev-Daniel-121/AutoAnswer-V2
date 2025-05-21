class IA:
    def __init__(self, nome: str):
        self.nome = nome
        self.metodos = {
            'GUI': True,
            'Stealph': True
        }

    def get_status_metodo(self, metodo: str):
        status = self.metodos.get(metodo, False)
        return 'Operando normalmente' if status else 'Indisponível'

    def get_status_geral(self):
        if all(self.metodos.values()):
            return f'{self.nome} – Operando normalmente'
        elif any(self.metodos.values()):
            return f'{self.nome} – Operação parcial'
        else:
            return f'{self.nome} – Indisponível'

    def get_status_detalhado(self):
        status_geral = self.get_status_geral()
        status_por_metodo = [
            f'{self.nome} – {metodo}: {self.get_status_metodo(metodo)}'
            for metodo in self.metodos
        ]
        return status_geral, status_por_metodo
    