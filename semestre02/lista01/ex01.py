def medias(lista, k):
    soma = 0
    for iten in range(k):
        soma += lista[iten]
    media = soma / k
    return media

lista = [0,1,2,3,4,5]
k= int(input("Digite o limite da janela: "))
resultado = medias(lista, k)
print(resultado)