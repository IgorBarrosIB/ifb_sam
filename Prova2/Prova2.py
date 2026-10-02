#Avaliação2
# Igor Barros de Sousa
class Produtos: #Classe chamado Produto
    def __init__(self, nome, descricao, preco, quantidade) -> None:
        self.__nome = nome  # atributo privado
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade = quantidade

    # ---------- Getters ----------
    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    # ---------- Setters com validação ----------
    @nome.setter
    def nome(self, novo_valor):
        if not novo_valor:
            print("Valor inválido")
        else:
            self.__nome = novo_valor

    @descricao.setter
    def descricao(self, novo_valor):
        if not novo_valor:
            print("Valor inválido")
        else:
            self.__descricao = novo_valor

    @preco.setter
    def preco(self, novo_valor):
        if novo_valor > 0:
            self.__preco = float(novo_valor)
        else:
            print("Valor inválido")

    @quantidade.setter
    def quantidade(self, novo_valor):
        if novo_valor > 0:
            self.__quantidade = int(novo_valor)
        else:
            print("Valor inválido")


class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.carrinho = []
    # Funções para adicionar, buscar, remover produtos, calcular total e listar produtos no carrinho
    def adicionar_produto(self, produto):
        self.carrinho.append(produto)
        print(f"{produto.nome} adicionado ao carrinho.")

    def buscar_por_nome(self, nome):
        for produto in self.carrinho:
            if produto.nome.lower() == nome.lower():
                return produto
        return None

    def remover_produto(self, nome):
        produto = self.buscar_por_nome(nome)
        if produto:
            self.carrinho.remove(produto)
            print(f"{produto.nome} removido do carrinho.")
        else:
            print(f"{nome} não está no carrinho.")

    def calcular_total(self):
        return sum(p.preco * p.quantidade for p in self.carrinho)

    def listar_produto(self):
        if not self.carrinho:
            print("Carrinho vazio.")
        else:
            for i, produto in enumerate(self.carrinho, start=1):
                subtotal = produto.preco * produto.quantidade
                print(f"{i}. {produto.nome} - {produto.descricao} - {produto.quantidade} x R${produto.preco:.2f} = R${subtotal:.2f}")
            print(f"Total: R${self.calcular_total():.2f}")


# ---------- Menu ----------
carrinho = CarrinhoDeCompras()

while True:
    print("\n1: Adicione um produto")
    print("2: Remova um produto")
    print("3: Visualize o conteúdo do carrinho")
    print("4: Calcular valor total")
    print("5: Sair")
    # Tratamento de exceções
    try:
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            nome = input("Nome do produto: ")
            descricao = input("Descrição: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            if not nome or preco <= 0 or quantidade <= 0:
                print("Dados inválidos.")
            else:
                carrinho.adicionar_produto(Produtos(nome, descricao, preco, quantidade))
        elif opcao == 2:
            nome = input("Nome do produto a remover: ")
            carrinho.remover_produto(nome)
        elif opcao == 3:
            carrinho.listar_produto()
        elif opcao == 4:
            print(f"Valor total da compra: R${carrinho.calcular_total():.2f}")
        elif opcao == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha entre 1 e 5.")
    # Tratamento de exceções
    except ValueError:
        print("Entrada inválida. Digite um número.")