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

    def test_valores_invalidos(self):
        with pytest.raises(
            ValorDeducaoInvalidoException, match="Valor inválido: -100"
        ):
            Deducao(
                descricao="Previdencia privada",
                valor=-100,
            )

    def test_valores_invalidos_2(self):
        with pytest.raises(
            ValorDeducaoInvalidoException, match="Valor inválido: -3000"
        ):
            Deducao(
                descricao="Previdencia privada",
                valor=-3000,
            )

    def test_valores_invalidos_3(self):
        with pytest.raises(
            ValorDeducaoInvalidoException, match="Valor inválido: None"
        ):
            Deducao(
                descricao="Previdencia privada",
                valor=None,
            )

    def test_valores_invalidos_4(self):
        with pytest.raises(
            ValorDeducaoInvalidoException, match="Valor inválido: abc"
        ):
            Deducao(
                descricao="Previdencia privada",
                valor="abc",
            )
