idades = list(map(int, input("Digite a quantidade de idades desejados, separadas por uma vírgula: ").split(",")))

soma_maior = 0
soma_menor = 0
menores = 0

for i in idades:
    if i >= 18 :
        soma_maior += i
    else:
        soma_menor += i
        menores += 1
    
print(f"A Soma das pessoas maiores de idade: {soma_maior}\nA Média de idade dos menores de idade é: {soma_menor/menores}")