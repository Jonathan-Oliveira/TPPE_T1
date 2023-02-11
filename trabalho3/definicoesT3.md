# TP3 - Qualidade do projeto de código


## Alunos

| Matrícula  |        Aluno           |
| ---------- | ---------------------- |
| 18/0074741 | Caio Martins           |
| 18/0103580 | Jonathan Jorge         |
| 18/0103792 | Júlia Farias           |
| 18/0105345 | Lucas Lima             |
| 19/0048760 | Wellington Jhonathan   |


## Sobre
Um projeto bem desenvolvido tem como objetivo ser mais flexível e resistente a mudanças futuras. Isso significa que ele deve ser fácil de ser modificado, entendido e consertado, além de ser menos suscetível a erros. Para isso, é necessário que o código tenha boa estrutura, seja claro e objetivo, possua alta coesão e baixo acoplamento, o que torna mais fácil entender e alterar. Com isso, bons projetos são aqueles que possuem as seguintes características:

* **Simplicidade:** significa que o projeto deve ser fácil de entender, manter e modificar, sem muita complexidade desnecessária.
* **Elegância:** se refere ao uso eficiente e bem pensado de recursos e estruturas de programação, para produzir soluções claras e eficazes.
* **Modularidade:** se refere a separação lógica do código em módulos independentes e bem definidos, com baixo acoplamento (dependência mínima entre os módulos) e alta coesão (cada módulo tem uma responsabilidade clara).
* **Boas interfaces:** são as formas de comunicação entre os módulos, que devem ser claras, estáveis e consistentes para facilitar a integração e manutenção do projeto.
* **Extensibilidade:** significa que o projeto deve ser projetado para permitir facilmente a adição de novas funcionalidades e ajustes, sem prejudicar o funcionamento existente.
* **Ausência de duplicidades:** se refere à evitação de código duplicado ou redundante, o que torna o projeto mais fácil de manter e menos propenso a erros.
* **Portabilidade:** significa que o projeto deve ser projetado para ser executado em diferentes sistemas e ambientes sem mudanças significativas.
* **Idiomático:** se refere ao uso de padrões e convenções comuns da linguagem de programação escolhida, para tornar o código mais fácil de entender e manter para os desenvolvedores familiarizados com a linguagem.
* **Boa documentação:** se refere à documentação clara e completa do projeto, incluindo descrições de design, código, interfaces e processos, para facilitar a compreensão, manutenção e extensão do projeto.


# Refatoração

## Idiomático
Código idiomático é uma forma específica e recorrente de escrever código em uma determinada linguagem de programação, que é amplamente aceita como a maneira correta ou padrão de fazer algo. Isso pode incluir convenções de nomenclatura, estruturação de código, uso de determinadas bibliotecas ou ferramentas, e outros aspectos. Seguir o código idiomático em uma linguagem de programação pode ajudar a tornar o código mais legível, fácil de manter e padronizado para a comunidade de desenvolvedores.

O código idiomático em Python inclui convenções como:

* Uso de letras minúsculas e sublinhados para nomear variáveis, funções, etc. (exemplo: "my_variable").
* Indentação de 4 espaços para delimitar blocos de código.
* Uso de docstrings para documentar funções, classes, etc.
* Não usar caracteres especiais, exceto _ para nomear variáveis e funções.
* Usar aspas duplas para string com múltiplas linhas e aspas simples para strings simples.
* Evite usar comentários desnecessários, prefira escrever código claro e auto-explicativo.
* Importar bibliotecas no topo do arquivo e separá-las por uma linha em branco.

### Antes da Refatoração
``` python
from datetime import datetime
from deducao import Deducao
from typing import Any



class Dependente(Deducao):
    def __init__(self, nome: str, dataNascimento: str) -> None:
        super().__init__("Dependente", 189.59)
        if not nome or not nome.strip():
            raise NomeEmBrancoException(nome)
        self.nome = nome

        try:
            datetime.strptime(dataNascimento, "%d/%m/%Y")
        except ValueError:
            raise DataInvalidaException(dataNascimento)

        self.dataNascimento = dataNascimento
```
### Depois da Refatoração
``` python
from datetime import datetime

from deducao import Deducao

from typing import Any


class dependente(deducao):
    def __init__(self, nome: str, data_nascimento: str) -> None:
        super().__init__("dependente", 189.59)
        if not nome or not nome.strip():
            raise nome_em_branco_exception(nome)
        self.nome = nome

        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")
        except ValueError:
            raise data_invalida_exception(data_nascimento)

        self.data_nascimento = data_nascimento
```

## Ausência de duplicidades

Código duplicado é uma má prática de programação que consiste em escrever o mesmo trecho de código em mais de um lugar no seu projeto. Isso pode levar a vários problemas, como por exemplo:

* Manutenção complexa: se precisarmos mudar algum comportamento no projeto, precisaremos alterar o codigo duplicado em varios locais, o que aumenta o risco de erros e a complexidade da manutenção.

* Dificuldade de leitura: o código duplicado pode tornar o código difícil de entender, especialmente para outras pessoas que trabalham no mesmo projeto.

* Dificuldade de testar: a duplicação de código pode levar a testes redundante e confusos, dificultando a identificação de erros e bugs.

Duplicação de código é considerado um dos maiores "maus cheiros", as duplicatas podem indicar maus cheiros de diversas naturezas, como:

* "Long Method": se há código duplicado, é provável que existam métodos longos e complexos, o que pode tornar difícil entender o seu comportamento e onde o código duplicado está sendo usado.
* "God Class": se há muito código duplicado, isso pode indicar a existência de uma classe muito grande, que é responsável por muitas funcionalidades.
* "Feature Envy": se há código duplicado, é provável que exista uma classe que está sendo "enciumada" por outra classe, o que significa que esta classe está usando muito código da outra classe. Isso pode ser um sinal de que o código duplicado deve ser transferido para a classe correta.

Em resumo, o código duplicado pode ser indicativo de vários maus cheiros em programação, e é importante refatorá-lo para melhorar a qualidade do software e evitar problemas de manutenção e evolução.

Sendo assim, refatoramos a classe "Valores" que anteriormente se encontrava no estado abaixo:
``` python
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
```

A refatoração abaixo consiste na criação de uma função genérica para calcular o valor da faixa. Em vez de termos 4 funções diferentes para cada faixa, criamos uma única função que pode ser reutilizada.
A função "calculate_band_value" recebe 5 argumentos: o valor líquido, o limite da faixa, o cento da faixa e os limites das faixas anteriores. A partir destes argumentos, a função realiza o cálculo correto para a faixa em questão.
Com esta refatoração, é possível reduzir a quantidade de código duplicado e torná-lo mais claro e conciso. Além disso, a manutenção do código se torna mais fácil, pois basta mudar a lógica em uma única função para que as mudanças sejam refletidas em todas as faixas.
``` python
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
```
## Boa documentação

Uma boa documentação é essencial para garantir a qualidade e manutenibilidade do código. Deve ser escrita de forma clara, concisa e fácil de entender, e adaptada ao público certo - usuários finais ou desenvolvedores.Uma documentação pode ser a inclusão de comentários claros e precisos no código, documentação externa (por exemplo, arquivos README), documentação de API, entre outras coisas.

A boa documentação ajuda na estruturação e organização do código, tornando-o mais fácil de entender e manter. Isso é especialmente importante em projetos de grande escala ou em equipes, onde muitos desenvolvedores estão trabalhando em diferentes partes do código.

A claridade da documentação ajuda a evitar erros e aumenta a eficiência do desenvolvimento, pois os desenvolvedores não precisam gastar tempo tentando entender o que o código está fazendo. Além disso, a boa documentação torna mais fácil para outros desenvolvedores contribuírem para o projeto, pois eles sabem exatamente o que precisam fazer e como o código funciona.

A falta de documentação adequada pode ser um indicador de code smell, uma vez que dificulta a compreensão do código e pode levar a erros e problemas futuros. Além disso, uma má documentação também pode ser um indicador de falta de clareza, complexidade desnecessária e redundância.

Portanto, uma boa documentação é fundamental para garantir a qualidade e a manutenibilidade do código.

Por conseguinte,  escolhemos a classe `Simulação` para exemplificar uma boa documentação. Foi aplicado uma documentação docstring, que consiste em uma string incluída no início de uma classe, função ou método, com o intuito de descrever o objetivo, funcionamento, uso, entradas e saídas. Esse tipo de documentação pode ser visualizado de várias formas, como por exemplo, no terminal, no Jupyter Notebook entre outros e também é possível gerar uma documentação externa, como a do Sphinx. Existem vários padrões de documentação docstring, como o [Google](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings), [Numpy](https://numpydoc.readthedocs.io/en/latest/format.html), [reStructuredText](https://docutils.sourceforge.io/rst.html) (utilizado pelo Sphinx), e o próprio padrão do Python, que é o [PEP 257](https://peps.python.org/pep-0257/). Nessa refatoração, foi utilizado o padrão do Numpy. A seguir, temos um antes e depois da refatoração da classe `Simulação`:

### Antes da refatoração

``` python
class Simulacao:
    def __init__(
        self,
        rendimentos: list[Rendimento] = [],
        deducoes: list[Deducao] = [],
        dependentes: list[Dependente] = [],
        pensoes: list[Pensao] = [],
        contribuicoes: list[Contribuicao] = [],
    ):
        self.rendimentos = rendimentos
        self.deducoes = deducoes
        self.dependentes = dependentes
        self.pensoes = pensoes
        self.contribuicoes = contribuicoes

        self.total_rendimento: float | int = 0
        self.total_deducoes: float | int = 0

    def adiciona_rendimento(self, descricao: str, valor: float):
        rendimento = Rendimento(descricao, valor)
        self.rendimentos.append(rendimento)
        self.total_rendimento += valor

    def get_total_rendimento(self) -> float | int:
        return self.total_rendimento

    def adiciona_deducao(self, descricao: str, valor: float) -> None:
        deducao = Deducao(descricao, valor)
        self.deducoes.append(deducao)
        self.total_deducoes += valor

    def adiciona_pensao(self, valor: float) -> None:
        pensao = Pensao(valor)
        self.pensoes.append(pensao)
        self.total_deducoes += valor

    def get_total_deducao(self) -> float | int:
        return self.total_deducoes

    def adiciona_dependente(self, nome: str, dataNascimento: str) -> None:
        dependente = Dependente(nome, dataNascimento)
        self.total_deducoes += dependente.valor
        self.dependentes.append(dependente)

    def adiciona_contribuicao(self, descricao: str, valor: int | float) -> None:
        contribuicao = Contribuicao(descricao, valor)
        self.total_deducoes += contribuicao.valor
        self.contribuicoes.append(contribuicao)

    def get_valor_liquido(self) -> float | int:
        return self.total_rendimento - self.total_deducoes

    def get_valor_imposto(self) -> float | int:
        valor_liquido = self.get_valor_liquido()
        valor_imposto = 0

        valores = Valores()
        valor_imposto += valores.get_valor_faixa5(valor_liquido)
        valor_imposto += valores.get_valor_faixa4(valor_liquido)
        valor_imposto += valores.get_valor_faixa3(valor_liquido)
        valor_imposto += valores.get_valor_faixa2(valor_liquido)

        return valor_imposto

    def get_aliquota(self) -> float:
        valor_imposto = self.get_valor_imposto()
        aliquotaEfetiva = (
            floor(valor_imposto / self.get_total_rendimento() * 10000) / 100
        )
        return aliquotaEfetiva
```

### Depois da refatoração

``` python
class Simulacao:
    """
    Classe que representa uma simulação de cálculo de imposto de renda.

    Através da classe, é possível adicionar rendimentos, deduções, dependentes,
    pensões e contribuições, além de calcular o valor líquido e o valor do imposto
    devido.

    Attributes
    ---------
    rendimentos: list[Rendimento]
        Lista de rendimentos da simulação.
    deducoes: list[Deducao]
        Lista de deduções da simulação.
    dependentes: list[Dependente]
        Lista de dependentes da simulação.
    pensoes: list[Pensao]
        Lista de pensões da simulação.
    contribuicoes: list[Contribuicao]
        Lista de contribuições da simulação.
    total_rendimento: float | int
        Valor total dos rendimentos da simulação.
    total_deducoes: float | int
        Valor total das deduções da simulação.

    Methods
    -------
    adiciona_rendimento(descricao: str, valor: float) -> None
        Adiciona um rendimento à simulação.
    get_total_rendimento() -> float | int
        Retorna o valor total dos rendimentos da simulação.
    adiciona_deducao(descricao: str, valor: float) -> None
        Adiciona uma dedução à simulação.
    adiciona_pensao(valor: float) -> None
        Adiciona uma pensão à simulação.
    get_total_deducao() -> float | int
        Retorna o valor total das deduções da simulação.
    adiciona_dependente(nome: str, dataNascimento: str) -> None
        Adiciona um dependente à simulação.
    adiciona_contribuicao(descricao: str, valor: int | float) -> None
        Adiciona uma contribuição à simulação.
    get_valor_liquido() -> float | int
        Retorna o valor líquido da simulação.
    get_valor_imposto() -> float | int
        Retorna o valor do imposto devido da simulação.
    get_aliquota() -> float
        Retorna a alíquota efetiva da simulação.
    """

    def __init__(
        self,
        rendimentos: list[Rendimento] = [],
        deducoes: list[Deducao] = [],
        dependentes: list[Dependente] = [],
        pensoes: list[Pensao] = [],
        contribuicoes: list[Contribuicao] = [],
    ):
        """
        Construtor da classe Simulacao.

        Parameters
        ----------
        rendimentos: list[Rendimento]
            Lista de rendimentos da simulação.
        deducoes: list[Deducao]
            Lista de deduções da simulação.
        dependentes: list[Dependente]
            Lista de dependentes da simulação.
        pensoes: list[Pensao]
            Lista de pensões da simulação.
        contribuicoes: list[Contribuicao]
            Lista de contribuições da simulação.
        """
        
        self.rendimentos = rendimentos
        self.deducoes = deducoes
        self.dependentes = dependentes
        self.pensoes = pensoes
        self.contribuicoes = contribuicoes
        self.total_rendimento: float | int = 0
        self.total_deducoes: float | int = 0

    def adiciona_rendimento(self, descricao: str, valor: float) -> None:
        """
        Adiciona um rendimento à simulação.

        Parameters
        ----------
        descricao: str
          Descrição do rendimento.
        valor: float
          Valor do rendimento.
        """

        rendimento = Rendimento(descricao, valor)
        self.total_rendimento += rendimento.valor
        self.rendimentos.append(rendimento)

    def get_total_rendimento(self) -> float | int:
        """
        Retorna o valor total dos rendimentos da simulação.

        Returns
        -------
        float | int
            Valor total dos rendimentos da simulação.
        """
        
        return self.total_rendimento

    def adiciona_deducao(self, descricao: str, valor: float) -> None:
        """
        Adiciona uma dedução à simulação.

        Parameters
        ----------
        descricao: str
            Descrição da dedução.
        valor: float
            Valor da dedução.

        """

        deducao = Deducao(descricao, valor)
        self.deducoes.append(deducao)
        self.total_deducoes += valor

    def adiciona_pensao(self, valor: float) -> None:
        """
        Adiciona uma pensão à simulação.

        Parameters
        ----------
        valor: float
            Valor da pensão.
        """

        pensao = Pensao(valor)
        self.pensoes.append(pensao)
        self.total_deducoes += valor

    def get_total_deducao(self) -> float | int:
        """
        Retorna o valor total das deduções da simulação.

        Returns
        -------
        float | int
            Valor total das deduções da simulação.
        """
        
        return self.total_deducoes

    def adiciona_dependente(self, nome: str, dataNascimento: str) -> None:
        """
        Adiciona um dependente à simulação.

        Parameters
        ----------
        nome: str
            Nome do dependente.
        dataNascimento: str
            Data de nascimento do dependente.
        """

        dependente = Dependente(nome, dataNascimento)
        self.total_deducoes += dependente.valor
        self.dependentes.append(dependente)

    def adiciona_contribuicao(self, descricao: str, valor: int | float) -> None:
        """
        Adiciona uma contribuição à simulação.

        Parameters
        ----------
        descricao: str
            Descrição da contribuição.
        valor: int | float
            Valor da contribuição.
        """

        contribuicao = Contribuicao(descricao, valor)
        self.total_deducoes += contribuicao.valor
        self.contribuicoes.append(contribuicao)

    def get_valor_liquido(self) -> float | int:
        """
        Retorna o valor líquido da simulação.

        Returns
        -------
        float | int
            Valor líquido da simulação.
        """
        
        return self.total_rendimento - self.total_deducoes

    def get_valor_imposto(self) -> float | int:
        """
        Retorna o valor do imposto devido na simulação.

        Returns
        -------
        float | int
            Valor do imposto devido na simulação.
        """

        valor_liquido = self.get_valor_liquido()
        valor_imposto = 0

        valores = Valores()
        valor_imposto += valores.get_valor_faixa5(valor_liquido)
        valor_imposto += valores.get_valor_faixa4(valor_liquido)
        valor_imposto += valores.get_valor_faixa3(valor_liquido)
        valor_imposto += valores.get_valor_faixa2(valor_liquido)

        return valor_imposto

    def get_aliquota(self) -> float:
        """
        Retorna a alíquota efetiva da simulação.

        Returns
        -------
        float
            Alíquota efetiva da simulação.
        """
        
        valor_imposto = self.get_valor_imposto()
        aliquotaEfetiva = (
            floor(valor_imposto / self.get_total_rendimento() * 10000) / 100
        )
        return aliquotaEfetiva
```

## Modularidade

Modularidade está relacionada a capacidade de separar a funcionalidade de um programa em módulos independentes e intercambiáveis, de modo que cada um contenha tudo o que é necessário para executar apenas um aspecto da funcionalidade desejada, ela está ligada aos conceitos de coesão e acoplamento de código. Coesão é a medida de quão relacionadas ou focadas estão as responsabilidades de um elemento, quando se diz que um código possui alta coesão, significa que as suas classes serão mais enxutas e focadas, possuindo apenas uma responsabilidade.

Já o acoplamento é a medida de quanto um elemento está conectado, ou depende de outros elementos. Uma classe com forte acoplamento depende de outras classes, o que pode gerar fatores indesejáveis como baixa reutilização e maior impacto com mudanças, por isso que para termos de código a melhor opção é ter um baixo acoplamento. O acoplamento tem relação com a coesão, de forma inversamente proporcional, ou seja, quanto maior a coesão, menor o acoplamento.

As vantagens de modularizar o código incluem:

-Reutilização de código: os módulos podem ser reutilizados em outros projetos, o que economiza tempo e esforço.

-Melhor organização: a modularização permite que o código seja dividido em partes mais gerenciáveis, o que torna mais fácil de entender e manter.

-Facilidade de manutenção: com o código dividido em módulos, as mudanças em uma parte específica do programa não afetarão outras partes, o que torna a manutenção mais fácil e segura.

-Teste mais eficiente: a modularização permite que cada módulo seja testado individualmente, o que torna o processo de teste mais eficiente e menos propenso a erros.

-Colaboração mais eficiente: a modularização permite que diferentes equipes de desenvolvimento trabalhem em diferentes módulos ao mesmo tempo, o que torna a colaboração mais eficiente.

### Antes da refatoração


``` python
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

```

Aqui pode-se observar que existia um problema n main de não ter classe e subclasse, apenas métodos,apresentando muitas variáveis de instâncias é indício de que ela está com coesão baixa (fazendo mais do que deveria) o que caracteriza um code smell de um método grande.

### Depois da refatoração
``` python
from simulacao import Simulacao
from cadastros import Cadastros
import time
from constants import (
    OPCAO_CADASTRAR_RENDIMENTO,
    OPCAO_CADASTRAR_DEDUCAO,
    OPCAO_CADASTRAR_DEPENDENTE,
    OPCAO_CADASTRAR_PENSAO,
    OPCAO_CALCULAR_IMPOSTO,
    OPCAO_SAIR,
)


class Main (Cadastros,Simulacao,time):

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


```
Aqui foi reduzido o tamanho do método e a criação de uma classe Menu e de outro aquivo cadastros.py com a classe Cadastros, ajudando a aumentar a coesão.Isso permite que o código seja mais organizado, fácil de manter e testar, e permite a equipe de desenvolvimento colaborar de forma mais eficiente em projetos de software. A modularidade também facilita a resolução de problemas, pois os erros podem ser localizados e corrigidos mais facilmente em um único módulo.

``` python
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

```

## Simplicidade
A simplicidade no código refere-se a escrever código de forma clara, concisa e fácil de entender. Isso ajuda a tornar o código mais legível e fácil de manter, além de aumentar a eficiência do desenvolvimento. Algumas alternativas para manter a simplicidade no código incluem:


Nomenclatura clara: use nomes de variáveis e funções que sejam descritivos e fáceis de entender.

Comentários: escreva comentários claros e concisos para explicar o propósito de cada parte do código.

Estrutura clara: organize o código em blocos lógicos, usando indentação e espaços em branco para torná-lo mais fácil de entender.

Evite código redundante: evite escrever código repetitivo e busque formas de reutilizar o código de forma mais eficiente.

Teste e debug: teste o código frequentemente para identificar erros e problemas, e depure o código para corrigi-los.

Em resumo, a simplicidade no código é uma prática importante para escrever código claro, legível e fácil de manter, o que ajuda a tornar o desenvolvimento mais eficiente e a resolução de problemas mais fácil.

### Antes da refatoração
``` python

class Pensao:
    def __init__(self, valor_pensao: int | float) -> None:
        if not valor_pensao:
            raise ValorPensaoEmBrancoException(valor_pensao)
        if type(valor_pensao) not in [float, int] or valor_pensao < 0:
            raise ValorPensaoInvalidaException(valor_pensao)
        self.valor_pensao = valor_pensao


class ValorPensaoInvalidaException(Exception):
    def __init__(self, valor_pensao: Any) -> None:
        self.valor_pensao = valor_pensao
        super().__init__(f"Valor inválido: {self.valor_pensao}")

    def __str__(self) -> str:
        return f"Valor inválido: {self.valor_pensao}"


class ValorPensaoEmBrancoException(Exception):
    def __init__(self, valor_pensao: Any) -> None:
        self.valor_pensao = valor_pensao
        super().__init__(f"Valor em branco: {valor_pensao}")

    def __str__(self) -> str:
        return f"Valor em branco: {self.valor_pensao}"

```
Para ter uma nomenclatura clara foram modificados os nomes das classes que mesclavam ingles e portugues, deixando apenas em portugues em concordancia com o resto do programa.
### Depois da refatoração
``` python

class Pensao:
    def __init__(self, valor_pensao: int | float) -> None:
        if not valor_pensao:
            raise ValorPensaoEmBrancoExcecao(valor_pensao)
        if type(valor_pensao) not in [float, int] or valor_pensao < 0:
            raise ValorPensaoInvalidaExcecao(valor_pensao)
        self.valor_pensao = valor_pensao


class ValorPensaoInvalidaExcecao(Exception):
    def __init__(self, valor_pensao: Any) -> None:
        self.valor_pensao = valor_pensao
        super().__init__(f"Valor inválido: {self.valor_pensao}")

    def __str__(self) -> str:
        return f"Valor inválido: {self.valor_pensao}"


class ValorPensaoEmBrancoExcecao(Exception):
    def __init__(self, valor_pensao: Any) -> None:
        self.valor_pensao = valor_pensao
        super().__init__(f"Valor em branco: {valor_pensao}")

    def __str__(self) -> str:
        return f"Valor em branco: {self.valor_pensao}"


```