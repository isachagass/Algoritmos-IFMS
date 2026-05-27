numeros = [1,2,3,4,5,6]
pares = 0
impares = 0
num_pares = []
num_impares = []
for i in numeros:
    if i % 2 == 0:
        pares += 1
        num_pares.append(i)
    else:
        impares += 1
        num_impares.append(i)

print(f"Quantidade de numeros pares: {pares}\nNumeros pares: {num_pares}\nQuantidade de numeros impares: {impares}\nNumeros impares{num_impares}")