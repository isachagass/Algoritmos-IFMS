tipo = input("Qual é tipo do seu bilhete: ")
valor = int(input("Quanto você vai dar: "))

unit = 1.3
duplo = 2.6
viagens = 12

if str.lower(tipo) == 'unitário':
    resto = valor
    quant = 0
    while resto >= unit:
        resto -= unit
        quant += 1
    print(f"Qunatidade de bilhetes: {quant}\nTroco: {resto}")

//ex17.py

numeros = list(map(int, input("Digite 3 valores: ").split(',')))


if numeros[0] < numeros[1] + numeros[2]:
    print("Triângulo válido")
    if numeros[0] ==  numeros[1] == numeros[2]:
        print("Triângulo esquilatero")
    elif numeros[0] == numeros[1] or numeros[1] == numeros[2] or numeros[0] == numeros[2]:
        print("Triângulo isósceles")
    else:
        print("Triangulo escaleno")

else:
    print("Não é um triangulo")
