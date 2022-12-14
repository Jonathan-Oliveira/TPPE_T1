from typing import Any


class Deducao:
    def __init__(self, descricao: str, valor: int | float) -> None:
        if not descricao or not descricao.strip():
            raise DescricaoEmBrancoException(descricao)
        if type(valor) not in [float, int] or not valor or valor < 0:
            raise ValorDeducaoInvalidoException(valor)
        self.descricao = descricao
        self.valor = valor


class ValorDeducaoInvalidoException(Exception):
    def __init__(self, valor: Any) -> None:
        self.valor = valor
        super().__init__("Valor inválido: -100")

    def __str__(self) -> str:
        return f"Valor inválido: {self.valor}"


class DescricaoEmBrancoException(Exception):
    def __init__(self, descricao: Any) -> None:
        self.descricao = descricao
        super().__init__(f"Descrição em branco: {descricao}")

    def __str__(self) -> str:
        return f"Descrição em branco: {self.descricao}"
