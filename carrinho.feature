# language: pt

Funcionalidade: Carrinho de compras

  Cenário: Adicionar produto com sucesso
    Dado que o carrinho está vazio
    E que o produto custa 50 reais por unidade
    E que existem 10 unidades disponíveis em estoque
    Quando o usuário adicionar 2 unidades do produto
    Então o carrinho deve conter 2 itens
    E o valor total deve ser 100 reais

Cenário: Tentar adicionar produto sem estoque suficiente
    Dado que o carrinho está vazio
    E que o produto custa 50 reais por unidade
    E que existem 5 unidades disponíveis em estoque
    Quando o usuário tentar adicionar 8 unidades do produto
    Então o sistema deve informar "Estoque insuficiente"
    E o carrinho deve permanecer vazio
    E o valor total deve continuar em 0 reais
