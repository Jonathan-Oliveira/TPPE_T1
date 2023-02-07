from rendimento import Rendimento
from deducao import Deducao
from dependente import Dependente
from pensao import Pensao
from contribuicao import Contribuicao
from valores import Valores
from math import floor

class Simulacao:
    def __init__(
        self,
        rendimentos: list[Rendimento] = [],
        deducoes: list[Deducao] = [],
        dependentes: list[Dependente] = [],
        pensoes: list[Pensao] = [],
        contribuicoes: list[Contribuicao] = [],
    ):
        self.rendimentos = rendimentos
        self.deducoes = deducoes
        self.dependentes = dependentes
        self.pensoes = pensoes
        self.contribuicoes = contribuicoes

        self.total_rendimento: float | int = 0
        self.total_deducoes: float | int = 0

    def adiciona_rendimento(self, descricao: str, valor: float):
        rendimento = Rendimento(descricao, valor)
        self.rendimentos.append(rendimento)
        self.total_rendimento += valor

    def get_total_rendimento(self):
        return self.total_rendimento

    def adiciona_deducao(self, descricao: str, valor: float):
        deducao = Deducao(descricao, valor)
        self.deducoes.append(deducao)
        self.total_deducoes += valor

    def adiciona_pensao(self, valor: float):
        pensao = Pensao(valor)
        self.pensoes.append(pensao)
        self.total_deducoes += valor

    def get_total_deducao(self):
        return self.total_deducoes

    def adiciona_dependente(self, nome: str, dataNascimento: str):
        dependente = Dependente(nome, dataNascimento)
        self.total_deducoes += dependente.valor
        self.dependentes.append(dependente)

    def adiciona_contribuicao(self, descricao: str, valor: int | float):
        contribuicao = Contribuicao(descricao, valor)
        self.total_deducoes += contribuicao.valor
        self.contribuicoes.append(contribuicao)

    def get_valor_liquido(self):
        return self.total_rendimento - self.total_deducoes

    def get_valor_imposto(self):
        valor_liquido = self.get_valor_liquido()
        valor_imposto = 0

        valores = Valores()
        valor_imposto += valores.get_valor_faixa5(valor_liquido)
        valor_imposto += valores.get_valor_faixa4(valor_liquido)
        valor_imposto += valores.get_valor_faixa3(valor_liquido)
        valor_imposto += valores.get_valor_faixa2(valor_liquido)

        return valor_imposto
        
    def get_aliquota(self):
        valor_imposto = self.get_valor_imposto()
        aliquotaEfetiva = (
            floor(valor_imposto / self.get_total_rendimento() * 10000) / 100
        )
        return aliquotaEfetiva