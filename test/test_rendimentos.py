from rendimento import Rendimento

class TestRendimentos:
    
    def test_cadastro(self):
        rendimento = Rendimento(descricao = "Salario", valor =1200)
        assert rendimento.descricao == "Salario"
        assert rendimento.valor == 1200

     def test_cadastro2(self):
        rendimento = rendimento(descricao="aluguel", valor=800)
        assert rendimento.valor == 800
        assert rendimento.descricao == "aluguel"
    


