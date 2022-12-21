from deducao import (
    Deducao,
    DescricaoEmBrancoException,
    ValorDeducaoInvalidoException,
)
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
        ],
    )
    def test_descricao_em_branco(self, test_input, expected):
        with pytest.raises(DescricaoEmBrancoException, match=expected):
            Deducao(
                descricao=test_input.get("descricao"),
                valor=test_input.get("valor"),
            )

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"descricao": "Previdencia privada", "valor": -100},
                ("Valor inválido: -100"),
            ),
            (
                {"descricao": "Previdencia privada", "valor": -3000},
                ("Valor inválido: -3000"),
            ),
            (
                {"descricao": "Previdencia privada", "valor": None},
                ("Valor inválido: None"),
            ),
            (
                {"descricao": "Previdencia privada", "valor": "abc"},
                ("Valor inválido: abc"),
            ),
        ],
    )
    def test_valores_invalidos(self, test_input, expected):
        with pytest.raises(ValorDeducaoInvalidoException, match=expected):
            Deducao(
                descricao=test_input.get("descricao"),
                valor=test_input.get("valor"),
            )
