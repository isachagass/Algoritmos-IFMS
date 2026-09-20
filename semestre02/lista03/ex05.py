import numpy as np
notas = np.array([5.5, 8.0, 4.5, 9.0, 6.5])

notas_a = np.insert(notas, 2, 7.0)
print("Inserindo no id 2:", notas_a)

notas[notas < 6] = 6.0
print("Substituindo valores: ",notas)

notas_c = np.delete(notas, 4)
print("Item 4 removido:", notas_c)