numeros = list(map(int, input('Digite 2 números: ').split(',')))

soma = 0
sub = numeros[0] - numeros[1]

for num in numeros:
    soma += num


print(f"Soma: {soma}\nSubtração: {sub}")
