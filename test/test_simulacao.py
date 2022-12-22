from simulacao import Simulacao

import pytest


class TestSimulacao:
    def test_calcula_imposto(self) -> None:
        simulacao = Simulacao()
        simulacao.adiciona_rendimento(descricao="Salario", valor=1500.0)
        simulacao.adiciona_deducao(
            descricao="Previdencia privada", valor=100.0
        )
        simulacao.adiciona_deducao(descricao="Funpresp", valor=800.0)
        simulacao.adiciona_dependente(
            nome="Fulano da silva", dataNascimento="21/05/2010"
        )
        simulacao.adiciona_pensao(valor=200.50)
        simulacao.adiciona_contribuicao(
            descricao="Aposentadoria", valor=100.40
        )

        assert simulacao.total_rendimento == 1500.0
        assert simulacao.total_deducoes == 1390.49
        assert round(simulacao.get_valor_liquido(), 2) == 109.51
        assert simulacao.get_valor_imposto() == 0.0
