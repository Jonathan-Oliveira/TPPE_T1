class Rendimento:
    def __init__(self, descricao, valor)->None:
        if not descricao:
            raise DescricaoEmBrancoException(descricao)
        self.descricao = descricao
        self.valor = valor

class DescricaoEmBrancoException(Exception):
    
    def __init__(self, descricao: str) -> None:
        self.descricao = descricao
        super().__init__(f"Descrição em branco: {descricao}")

    def __str__(self) -> str:
        return f"Descrição em branco: {self.descricao}"      