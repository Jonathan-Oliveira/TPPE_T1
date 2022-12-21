class Pensao:
    def __init__(self, valor_pensao: int) -> None:
        if type(valor_pensao) != int or not valor_pensao or valor_pensao < 0:
            raise ValorPensaoInvalidaException(valor_pensao)
        self.valor_pensao = valor_pensao


class ValorPensaoInvalidaException(Exception):
    def __init__(self, valor_pensao: int) -> None:
        self.valor_pensao = valor_pensao
        super().__init__("Valor inválido: -100")

    def __str__(self) -> str:
        return f"Valor inválido: {self.valor_pensao}"