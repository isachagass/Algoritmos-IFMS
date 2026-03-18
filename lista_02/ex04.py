numeros = list(map(int, input("Digite 3 números: ").split(',')))

numeros.sort()

print(f"Os menores números são: {numeros[0]}, {numeros[1]}")