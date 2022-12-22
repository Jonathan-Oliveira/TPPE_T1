from rendimento import (
    Rendimento,
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException,
)
import pytest


class TestRendimentos:
    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"descricao": "Salario", "valor": 1200},
                {"descricao": "Salario", "valor": 1200},
            ),
            (
                {"descricao": "aluguel", "valor": 800},
                {"descricao": "aluguel", "valor": 800},
            ),
            (
                {"descricao": "ações", "valor": 1000},
                {"descricao": "ações", "valor": 1000},
            ),
        ],
    )
    def test_cadastro(self, test_input, expected):
        rendimento = Rendimento(
            descricao=test_input.get("descricao"),
            valor=test_input.get("valor"),
        )
        assert rendimento.valor == expected.get("valor")
        assert rendimento.descricao == expected.get("descricao")

    def test_descricao_em_branco(self):
        with pytest.raises(DescricaoEmBrancoException):
            Rendimento(descricao="", valor=1200)

    def test_descricao_em_branco2(self):
        with pytest.raises(DescricaoEmBrancoException):
            Rendimento(descricao="   ", valor=1200)

    def test_descricao_em_branco3(self):
        with pytest.raises(DescricaoEmBrancoException):
            Rendimento(descricao=None, valor=800)

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"descricao": "Salario", "valor": -100},
                ("Valor inválido: -100"),
            ),
            (
                {"descricao": "Salario", "valor": -3000},
                ("Valor inválido: -3000"),
            ),
            (
                {"descricao": "Salario", "valor": None},
                ("Valor inválido: None"),
            ),
            (
                {"descricao": "Salario", "valor": "abc"},
                ("Valor inválido: abc"),
            ),
        ],
    )
    def test_valores_invalidos(self, test_input, expected):
        with pytest.raises(ValorRendimentoInvalidoException, match=expected):
            Rendimento(
                descricao=test_input.get("descricao"),
                valor=test_input.get("valor"),
            )
