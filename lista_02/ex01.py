numeros = list(map(int, input("Digite 2 números: ").split(',')))

menor = numeros[0]
for num in numeros:
    if num < menor:
        menor = num

print(f"O Menor número é: {menor}")