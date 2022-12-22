from deducao import Deducao


class Contribuicao(Deducao):
    def __init__(self, descricao: str, valor: int | float) -> None:
        super().__init__(descricao, valor)
