import numpy as np

matriz = np.random.randint(10,99, size=(4,4))

soma_linha = np.sum(matriz, axis=1)
soma_coluna = np.sum(matriz, axis=0)
media_coluna = soma_coluna / 4

matriz_nova = matriz.reshape(2,8)

print("Matriz 4x4:\n",matriz)
print("Soma de cada linha:", soma_linha)
print("Media de cada coluna: ",media_coluna)
print("Matriz 2x8:\n",matriz_nova)