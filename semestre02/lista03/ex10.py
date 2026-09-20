import numpy as np

notas = np.array([[5.0, 7.5, 6.0], [8.0, 9.0, 4.0], [3.5, 5.0, 6.5], [7.0, 6.0, 8.5]])
medias_notas = np.sum(notas, axis=1) / 3
medias_provas = np.sum(notas, axis=0) / 3
maior_med = np.argmax(medias_provas)

notas[notas<6] = 6.0
nova_notas = np.delete(notas,2, axis=1)

print("Medias de notas:", medias_notas)
print("Medias de avaliações:", medias_provas)
print("Maior Media Geral:", maior_med)
print("Reajuste:\n",notas)
print("Retirada da Avaliaçao 3:\n",nova_notas)