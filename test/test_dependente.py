from dependente import Dependente
import pytest


class TestDependentes:

    def test_cadastro(self, nome = "caio", dataNascimento = "19/10/1999"):
        dependente = Dependente(nome, dataNascimento)
        assert dependente.valor == "caio"
        assert dependente.descricao == "19/10/1999"