numeros = list(map(int, input("Digite 5 números: ").split(',')))
maior_100 = 0
menores_17 = 0
entre_17_100 = 0

for num in numeros:
    if num < 17:
        menores_17 += 1
    elif num > 100:
        maior_100 += 1
    elif num > 17 and num < 100:
        entre_17_100 += 1

print(f"Menores que 17: {menores_17}\nMaiores que 100: {maior_100}\nMaior que 17 e menor que 100: {entre_17_100}")