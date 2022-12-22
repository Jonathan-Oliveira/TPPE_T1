from rendimento import Rendimento, DescricaoEmBrancoException, ValorRendimentoInvalidoException
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
                # pytest.param("6*9", 42, marks=pytest.mark.xfail),
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
    
    def test_valores_invalidos(self):
        with pytest.raises(
            ValorRendimentoInvalidoException, match="Valor inválido: -100"
        ):
            Rendimento(
                descricao="Salario",
                valor=-100,
            )
    def test_valores_invalidos_2(self):
        with pytest.raises(
            ValorRendimentoInvalidoException, match="Valor inválido: -3000"
        ):
            Rendimento(
                descricao="Salario",
                valor=-2000,
            )    

    def test_valores_invalidos_3(self):
        with pytest.raises(
            ValorRendimentoInvalidoException, match="Valor inválido: None"
        ):
            Rendimento(
                descricao="Salario",
                valor=None,
            )

    def test_valores_invalidos_4(self):
        with pytest.raises(
            ValorRendimentoInvalidoException, match="Valor inválido: abc"
        ):
            Rendimento(
                descricao="Salario",
                valor="abc",
            )
