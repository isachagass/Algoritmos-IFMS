import numpy as np

matriz_listas = []

for i in range(3):
    sub_lista = []
    for i in range(3):
        num = int(input("Digite um número: "))
        sub_lista.append(num)
    matriz_listas.append(sub_lista)

matriz = np.array(matriz_listas)
print("\n\nMatriz Tabulada:\n",matriz)

linha, coluna = np.indices(matriz.shape)

diagonal_princ = matriz[linha == coluna]
diagonal_secundaria = matriz[linha + coluna == 2]

print("Diagonal principal: ", diagonal_princ)
print("Diagonal secundaria: ", diagonal_secundaria)