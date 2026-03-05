from produto import Produto
from carrinho import Carrinho

carrinho = Carrinho()

while True:
    print("\n=== CARRINHO DE COMPRAS ===")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Aplicar desconto")
    print("4 - Ver total")
    print("5 - Gerar nota fiscal")
    print("6 - Listar produtos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        produto = Produto(nome, preco)
        carrinho.adicionar_produto(produto)

    elif opcao == "2":
        nome = input("Nome do produto para remover: ")
        carrinho.remover_produto(nome)

    elif opcao == "3":
        desconto = float(input("Percentual de desconto: "))
        carrinho.aplicar_desconto(desconto)

    elif opcao == "4":
        total = carrinho.calcular_total()
        print(f"Total do carrinho: R$ {total:.2f}")

    elif opcao == "5":
        carrinho.gerar_nota_fiscal()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")
