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
            
        ],
    )
    def test_contribuicao(self, test_input, expected):
        contribuicao = Contribuicao(
            descricao=test_input.get("descricao"),
            valor=test_input.get("valor"),
        )
        assert contribuicao.valor == expected.get("valor")
        assert contribuicao.descricao == expected.get("descricao") 
        