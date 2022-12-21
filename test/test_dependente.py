from dependente import Dependente
import pytest


class TestDependentes:

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"nome": "Pessoa", "dataNascimento": "19/10/1999"},
                {"nome": "Pessoa", "dataNascimento": "19/10/1999"},
            ),
            (
                {"nome": "alguem", "dataNascimento": "19/10/2000"},
                {"nome": "alguem", "dataNascimento": "19/10/2000"},
            ),
            (
                {"nome": "outro", "dataNascimento": "19/10/2042"},
                {"nome": "outro", "dataNascimento": "19/10/2042"},
            ),
        ],
    )

    def test_cadastro(self, test_input, expected):
        dependente = Dependente(
            nome=test_input.get("nome"),
            dataNascimento=test_input.get("dataNascimento")
        )
        assert dependente.nome == expected.get("nome")
        assert dependente.dataNascimento == expected.get("dataNascimento")
