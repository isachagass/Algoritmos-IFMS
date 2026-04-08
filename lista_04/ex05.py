numero = int(input("Digite um número: "))
divisores = []

def perfeito(numero):
    for i in range(1,numero):
        if numero % i == 0:
            divisores.append(i)
        
    soma = 0
    for i in divisores:
        soma += i

    if soma == numero:
        print("O número é perfeito")
    else:
        print("O número não é perfeito")

perfeito(numero)