# ex01
# lista = [9,3,5,11,4,2,12,40]
# lista_crescente = []
# lista_decrescente = []
# lista_menor = []
# lista_maior = []

# for i in lista:
#     lista_maior.append(i)
#     lista_menor.append(i)

# def menor(lista):
#     menor = 0
#     ind_menor = 0
#     contador = 0
#     for i in lista:
#         if contador == 0:
#             menor = i
#         if i < menor:
#             menor = i
#             ind_menor = contador
#         contador+=1
    
#     del lista[ind_menor]

#     lista_crescente.append(menor)

#     return lista

# def maior(lista):
#     maior = 0
#     ind_maior = 0
#     contador = 0
#     for i in lista:
#         if contador == 0:
#             maior = i
#         if i > maior:
#             maior = i
#             ind_maior = contador
#         contador += 1
    
#     del lista[ind_maior]

#     lista_decrescente.append(maior)

#     return lista

# while len(lista_menor) != 0:
#     lista_menor = menor(lista_menor)

# while len(lista_maior) != 0:
#     lista_maior = maior(lista_maior)

    
# print("\n")

# print("Crescente - sem funcao:",lista_crescente)
# print("decrescente - sem funcao:",lista_decrescente)

# print("\n")
# lista.sort()
# print("Crescente - com função: ",lista)
# lista.reverse()
# print("Decescente - com função: ",lista)

# print("\n")

# ex02
# lista = []
# sair = 0
# while sair == 0:
#     num = (input("Digite um número: "))
#     if num == 'sair':
#         sair = 1
#     else:
#         lista.append(int(num))
# soma = 0
# maior = 0
# menor = 0
# tamanho = 0
# for i in lista:
#     if i == lista[0]:
#         menor = i
#     soma += i
#     tamanho +=1
#     if i > maior:
#         maior = i
#     if i < menor:
#         menor = i

# print("\n")
# print(lista)
# print("\n")
# print("maior valor - sem funcao:",maior)
# print("menor valor - sem funcao: ",menor)
# print("soma - sem funcao:",soma)
# print("tamanho da lista - sem funcao:", tamanho)

# print("\n")
# print("maior valor - com funcao:",max(lista))
# print("menor valor - com funcao: ",min(lista))
# print("soma - com funcao:",sum(lista))
# print("tamanho da lista - com funcao:",len(lista))


# print("\n")

# ex03
# def remover(lista, nome):

#     contador = 0
#     for i in lista:
#         if i == nome:
#             del lista[contador]
#         contador += 1
#     return lista

# lista = []
# for i in range(3):
#     nome = input("Digite um nome: ")
#     lista.append(nome)
# remover_nome = input("Digite o nome que será removido: ")

# lista_nova = remover(lista, remover_nome)

# print("Nomes restantes: ",lista_nova)