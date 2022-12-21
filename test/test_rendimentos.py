from rendimento import Rendimento

class TestRendimentos:
    def test_cadastro(self):
        rendimento = Rendimento(descricao = "Salario",valor =1200)
        assert rendimento.descricao == "Salario"
        assert rendimento.valor == 1200


