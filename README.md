# Trabalho Prático 1 - Test-Driven Development

**Número do Trabalho**: 1

**Conteúdo da Disciplina**: Desenvolvimento Orientado a Testes

## Alunos

| Matrícula  |        Aluno           |
| ---------- | ---------------------- |
| 18/0074741 | Caio Martins           |
| 18/0103580 | Jonathan Jorge         |
| 18/0103792 | Júlia Farias           |
| 18/0105345 | Lucas Lima             |
| 19/0048760 | Wellington Jhonathan   |

## Sobre

Criação de um simulador similar ao simulador disponibilizado pela RFB. Esse simulador deverá ser construído através do método de TDD utilizando, obrigatoriamente, as técnicas de falsificação, duplicação e triangulação de testes.

## Instalação

**Linguagem**: Python 3.11.0 ou superior

Para instalar as dependências do projeto, execute o comando abaixo:

```bash
pip install -r requirements.txt
```

para executar o projeto, execute o comando abaixo:

```bash
python src/main.py
```

Para executar os testes e verificar a cobertura de código, execute o comando abaixo:

```bash
pytest --cov=src test/
```
