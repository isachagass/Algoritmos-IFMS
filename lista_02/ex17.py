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