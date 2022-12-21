from deducao import Deducao


class TestDecucoes:
    def test_cadastro(self):
        deducao = Deducao(descricao="Previdencia privada", valor=100)
        assert deducao.valor == 100
        assert deducao.descricao == "Previdencia privada"

    def test_cadastro2(self):
        deducao = Deducao(descricao="Funpresp", valor=800)
        assert deducao.valor == 800
        assert deducao.descricao == "Funpresp"
