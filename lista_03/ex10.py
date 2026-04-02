numeros = []
for i in range(1, 20001):
    divisao = 0
    for j in range(2, i+1):
        if i % j == 0:
            divisao += 1
    if divisao == 1:
        numeros.append(i)
print(f"Numeros primos = {numeros}")