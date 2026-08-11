#Avaliação1

def addLivro(dicLivros): #declara a função que adiciona livros no estoque, ou incrementa a quantidade existente
        print("=== Adicionar livro ===")
 
        titulo = input("\n Título: ").lower().strip()
        quantidade = int(input("\n Quantidade: "))
 
        if titulo in dicLivros:
            dicLivros[titulo] += quantidade #incremento de um novo livro ou adiciona a quantidade se o livro já existir
        else:
            dicLivros[titulo] = quantidade
 
        print("Livro adicionado!")
 
def removeLivro(dicLivros): #declara a função que remove uma quantidade de acordo com o título informado
        print("=== Remover Livro! ===")
        titulo = input("\n Título: ").lower().strip() #declara a variável e com lower(deixar todo o texto em minúsculo) e strip(remove os espaços das extremidades)
 
        if titulo not in dicLivros:
                print("\n O livro não existe no estoque!")
        else:
            quantidade = int(input("\nQuantidade: "))
            if quantidade > dicLivros[titulo]:
                print("Quantidade insuficiente! ") 
                print (f"Quantidade disponível :  {dicLivros[titulo]}")
            else:
                dicLivros[titulo] -= quantidade # decremento da quantidade de livros
                print (f"Quantidade atualizada: {dicLivros[titulo]}")  
 
def consulta(dicLivros): # Declara a função que busca na lista o título informado pelo usuário
        titulo = input("\n Digite o título do livro: ").lower().strip()
        if titulo in dicLivros:
            print (f"\nLivro: {titulo}")
            print (f"\nQuantidade disponível: {dicLivros[titulo]}")
        else:
            print("O livro não existe no estoque!")
 
def listar(dicLivros): # declara a função que lista todos os livros cadastrados
        print("\n === Livros disponíveis ===")
 
        for titulo, quantidade in dicLivros.items():
            print(f"{titulo} - {quantidade}")
 
def main():
 
    dicLivros = { #cria o estoque de livros usando um dicioário
            "querido john": 12,
            "a ultima musica": 6,
            "a revoluçao dos bichos": 10,
            "o sol é pra todos": 5,
            "quem pensa enriquece": 7,
            "gatilhos mentais": 9
            }
 
    while True:
 
        print(" \n=== SISTEMA DE GESTÃO DE LIVRARIA ===")
        print(" \n Escolha uma opção" )
        print(" 1 - Adicionar Livro")
        print(" 2 - Remover Livro")
        print(" 3 - Consultar Livro")
        print(" 4 - Listar Livros")
        print(" 5 - Sair")
 
        op = input("\n Digite a opção escolhida: ")
 
        match op: 
             case "1":
                  addLivro(dicLivros)
             case "2":
                  removeLivro(dicLivros)
             case "3":
                  consulta(dicLivros)
             case "4":
                  listar(dicLivros)
             case "5":
                  print("\nSaindo...\n\n\n\n")
                  break
             case _:
                  print("\n Opção inválida")
 
main ()