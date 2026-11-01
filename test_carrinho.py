from pytest_bdd import scenarios, given, when, then, parsers

from carrinho import criar_carrinho, adicionar_produto

scenarios("carrinho.feature")

@given("que o carrinho está vazio", target_fixture="carrinho")
def carrinho_vazio():
    return criar_carrinho()

@given(
    parsers.parse("que o produto custa {preco:d} reais por unidade"),
    target_fixture="preco"
)
def produto_com_preco(preco):
    return preco

@given(
    parsers.parse("que existem {estoque:d} unidades disponíveis em estoque"),
    target_fixture="estoque"
)
def estoque_disponivel(estoque):
    return estoque



@when(parsers.parse("o usuário adicionar {quantidade:d} unidades do produto"))
def adicionar_produto_ao_carrinho(carrinho, quantidade, estoque, preco):
    adicionar_produto(carrinho, quantidade, estoque, preco)

@when(parsers.parse("o usuário tentar adicionar {quantidade:d} unidades do produto"))
def tentar_adicionar_produto(carrinho, quantidade, estoque, preco):
    try:
        adicionar_produto(carrinho, quantidade, estoque, preco)
    except ValueError as erro:
        carrinho["erro"] = str(erro)



@then(parsers.parse("o carrinho deve conter {quantidade:d} itens"))
def verificar_quantidade(carrinho, quantidade):
    assert carrinho["itens"] == quantidade

@then(parsers.parse("o valor total deve ser {total:d} reais"))
def verificar_total(carrinho, total):
    assert carrinho["total"] == total

@then(parsers.parse('o sistema deve informar "{mensagem}"'))
def verificar_erro(carrinho, mensagem):
    assert carrinho["erro"] == mensagem

@then("o carrinho deve permanecer vazio")
def verificar_carrinho_vazio(carrinho):
    assert carrinho["itens"] == 0

@then(parsers.parse("o valor total deve continuar em {total:d} reais"))
def verificar_total_sem_alteracao(carrinho, total):
    assert carrinho["total"] == total

    