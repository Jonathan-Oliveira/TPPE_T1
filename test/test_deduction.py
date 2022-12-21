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

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"descricao": "", "valor": 100},
                ("Descrição em branco: "),
            ),
            (
                {"descricao": "    ", "valor": 100},
                ("Descrição em branco:    "),
            ),
            (
                {"descricao": None, "valor": 100},
                ("Descrição em branco: None"),
            ),
            # pytest.param("6*9", 42, marks=pytest.mark.xfail),
        ],
    )
    def test_descricao_em_branco(self, test_input, expected):
        with pytest.raises(DescricaoEmBrancoException, match=expected):
            Deducao(
                descricao=test_input.get("descricao"),
                valor=test_input.get("valor"),
            )
