from rendimento import Rendimento
from deducao import Deducao
from dependente import Dependente
from pensao import Pensao
from contribuicao import Contribuicao

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
        lim_faixa1 = 1903.98
        lim_faixa2 = 922.67
        lim_faixa3 = 924.40
        lim_faixa4 = 913.63
        lim_faixa5 = lim_faixa1 + lim_faixa2 + lim_faixa3 + lim_faixa4

        cento_faixa2 = 0.075
        cento_faixa3 = 0.15
        cento_faixa4 = 0.225
        cento_faixa5 = 0.275

        valor_liquido = self.get_valor_liquido()
        valor_imposto = 0

        if valor_liquido > lim_faixa5:
            valor = valor_liquido - lim_faixa5
            valor_imposto += valor * cento_faixa5

        if valor_liquido > lim_faixa3 + lim_faixa2 + lim_faixa1:
            valor = min(
                (valor_liquido - lim_faixa3 + lim_faixa2 + lim_faixa1),
                lim_faixa4,
            )
            valor_imposto += valor * cento_faixa4

        if valor_liquido > lim_faixa2 + lim_faixa1:
            valor = min((valor_liquido - lim_faixa2 + lim_faixa1), lim_faixa3)
            valor_imposto += valor * cento_faixa3

        if valor_liquido > lim_faixa1:
            valor = min((valor_liquido - lim_faixa1), lim_faixa2)
            valor_imposto += valor * cento_faixa2

        return valor_imposto

    def get_aliquota(self):
        valor_imposto = self.get_valor_imposto()
        aliquotaEfetiva = (
            floor(valor_imposto / self.get_total_rendimento() * 10000) / 100
        )
        return aliquotaEfetiva
