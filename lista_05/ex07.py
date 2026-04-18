def calculo(numeros):
    numeros.sort()
    soma = 0
    for i in numeros:
        soma += i
    media = soma / len(numeros)
    return print(f"Média = {media}\nMaior = {numeros[-1]}\nMenor = {numeros[0]}")
num = -1
numeros = []
while num != 0:
    num = int(input("Digite um número, ou 0 para sair: "))
    if num != 0:
        numeros.append(num)

calculo(numeros)