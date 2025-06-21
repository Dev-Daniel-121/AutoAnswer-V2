class ValidateRadios:
    def __init__(self):
        pass

    def validate(self, resposta, opcoes):
        try:
            if not isinstance(resposta, str):
                raise ValueError('A resposta deve ser uma string.')
            if resposta not in opcoes:
                raise ValueError(f'\'{resposta}\' não é uma opção válida.')
            return True
        except ValueError as e:
            print(f'Erro de validação: {e}')
            return False
