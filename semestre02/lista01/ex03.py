def concatenacao(lista1, lista2):
    nova_lista = []
    if len(lista1) < len(lista2):
        for i in range(len(lista1)):
            nova_lista.append(lista1[i])
            nova_lista.append(lista2[i])
            lista2.pop(i)
            print(lista2)
        for iten in lista2:
            nova_lista.append(iten)
        # nova_lista.append(lista2)

        
    else:
        for i in range(len(lista2)):
            nova_lista.append(lista1[i])
            nova_lista.append(lista2[i])
            lista1.pop(i)
        nova_lista.append(lista1)

    print(nova_lista)

lista1 = [10,10,10,10,10]
lista2 = [3,4,5,6,7,8,9,19,17]
concatenacao(lista1,lista2)