import numpy as np

lista_a = np.arange(10,51,5)
print("Numeros:",lista_a)

lista_b = lista_a ** 2
print("Elevados ao quadrado:",lista_b)

lista_c = lista_b[lista_b > 500]
print("Maiores que 500:",lista_c)