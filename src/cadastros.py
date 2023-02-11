from simulacao import Simulacao
import time
from constants import (
    OPCAO_CADASTRAR_RENDIMENTO,
    OPCAO_CADASTRAR_DEDUCAO,
    OPCAO_CADASTRAR_DEPENDENTE,
    OPCAO_CADASTRAR_PENSAO,
    OPCAO_CALCULAR_IMPOSTO,
    OPCAO_SAIR,
)
class Cadastros(Simulacao,time):
    def cadastrar_rendimento(simulacao):
        descricao = input("Digite a descrição do rendimento: ")
        valor = float(input("Digite o valor do rendimento: "))
        simulacao.adiciona_rendimento(descricao, valor)
        print("Rendimento cadastrado com sucesso!")


    def cadastrar_deducao(simulacao):
        descricao = input("Digite a descrição da dedução: ")
        valor = float(input("Digite o valor da dedução: "))
        simulacao.adiciona_deducao(descricao, valor)
        print("Dedução cadastrada com sucesso!")


    def cadastrar_dependente(simulacao):
        nome = input("Digite o nome do dependente: ")
        data_nascimento = input("Digite a data de nascimento do dependente (dia/mes/ano): ")
        simulacao.adiciona_dependente(nome, data_nascimento)
        print("Dependente cadastrado com sucesso!")


    def cadastrar_pensao(simulacao):
        valor = float(input("Digite o valor da pensão: "))
        simulacao.adiciona_pensao(valor)


    def calcular_imposto(simulacao):
        print(f"Valor líquido: {simulacao.get_valor_liquido()}")
        print(f"Valor imposto: {simulacao.get_valor_imposto()}")