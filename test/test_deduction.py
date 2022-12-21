from deducao import Deducao


class TestDecucoes:
    def test_cadastro(self):
        deducao = Deducao(descricao="Previdencia privada", valor=100)
        assert deducao.valor == 100
        assert deducao.descricao == "Previdencia privada"
