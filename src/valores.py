from math import floor

class valores:


    def get_valor_faixa5(self, valor_liquido,lim_faixa5,cento_faixa5):
        if valor_liquido > lim_faixa5:
            valor = valor_liquido - lim_faixa5
            return valor * cento_faixa5
        return 0

    def get_valor_faixa4(self, valor_liquido,lim_faixa1,lim_faixa2,lim_faixa3,lim_faixa4,cento_faixa4):
        if valor_liquido > lim_faixa3 + lim_faixa2 + lim_faixa1:
            valor = min((valor_liquido - lim_faixa3 + lim_faixa2 + lim_faixa1), lim_faixa4)
            return valor * cento_faixa4
        return 0
    
    def get_valor_faixa3(self, valor_liquido,lim_faixa1,lim_faixa2,lim_faixa3,cento_faixa3):
        if valor_liquido > lim_faixa2 + lim_faixa1:
            valor = min((valor_liquido - lim_faixa2 + lim_faixa1), lim_faixa3)
            return  valor * cento_faixa3
        return 0

    def get_valor_faixa2(self, valor_liquido, lim_faixa1, centro_faixa2,lim_faixa2):
        if valor_liquido>lim_faixa1:
            valor= min ((valor_liquido - lim_faixa1), lim_faixa2)   
            return valor*centro_faixa2
        return 0
