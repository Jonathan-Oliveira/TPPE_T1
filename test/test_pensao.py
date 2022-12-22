from pensao import (
    Pensao,
    ValorPensaoEmBrancoException,
    ValorPensaoInvalidaException,
)
import pytest


class TestDecucoes:
    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"valor": 100},
                {"valor": 100},
            ),
            (
                { "valor": 200},
                { "valor": 200},
            ),
            (
                {"valor": 500},
                {"valor": 500},
            ),
        ],
    )
    def test_cadastro(self, test_input, expected):
        pensao = Pensao(
            valor_pensao=test_input.get("valor"),
        )
        assert pensao.valor == expected.get("valor")

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"valor": 100},
                ("Valor em branco: "),
            ),
            (
                {"valor": 200},
                ("Valor em branco: "),
            ),
            (
                {"valor": None, "valor": 100},
                ("Valor em branco: None"),
            ),
        ],
    )
    def test_pensao_em_branco(self, test_input, expected):
        with pytest.raises(ValorPensaoEmBrancoException, match=expected):
            Pensao(
                valor=test_input.get("valor"),
            )

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"valor": 50, "valor": -100},
                ("Valor inválido: -100"),
            ),
            (
                {"valor": 150, "valor": -3000},
                ("Valor inválido: -3000"),
            ),
            (
                {"valor": 550, "valor": None},
                ("Valor inválido: None"),
            ),
            (
                {"valor": 200, "valor": "abc"},
                ("Valor inválido: abc"),
            ),
        ],
    )
    def test_valores_invalidos(self, test_input, expected):
        with pytest.raises(ValorPensaoInvalidaException, match=expected):
            Pensao(
                valor=test_input.get("valor"),
            )
