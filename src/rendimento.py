from typing import Any


class Rendimento:
    def __init__(self, descricao: str, valor: int | float) -> None:
        if not descricao or not descricao.strip():
            raise DescricaoEmBrancoException(descricao)
        if not valor or type(valor) not in [int, float] or valor < 0:
            raise ValorRendimentoInvalidoException(valor)
        self.descricao = descricao
        self.valor = valor


class DescricaoEmBrancoException(Exception):
    def __init__(self, descricao: Any) -> None:
        self.descricao = descricao
        super().__init__(f"Descrição em branco: {descricao}")

    def __str__(self) -> str:
        return f"Descrição em branco: {self.descricao}"


class ValorRendimentoInvalidoException(Exception):
    def __init__(self, valor: Any) -> None:
        self.valor = valor
        super().__init__(f"Valor inválido: {valor}")

    def __str__(self) -> str:
        return f"Valor inválido: {self.valor}"
