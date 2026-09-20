import numpy as np

matriz = [
    [1, 2], 
    [3, 4],
    [5, 6]
]

matriz[1][0] = 99

def matriz_transposta(matriz):
    # nova_matriz = []
    # linha1 = []
    # linha2 = []
    # for i in matriz:
    #     linha1.append(i[0])
    #     linha2.append(i[1])

    # nova_matriz.append(linha1)
    # nova_matriz.append(linha2)
    # nova_matriz = np.array(nova_matriz)

    nova_matriz = np.transpose(matriz)
    return nova_matriz

print("Matriz transposta: \n",matriz_transposta(matriz))