import os
import sys
import pytest

try:
    sys.path.append(os.getcwd() + "/src")
except Exception:
    pass

from simulacao import Simulacao

@pytest.fixture(scope="function")
def simulacao():
    simulacao = Simulacao()
    simulacao.adiciona_deducao(descricao="Previdencia privada", valor=100.0)
    simulacao.adiciona_deducao(descricao="Funpresp", valor=800.0)
    simulacao.adiciona_deducao(descricao="Previdencia privada", valor=1000.42)
    simulacao.adiciona_dependente(
        descricao="Filho", dataNascimento="21/05/2010"
    )
    simulacao.adiciona_pensao(descricao="Filho", valor=100)
