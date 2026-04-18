def media(numeros):
    if len(numeros) == 0:
        return 0, 0
    soma = 0
    for i in numeros:
        soma += i
    media = soma / len(numeros)
    return soma, media

positivos, negativos = [], []
for i in range(100):
    num = int(input("Digite um número: "))
    if num > 0:
        positivos.append(num)
    else:
        negativos.append(num)

somap, mediap = media(positivos)
soman, median = media(negativos)
diferença = abs(len(positivos) - len(negativos))

print(f"\nSoma de positivos: {somap}\nMédia de positivos: {mediap}\nSoma de negativos: {soman}\nMédia de negativos: {median}\nDiferença de quantidade: {diferença}")
