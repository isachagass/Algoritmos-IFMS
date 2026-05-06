alto = int(input("Digite o valor mais alto: "))
baixo = int(input("Digite o valor mais baixo: "))
soma = 0
qnt = 0
for i in range(alto, baixo-1, -3):
    print(i)
    soma += i
    qnt += 1 

media = soma / (qnt)
print("Média: ", media)