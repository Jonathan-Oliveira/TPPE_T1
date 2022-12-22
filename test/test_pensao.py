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
                {"valor_pensao": 100.40},
                {"valor_pensao": 100.40},
            ),
            (
                {"valor_pensao": 200.57},
                {"valor_pensao": 200.57},
            ),
            (
                {"valor_pensao": 500},
                {"valor_pensao": 500},
            ),
        ],
    )
    def test_cadastro(self, test_input, expected):
        pensao = Pensao(
            valor_pensao=test_input.get("valor_pensao"),
        )
        assert pensao.valor_pensao == expected.get("valor_pensao")

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"valor_pensao": ""},
                ("Valor em branco: "),
            ),
            (
                {"valor_pensao": None},
                ("Valor em branco: None"),
            ),
        ],
    )
    def test_pensao_em_branco(self, test_input, expected):
        with pytest.raises(ValorPensaoEmBrancoException, match=expected):
            Pensao(
                valor_pensao=test_input.get("valor_pensao"),
            )

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"valor_pensao": -100},
                ("Valor inválido: -100"),
            ),
            (
                {"valor_pensao": -3000},
                ("Valor inválido: -3000"),
            ),
            (
                {"valor_pensao": "abc"},
                ("Valor inválido: abc"),
            ),
        ],
    )
    def test_valores_invalidos(self, test_input, expected):
        with pytest.raises(ValorPensaoInvalidaException, match=expected):
            Pensao(
                valor_pensao=test_input.get("valor_pensao"),
            )
