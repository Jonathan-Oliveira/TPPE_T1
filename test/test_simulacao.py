from simulacao import Simulacao

import pytest


class TestSimulacao:
    # @pytest.mark.parametrize("test_input, expected", [(), (), ()])
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
        assert simulacao.get_aliquota() == 0.0

    @pytest.mark.parametrize(
        "rendimentos, deducoes, dependentes, pensoes, contribuicoes, expected",
        [
            (
                # Rendimentos caso0
                [
                    {"descricao": "Salario", "valor": 2000.0},
                    {"descricao": "Salario", "valor": 3000.0},
                ],
                # Deducao caso0
                [
                    {"descricao": "Previdencia privada", "valor": 100.0},
                    {"descricao": "Previdencia privada", "valor": 300.0},
                ],
                # Dependente caso0
                [
                    {
                        "nome": "Fulano da silva",
                        "dataNascimento": "21/05/2010",
                    },
                    {
                        "nome": "Silva de Fulano",
                        "dataNascimento": "12/06/2006",
                    },
                ],
                # Pensao caso0
                [{"valor": 200.50}, {"valor": 140.50}],
                # Contribuicao caso0
                [
                    {"descricao": "Aposentadoria", "valor": 100.40},
                    {"descricao": "Aposentadoria", "valor": 320.40},
                ],
                # Expected caso0
                {
                    "total_rendimento": 5000.0,
                    "total_deducoes": 1540.98,
                    "valor_liquido": 3459.02,
                    "valor_imposto": 164.06,
                    "aliquota": 3.28,
                },
            ),
            (
                # Rendimentos caso1
                [
                    {"descricao": "Salario", "valor": 500.0},
                    {"descricao": "Salario", "valor": 300.0},
                ],
                # Deducao caso1
                [
                    {"descricao": "Previdencia privada", "valor": 50.0},
                    {"descricao": "Funpresp", "valor": 140.0},
                ],
                # Dependente caso1
                [{"nome": "Sicrano Jorge", "dataNascimento": "08/05/2000"}],
                # Pensao caso1
                [],
                # Contribuicao caso1
                [{"descricao": "Aposentadoria", "valor": 50.20}],
                # Expected caso1
                {
                    "total_rendimento": 800.0,
                    "total_deducoes": 429.79,
                    "valor_liquido": 370.21,
                    "valor_imposto": 0.0,
                    "aliquota": 0.0,
                },
            ),
            (
                # Rendimentos caso2
                [
                    {"descricao": "Salario", "valor": 1500.0},
                ],
                # Deducao caso2
                [
                    {"descricao": "Previdencia privada", "valor": 100.0},
                    {"descricao": "Funpresp", "valor": 800.0},
                ],
                # Dependente caso2
                [
                    {
                        "nome": "Fulano da silva",
                        "dataNascimento": "21/05/2010",
                    },
                ],
                # Pensao caso2
                [{"valor": 200.50}],
                # Contribuicao caso2
                [
                    {"descricao": "Aposentadoria", "valor": 100.40},
                ],
                # Expected caso2
                {
                    "total_rendimento": 1500.0,
                    "total_deducoes": 1390.49,
                    "valor_liquido": 109.51,
                    "valor_imposto": 0.0,
                    "aliquota": 0.0,
                },
            ),
            (
                # Rendimentos caso3
                [
                    {"descricao": "Salario", "valor": 4664.0},
                    {"descricao": "Ações", "valor": 300.0},
                ],
                # Deducao caso3
                [
                    {"descricao": "Previdencia privada", "valor": 50.0},
                    {"descricao": "Previdencia privada", "valor": 140.0},
                ],
                # Dependente caso3
                [{"nome": "Sicrano Jorge", "dataNascimento": "08/05/2000"}],
                # Pensao caso3
                [{"valor": 0.09}],
                # Contribuicao caso3
                [{"descricao": "Aposentadoria", "valor": 50.20}],
                # Expected caso3
                {
                    "total_rendimento": 4964.0,
                    "total_deducoes": 429.88,
                    "valor_liquido": 4534.12,
                    "valor_imposto": 384.05,
                    "aliquota": 7.7,
                },
            ),
        ],
    )
    def test_imposto_parametizado(
        self,
        rendimentos,
        deducoes,
        dependentes,
        pensoes,
        contribuicoes,
        expected,
    ):
        simulacao = Simulacao()
        for rendimento in rendimentos:
            simulacao.adiciona_rendimento(**rendimento)

        for deducao in deducoes:
            simulacao.adiciona_deducao(**deducao)

        for dependentes in dependentes:
            simulacao.adiciona_dependente(**dependentes)

        for pensao in pensoes:
            simulacao.adiciona_pensao(**pensao)

        for contribuicao in contribuicoes:
            simulacao.adiciona_contribuicao(**contribuicao)

        print(simulacao.dependentes[0].nome)
        assert simulacao.total_rendimento == expected.get("total_rendimento")
        assert simulacao.total_deducoes == expected.get("total_deducoes")
        assert round(simulacao.get_valor_liquido(), 2) == expected.get(
            "valor_liquido"
        )
        assert round(simulacao.get_valor_imposto(), 2) == expected.get(
            "valor_imposto"
        )