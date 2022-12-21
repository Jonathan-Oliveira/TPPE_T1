from dependente import Dependente
import pytest


class TestDependentes:

    def test_cadastro(self, nome = "caio", dataNascimento = "19/10/1999"):
        dependente = Dependente(nome, dataNascimento)
        assert dependente.nome == "caio"
        assert dependente.dataNascimento == "19/10/1999"

    def test_cadastro2(self, nome = "alguem", dataNascimento = "19/10/2000"):
        dependente = Dependente(nome, dataNascimento)
        assert dependente.nome == "alguem"
        assert dependente.dataNascimento == "19/10/2000"

    def test_cadastro2(self, nome = "outro", dataNascimento = "19/10/2042"):
        dependente = Dependente(nome, dataNascimento)
        assert dependente.nome == "outro"
        assert dependente.dataNascimento == "19/10/2042"