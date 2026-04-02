numeros = list(map(int, input("Digite a sequencia de números separados po ruma virgula: ").split(',')))

soma_par = 0
soma_impar = 0
qtd_par = 0
qtd_impar = 0

for i in numeros:
    if i % 2 == 0:
        soma_par += i
        qtd_par += 1
    else:
        soma_impar += i
        qtd_impar += 1

print(f"Soma de nuemros pares = {soma_par}\nQuantidade de numeros pares = {qtd_par}\n\nSoma de numeros impares = {soma_impar}\nQuantidade de numeros impares = {qtd_impar}")