def ordenar(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

num1, num2, num3 = map(int ,input("Digite 3 números (separados por virgulas): ").split(','))
print(ordenar(num1, num2, num3))


