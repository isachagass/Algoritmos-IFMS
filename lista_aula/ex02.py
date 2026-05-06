total = 0
nao_preferem = 0
for i in range(6):
    nome = input("Digite seu nome: ")
    qnt = int(input("Digite a quantidade de livros lidos: "))
    genero = int(input("Digite seu genero preferido:\n1- Ficção\n2-Não-Ficção\n "))

    total += qnt

    if genero == 2:
        nao_preferem += 1

    
preferem = (6- nao_preferem) * 100 / 6
print(f"Total de livros: {total}\nPorcentagem de quem prefere ficção: {preferem}%\nQauntdade de pessoas que não preferem ficção: {nao_preferem}")
