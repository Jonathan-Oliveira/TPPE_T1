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


def mostra_menu():
    print("1 - Cadastrar rendimento")
    print("2 - Cadastrar dedução")
    print("3 - Cadastrar dependente")
    print("4 - Cadastrar pensão")
    print("5 - Calcular imposto de renda")
    print("6 - Sair")


def limpa_tela():
    print("\n" * 100)


def ler_opcao():
    return input("Digite a opção desejada: ")


def validar_entrada_do_usuario(user_input):
    if user_input not in [
        OPCAO_CADASTRAR_RENDIMENTO,
        OPCAO_CADASTRAR_DEDUCAO,
        OPCAO_CADASTRAR_DEPENDENTE,
        OPCAO_CADASTRAR_PENSAO,
        OPCAO_CALCULAR_IMPOSTO,
        OPCAO_SAIR,
    ]:
        print("Opção inválida")
        return False
    return True


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


def aplicar_opcao(opcao, simulacao):
    if opcao == OPCAO_CADASTRAR_RENDIMENTO:
        cadastrar_rendimento(simulacao)
    elif opcao == OPCAO_CADASTRAR_DEDUCAO:
        cadastrar_deducao(simulacao)
    elif opcao == OPCAO_CADASTRAR_DEPENDENTE:
        cadastrar_dependente(simulacao)
    elif opcao == OPCAO_CADASTRAR_PENSAO:
        cadastrar_pensao(simulacao)
    elif opcao == OPCAO_CALCULAR_IMPOSTO:
        calcular_imposto(simulacao)
    elif opcao == "6":
        exit(0)


if __name__ == "__main__":
    simulacao = Simulacao()
    try:
        while True:
            mostra_menu()
            opcao = ler_opcao()
            if not validar_entrada_do_usuario(opcao):
                continue
            if opcao == OPCAO_SAIR:
                print("Saindo...")
                exit(0)
            else:
                aplicar_opcao(opcao, simulacao)
            time.sleep(1)
            limpa_tela()
    except KeyboardInterrupt:
        limpa_tela()
        print("\nSaindo...")
        time.sleep(1)
