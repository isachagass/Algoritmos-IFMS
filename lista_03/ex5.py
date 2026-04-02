numeros = list(map(int, input("Digite a quantidade de números que desejar, separados por uma virgula: ").split(",")))
soma = 0
for i in numeros:
    soma += i
print(f"Soma de {numeros} = {soma}")