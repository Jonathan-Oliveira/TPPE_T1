from dependente import Dependente, NomeEmBrancoException, DataInvalidaException
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
            dataNascimento=test_input.get("dataNascimento"),
        )
        assert dependente.nome == expected.get("nome")
        assert dependente.dataNascimento == expected.get("dataNascimento")

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"nome": "", "dataNascimento": "19/10/1999"},
                ("Nome em branco: "),
            ),
            (
                {"nome": "   ", "dataNascimento": "19/10/2000"},
                ("Nome em branco:    "),
            ),
            (
                {"nome": None, "dataNascimento": "19/10/2042"},
                ("Nome em branco: None"),
            ),
        ],
    )
    def test_nome_em_branco(self, test_input, expected):
        with pytest.raises(NomeEmBrancoException, match=expected):
            Dependente(
                nome=test_input.get("nome"),
                dataNascimento=test_input.get("dataNascimento"),
            )

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {"nome": "Pessoa", "dataNascimento": "29/02/2022"},
                ("Data Invalida: 29/02/2022"),
            ),
            (
                {"nome": "alguem", "dataNascimento": "42/01/2000"},
                ("Data Invalida: 42/01/2000"),
            ),
            (
                {"nome": "outro", "dataNascimento": "19/23/2001"},
                ("Data Invalida: 19/23/2001"),
            ),
        ],
    )
    def test_data_invalida(self, test_input, expected):
        with pytest.raises(DataInvalidaException, match=expected):
            Dependente(
                nome=test_input.get("nome"),
                dataNascimento=test_input.get("dataNascimento"),
            )
