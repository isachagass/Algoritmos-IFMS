def montar_lista(n):
    lista = []
    for i in range(n):
        num = int(input("Digite um número: "))
        lista.append(num)

    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)

    qtd_par = 0
    for i in lista:
        if i % 2 == 0:
            qtd_par += 1

    print(f"\nMaior: {maior} \nMenor:{menor} \nMedia: {media}\nQuantidade Pares: {qtd_par}")

quantidade = int(input("Quantidade de numeros para cadastrar: "))
montar_lista(quantidade)