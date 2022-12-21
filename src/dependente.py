class Dependente:
    def __init__(self, nome: str, dataNascimento: int) -> None:
        if not nome or not nome.strip():
            raise NomeEmBrancoException(nome)
        self.nome = nome
        self.dataNascimento = dataNascimento


class NomeEmBrancoException(Exception):
    def __init__(self, descricao: str) -> None:
        self.descricao = descricao
        super().__init__(f"Nome em branco: {descricao}")

    def __str__(self) -> str:
        return f"Nome em branco: {self.descricao}"