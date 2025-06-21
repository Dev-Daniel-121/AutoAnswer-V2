class ValidateCheckbox:
    def __init__(self):
        pass

    def validate(self, respostas, opcoes):
        try:
            if not isinstance(respostas, list):
                raise ValueError('As respostas devem ser uma lista.')
            if not respostas:
                raise ValueError('Pelo menos uma opção deve ser selecionada.')
            if len(respostas) > len(opcoes):
                raise ValueError('Número de respostas excede o número de opções.')
            for resposta in respostas:
                if resposta not in opcoes:
                    raise ValueError(f'\'{resposta}\' não é uma opção válida.')
            return True
        except ValueError as e:
            print(f'Erro de validação: {e}')
            return False
