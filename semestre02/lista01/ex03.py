def concatenacao(lista1, lista2):
    resultado = []

    for i in range(max(len(lista1), len(lista2))):
        if i < len(lista1):
            resultado.append(lista1[i])
        if i < len(lista2):
            resultado.append(lista2[i])

    return resultado


lista1 = [1,3,5,7,9,11,13]
lista2 = [2,4,6,8,10,12,14,15,16,17,18]

print(concatenacao(lista1, lista2))