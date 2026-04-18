def media(salarios):
    if len(salarios) == 0:
        return 0

    soma = 0
    for i in salarios:
        soma += i
    media = soma / len(salarios)

    return media

# maior entre os dois


sem_filhos, filhos2, salarios_geral = [], [], []
nome = 1
while nome != "0":

    nome = input("Digite seu nome, ou 0 para calcular: ")

    if nome == '0':
        break

    salario = float(input("Digite seu salário: "))
    filhos = int(input("Digite o número de filhos que você possui: "))

    salarios_geral.append(salario)

    if filhos == 2:
        filhos2.append(salario)
    elif filhos == 0:
        sem_filhos.append(salario)

media_0 = media(sem_filhos)
media_2 = media(filhos2)
media_geral = media(salarios_geral)

print(f"\n\nSalário médio das pessoas que possuem 2 filhos: R${media_2:.2f}\nSalário médio das pessoas que não possuem filhos: R${media_0:.2f}\nMédia de salário geral: R${media_geral:.2f}")

if media_0 > media_2:
    print("\nA média salárial de pessoas que não possuem filhos é maior do que a média salarial das pessoas que possuem 2 filhos")
else:
    print("\nA média salárial de pessoas que possuem 2 filhos é maior do que a média salarial das pessoas que não possuem filhos")