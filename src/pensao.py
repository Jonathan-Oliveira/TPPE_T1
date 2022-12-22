class Pensao:
    def __init__(self, valor_pensao: int) -> None:
        if type(valor_pensao) != int or not valor_pensao or valor_pensao < 0:
            raise ValorPensaoInvalidaException(valor_pensao)
        self.valor_pensao = valor_pensao


class ValorPensaoInvalidaException(Exception):
    def __init__(self, valor_pensao: int) -> None:
        self.valor_pensao = valor_pensao
        super().__init__ (f"Valor inválido: {self.valor_pensao}")

    def __str__(self) -> str:
        return f"Valor inválido: {self.valor_pensao}"

class ValorPensaoEmBrancoException(Exception):
    def __init__(self, valor_pensao: str) -> None:
        self.valor_pensao = valor_pensao
        super().__init__(f"Valor em branco: {valor_pensao}")

    def __str__(self) -> str:
        return f"Valor em branco: {self.valor_pensao}"
