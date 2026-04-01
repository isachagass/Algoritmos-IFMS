numeros = list(map(int, input("Digite 10 valores separados por virgulas: ").split(",")))
for i in numeros:
    if i > 25 and i < 85:
        print(i)