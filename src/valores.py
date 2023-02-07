class Valores:

    def __init__(
        self,
        lim_faixa1: float = 1903.98,
        lim_faixa2: float = 922.67,
        lim_faixa3: float = 924.40,
        lim_faixa4: float = 913.63,
        lim_faixa5: float = 4664.68,

        cento_faixa2: float = 0.075,
        cento_faixa3: float = 0.15,
        cento_faixa4: float = 0.225,
        cento_faixa5: float = 0.275,
    ):
        self.lim_faixa1 = lim_faixa1
        self.lim_faixa2 = lim_faixa2
        self.lim_faixa3 = lim_faixa3
        self.lim_faixa4 = lim_faixa4
        self.lim_faixa5 = self.lim_faixa1 + self.lim_faixa2 + self.lim_faixa3 + self.lim_faixa4

        self.cento_faixa2 = cento_faixa2
        self.cento_faixa3 = cento_faixa3
        self.cento_faixa4 = cento_faixa4
        self.cento_faixa5 = cento_faixa5


    def calcular_valor_faixa(self, valor_liquido, limite_abaixo, limite_faixa, porcentagem_faixa):
        if valor_liquido > limite_abaixo:
            valor = min(valor_liquido - limite_abaixo, limite_faixa)
            return valor * porcentagem_faixa
        return 0

    def get_valor_faixa5(self, valor_liquido):
        return self.calcular_valor_faixa(valor_liquido, self.lim_faixa5, float('inf'), self.cento_faixa5)

    def get_valor_faixa4(self, valor_liquido):
        limite_abaixo = self.lim_faixa3 + self.lim_faixa2 + self.lim_faixa1
        return self.calcular_valor_faixa(valor_liquido, limite_abaixo, self.lim_faixa4, self.cento_faixa4)

    def get_valor_faixa3(self, valor_liquido):
        limite_abaixo = self.lim_faixa2 + self.lim_faixa1
        return self.calcular_valor_faixa(valor_liquido, limite_abaixo, self.lim_faixa3, self.cento_faixa3)

    def get_valor_faixa2(self, valor_liquido):
        return self.calcular_valor_faixa(valor_liquido, self.lim_faixa1, self.lim_faixa2, self.cento_faixa2)
