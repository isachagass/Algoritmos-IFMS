numeros = list(map(int, input('Digite 2 números: ').split(',')))

soma = 0


for num in numeros:
    soma += num


print(f"Soma: {soma}")
