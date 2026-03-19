numeros = list(map(int, input("Digite 5 números: ").split(',')))
exibir = []

for num in numeros:
    if num > 10 and num < 17:
        exibir.append(num)
exibir.sort()
print(f"Números maiores que 10 e menores que 17: {exibir}")
    