produtos = ["Pao", "Farinha"]
quantidades = [0, 3]
menu = 0

while menu != 5:
    menu = int(input("\n\nEscolha uma opção:\n1.Cadastrar Produto \n2.Listar Estoque \n3.Atualizar Quantidade \n4.Excluir Produto \n5.Sair\n\n"))

    match menu:
        case 1:
            produto = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade de produto: "))
            produtos.append(produto)
            quantidades.append(quantidade)
        case 2:
            print("\nLista de estoque:")
            for i in range(len(produtos)):
                print(f"{produtos[i]} : {quantidades[i]}")
        case 3:
            produto = input("Digite o nome do produto para alterar o estoque: ")
            if produto in produtos:
                id = produtos.index(produto)
                nova_qtd = int(input("Digite a nova quantidade: "))
                quantidades[id] = nova_qtd
            else:
                print("Produto não encontrado")
        case 4:
            produto = input("Digite o nome do produto para excluir: ")
            if produto in produtos:
                id = produtos.index(produto)
                produtos.pop(id)
                quantidades.pop(id)
                print("Produto excluido com sucesso")
            else:
                print("Produto não encontrado")
        case 5:
            print("Sessão encerrada!")
            break
        case _:
            print("Digite uma opção válida!")

