class Rendimento:
    def __init__(self, descricao, valor)->None:
        if not descricao or not descricao.strip():
            raise DescricaoEmBrancoException(descricao)
        if type(valor) != int or not valor or valor < 0:
            raise ValorRendimentoInvalidoException(valor)  
        self.descricao = descricao
        self.valor = valor

class DescricaoEmBrancoException(Exception):
    
    def __init__(self, descricao: str) -> None:
        self.descricao = descricao
        super().__init__(f"Descrição em branco: {descricao}")

    def __str__(self) -> str:
        return f"Descrição em branco: {self.descricao}"      

class ValorRendimentoInvalidoException(Exception):
    def __init__(self, valor: int) -> None:
        self.valor = valor
        super().__init__("Valor inválido: -100")

    def __str__(self) -> str:
        return f"Valor inválido: {self.valor}"   