from deducao import Deducao, DescricaoEmBrancoException

import pytest


class TestDecucoes:
    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"descricao": "Previdencia privada", "valor": 100},
                {"descricao": "Previdencia privada", "valor": 100},
            ),
            (
                {"descricao": "Funpresp", "valor": 800},
                {"descricao": "Funpresp", "valor": 800},
            ),
            (
                {"descricao": "Previdencia privada", "valor": 1000},
                {"descricao": "Previdencia privada", "valor": 1000},
            ),
            # pytest.param("6*9", 42, marks=pytest.mark.xfail),
        ],
    )
    def test_cadastro(self, test_input, expected):
        deducao = Deducao(
            descricao=test_input.get("descricao"),
            valor=test_input.get("valor"),
        )
        assert deducao.valor == expected.get("valor")
        assert deducao.descricao == expected.get("descricao")

    def test_descricao_em_branco(self):
        with pytest.raises(DescricaoEmBrancoException):
            Deducao(descricao="", valor=100)

    def test_descricao_em_branco2(self):
        with pytest.raises(DescricaoEmBrancoException):
            Deducao(descricao="   ", valor=100)
