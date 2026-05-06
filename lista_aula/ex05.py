num = int(input("Digite o valor de N: "))
numeros = []
for i in range(1,num+1):
    for j in range(i, i+1):
        numeros.append(j)
    print(numeros)