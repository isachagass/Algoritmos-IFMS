limite = int(input("Digite o número limeite de números primos que serão somados: "))
soma = 0
for i in range(1, limite+1):
    divisao = 0
    for j in range(2, i+1):
        if i % j == 0:
            divisao += 1
    if divisao == 1:
        soma += i
    else:
        continue
print(f"Soma = {soma}")