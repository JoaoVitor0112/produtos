produtos = []

while True:
    print("\n(1) Adicionar produto")
    print("(2) Listar produtos")
    print("(3) Remover produto")
    print("(4) Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Digite o nome do produto: ")
        produtos.append(produto)
        print("Produto adicionado com sucesso!")

    elif opcao == "2":
        print("Função ainda não funciona.")

    elif opcao == "3":
        print("Função ainda não funciona.")

    elif opcao == "4":
        print("Função ainda não funciona.")

    else:
        print("Opção inválida!")