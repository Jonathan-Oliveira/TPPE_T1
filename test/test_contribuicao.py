from contribuicao import Contribuicao

import pytest

class TestContribuicao:
    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"descricao": "Aposentadoria", "valor": 100},
                {"descricao": "Aposentadoria", "valor": 100},
                
            ),
            (
                {"descricao": "Auxílio-alimentacao", "valor": 800},
                {"descricao": "Auxílio-alimentacao", "valor": 800},
            ),
            (
                {"descricao": "Auxílio-Transporte", "valor": 1000},
                {"descricao": "Auxílio-Transporte", "valor": 1000},
            ),
        ],
    )
    def test_contribuicao(self, test_input, expected):
        contribuicao = Contribuicao(
            descricao=test_input.get("descricao"),
            valor=test_input.get("valor"),
        )
        assert contribuicao.valor == expected.get("valor")
        assert contribuicao.descricao == expected.get("descricao") 
        