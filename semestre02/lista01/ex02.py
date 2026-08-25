def deslocar(lista, n):
    # nova_lista = []
    for i in range(n):
        lista.insert(i, lista[-1])
        lista.pop()
    return lista

lista = [1,2,3,4,5]
n = int(input("Digite o nuemro de casas que serão deslocadas: "))
lista_deslocada = deslocar(lista, n)
print(lista_deslocada)