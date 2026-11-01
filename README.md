[![AST11 - Testes Automatizados](https://github.com/marialuiza-mdealcantara/AST11-BDD/actions/workflows/tests.yml/badge.svg)](https://github.com/marialuiza-mdealcantara/AST11-BDD/actions/workflows/tests.yml)

# AST11 — Implementação de BDD em um Carrinho de Compras

## Sobre o projeto

Este projeto foi desenvolvido como parte da atividade prática AST11, com o objetivo de aplicar os conceitos de **Behavior-Driven Development (BDD)** na implementação e automação de testes de um sistema básico de carrinho de compras.

A proposta consiste em transformar requisitos de negócio em cenários testáveis utilizando Gherkin, implementar as regras de negócio em Python e automatizar a validação dos comportamentos com pytest-bdd.

## Objetivos

- Descrever requisitos de negócio utilizando Gherkin.
- Implementar regras de negócio em Python.
- Validar a disponibilidade de produtos em estoque.
- Calcular automaticamente o valor total do carrinho.
- Tratar exceções em situações de estoque insuficiente.
- Automatizar cenários de comportamento utilizando BDD.
- Implementar integração contínua para execução automática dos testes.

## Tecnologias utilizadas

- **Python:** implementação das regras de negócio.
- **Gherkin:** especificação dos comportamentos esperados.
- **pytest:** execução dos testes automatizados.
- **pytest-bdd:** integração entre cenários Gherkin e testes Python.
- **Git e GitHub:** versionamento e hospedagem do projeto.
- **GitHub Actions:** integração contínua e execução automatizada dos testes.

## Estrutura do projeto

```text
AST11-BDD/
├── .github/
│   └── workflows/
│       └── tests.yml
├── carrinho.feature
├── carrinho.py
├── test_carrinho.py
├── README.md
└── .gitignore
```

## Regras de negócio implementadas

1. O carrinho deve iniciar vazio, com total igual a zero.
2. O sistema deve permitir adicionar produtos quando houver estoque suficiente.
3. A quantidade de itens e o valor total devem ser atualizados após cada adição.
4. O sistema deve impedir a inclusão de quantidades superiores ao estoque disponível.
5. Em caso de estoque insuficiente, deve ser gerada a exceção `ValueError`, com a mensagem "Estoque insuficiente".

## Cenários automatizados

**Cenário 1 — Adicionar produto com sucesso**

- Estoque disponível: 10 unidades.
- Quantidade solicitada: 2 unidades.
- Preço unitário: R$ 50,00.
- Resultado esperado: 2 itens e total de R$ 100,00.

**Cenário 2 — Estoque insuficiente**

- Estoque disponível: 5 unidades.
- Quantidade solicitada: 8 unidades.
- Resultado esperado: exceção tratada, mensagem de estoque insuficiente e carrinho sem alterações.

## Integração contínua (CI)

O projeto utiliza **GitHub Actions** para automatizar a execução dos testes por meio de um workflow configurado em `.github/workflows/tests.yml`.

A automação é executada nos seguintes eventos:

- Envio de alterações ao repositório (`push`).
- Abertura ou atualização de Pull Requests (`pull_request`).
- Execução manual pelo GitHub (`workflow_dispatch`).

Durante a execução, o GitHub Actions prepara o ambiente Python, instala as dependências necessárias e executa os testes automatizados com pytest.

### Como consultar os resultados dos testes no GitHub

Os testes podem ser acompanhados diretamente pelo repositório, sem necessidade de executar o projeto localmente.

Para consultar:

1. Acesse o repositório no GitHub.
2. Clique na aba **Actions**.
3. Selecione o workflow **AST11 - Testes Automatizados**.
4. Escolha uma execução para visualizar os detalhes.
5. Consulte o resultado de cada etapa, incluindo a execução dos cenários BDD.

As execuções apresentam o status dos testes, permitindo verificar se foram aprovados ou se ocorreram falhas.

## Como executar o projeto localmente

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd AST11-BDD
```

### 2. Criar e ativar o ambiente virtual

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
python -m pip install pytest pytest-bdd
```

### 4. Executar os testes

```bash
pytest test_carrinho.py -v
```

## Resultados

Os dois cenários comportamentais foram executados com sucesso no ambiente local, validando tanto a inclusão de produtos quanto o tratamento de estoque insuficiente.

Os resultados das execuções automatizadas também podem ser consultados na aba **Actions** do repositório no GitHub.

## Aprendizados

A atividade permitiu praticar a integração entre especificação de requisitos, desenvolvimento orientado a comportamento e automação de testes, demonstrando como o BDD aproxima as regras de negócio da implementação técnica.

Além disso, possibilitou aplicar conceitos de versionamento de código e integração contínua utilizando GitHub Actions.
