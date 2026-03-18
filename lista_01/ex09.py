numeros = list(map(int, input("Digite 3 numeros: ").split(',')))

soma = 0
for num in numeros:
    soma += num

media = soma/3

print(f"Média = {media}")