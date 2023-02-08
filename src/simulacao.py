from rendimento import Rendimento
from deducao import Deducao
from dependente import Dependente
from pensao import Pensao
from contribuicao import Contribuicao
from valores import Valores
from math import floor


class Simulacao:
    """
    Classe que representa uma simulação de cálculo de imposto de renda.

    Através da classe, é possível adicionar rendimentos, deduções, dependentes,
    pensões e contribuições, além de calcular o valor líquido e o valor do imposto
    devido.

    Attributes
    ---------
    rendimentos: list[Rendimento]
        Lista de rendimentos da simulação.
    deducoes: list[Deducao]
        Lista de deduções da simulação.
    dependentes: list[Dependente]
        Lista de dependentes da simulação.
    pensoes: list[Pensao]
        Lista de pensões da simulação.
    contribuicoes: list[Contribuicao]
        Lista de contribuições da simulação.
    total_rendimento: float | int
        Valor total dos rendimentos da simulação.
    total_deducoes: float | int
        Valor total das deduções da simulação.

    Methods
    -------
    adiciona_rendimento(descricao: str, valor: float) -> None
        Adiciona um rendimento à simulação.
    get_total_rendimento() -> float | int
        Retorna o valor total dos rendimentos da simulação.
    adiciona_deducao(descricao: str, valor: float) -> None
        Adiciona uma dedução à simulação.
    adiciona_pensao(valor: float) -> None
        Adiciona uma pensão à simulação.
    get_total_deducao() -> float | int
        Retorna o valor total das deduções da simulação.
    adiciona_dependente(nome: str, dataNascimento: str) -> None
        Adiciona um dependente à simulação.
    adiciona_contribuicao(descricao: str, valor: int | float) -> None
        Adiciona uma contribuição à simulação.
    get_valor_liquido() -> float | int
        Retorna o valor líquido da simulação.
    get_valor_imposto() -> float | int
        Retorna o valor do imposto devido da simulação.
    get_aliquota() -> float
        Retorna a alíquota efetiva da simulação.
    """

    def __init__(
        self,
        rendimentos: list[Rendimento] = [],
        deducoes: list[Deducao] = [],
        dependentes: list[Dependente] = [],
        pensoes: list[Pensao] = [],
        contribuicoes: list[Contribuicao] = [],
    ):
        """
        Construtor da classe Simulacao.

        Parameters
        ----------
        rendimentos: list[Rendimento]
            Lista de rendimentos da simulação.
        deducoes: list[Deducao]
            Lista de deduções da simulação.
        dependentes: list[Dependente]
            Lista de dependentes da simulação.
        pensoes: list[Pensao]
            Lista de pensões da simulação.
        contribuicoes: list[Contribuicao]
            Lista de contribuições da simulação.
        """

        self.rendimentos = rendimentos
        self.deducoes = deducoes
        self.dependentes = dependentes
        self.pensoes = pensoes
        self.contribuicoes = contribuicoes
        self.total_rendimento: float | int = 0
        self.total_deducoes: float | int = 0

    def adiciona_rendimento(self, descricao: str, valor: float) -> None:
        """
        Adiciona um rendimento à simulação.

        Parameters
        ----------
        descricao: str
          Descrição do rendimento.
        valor: float
          Valor do rendimento.
        """

        rendimento = Rendimento(descricao, valor)
        self.total_rendimento += rendimento.valor
        self.rendimentos.append(rendimento)

    def get_total_rendimento(self) -> float | int:
        """
        Retorna o valor total dos rendimentos da simulação.

        Returns
        -------
        float | int
            Valor total dos rendimentos da simulação.
        """

        return self.total_rendimento

    def adiciona_deducao(self, descricao: str, valor: float) -> None:
        """
        Adiciona uma dedução à simulação.

        Parameters
        ----------
        descricao: str
            Descrição da dedução.
        valor: float
            Valor da dedução.

        """

        deducao = Deducao(descricao, valor)
        self.deducoes.append(deducao)
        self.total_deducoes += valor

    def adiciona_pensao(self, valor: float) -> None:
        """
        Adiciona uma pensão à simulação.

        Parameters
        ----------
        valor: float
            Valor da pensão.
        """

        pensao = Pensao(valor)
        self.pensoes.append(pensao)
        self.total_deducoes += valor

    def get_total_deducao(self) -> float | int:
        """
        Retorna o valor total das deduções da simulação.

        Returns
        -------
        float | int
            Valor total das deduções da simulação.
        """

        return self.total_deducoes

    def adiciona_dependente(self, nome: str, dataNascimento: str) -> None:
        """
        Adiciona um dependente à simulação.

        Parameters
        ----------
        nome: str
            Nome do dependente.
        dataNascimento: str
            Data de nascimento do dependente.
        """

        dependente = Dependente(nome, dataNascimento)
        self.total_deducoes += dependente.valor
        self.dependentes.append(dependente)

    def adiciona_contribuicao(self, descricao: str, valor: int | float) -> None:
        """
        Adiciona uma contribuição à simulação.

        Parameters
        ----------
        descricao: str
            Descrição da contribuição.
        valor: int | float
            Valor da contribuição.
        """

        contribuicao = Contribuicao(descricao, valor)
        self.total_deducoes += contribuicao.valor
        self.contribuicoes.append(contribuicao)

    def get_valor_liquido(self) -> float | int:
        """
        Retorna o valor líquido da simulação.

        Returns
        -------
        float | int
            Valor líquido da simulação.
        """

        return self.total_rendimento - self.total_deducoes

    def get_valor_imposto(self) -> float | int:
        """
        Retorna o valor do imposto devido na simulação.

        Returns
        -------
        float | int
            Valor do imposto devido na simulação.
        """

        valor_liquido = self.get_valor_liquido()
        valor_imposto = 0

        valores = Valores()
        valor_imposto += valores.get_valor_faixa5(valor_liquido)
        valor_imposto += valores.get_valor_faixa4(valor_liquido)
        valor_imposto += valores.get_valor_faixa3(valor_liquido)
        valor_imposto += valores.get_valor_faixa2(valor_liquido)

        return valor_imposto

    def get_aliquota(self) -> float:
        """
        Retorna a alíquota efetiva da simulação.

        Returns
        -------
        float
            Alíquota efetiva da simulação.
        """

        valor_imposto = self.get_valor_imposto()
        aliquotaEfetiva = (
            floor(valor_imposto / self.get_total_rendimento() * 10000) / 100
        )
        return aliquotaEfetiva
