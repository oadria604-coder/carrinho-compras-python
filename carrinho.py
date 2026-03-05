class Carrinho:
    def _init_(self):
        self.produtos = []
        self.desconto = 0

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"{produto.nome} foi adicionado ao carrinho.")

    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                print(f"{nome} removido do carrinho.")
                return
        print("Produto não encontrado.")

    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        total = total - (total * self.desconto / 100)
        return total

    def aplicar_desconto(self, percentual):
        self.desconto = percentual
        print(f"Desconto de {percentual}% aplicado.")

    def gerar_nota_fiscal(self):
        print("\n===== NOTA FISCAL =====")

        for produto in self.produtos:
            print(f"{produto.nome} - R$ {produto.preco:.2f}")

        subtotal = sum(produto.preco for produto in self.produtos)
        desconto = subtotal * self.desconto / 100
        total = subtotal - desconto

        print("----------------------")
        print(f"Subtotal: R$ {subtotal:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Total: R$ {total:.2f}")
        print("======================")

