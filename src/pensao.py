from typing import Any


class Pensao:
    def __init__(self, valor_pensao: int | float) -> None:
        if not valor_pensao:
            raise ValorPensaoEmBrancoException(valor_pensao)
        if type(valor_pensao) not in [float, int] or valor_pensao < 0:
            raise ValorPensaoInvalidaException(valor_pensao)
        self.valor_pensao = valor_pensao


class ValorPensaoInvalidaException(Exception):
    def __init__(self, valor_pensao: Any) -> None:
        self.valor_pensao = valor_pensao
        super().__init__(f"Valor inválido: {self.valor_pensao}")

    def __str__(self) -> str:
        return f"Valor inválido: {self.valor_pensao}"


class ValorPensaoEmBrancoException(Exception):
    def __init__(self, valor_pensao: Any) -> None:
        self.valor_pensao = valor_pensao
        super().__init__(f"Valor em branco: {valor_pensao}")

    def __str__(self) -> str:
        return f"Valor em branco: {self.valor_pensao}"
