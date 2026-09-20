salarios = [2500.0, 3200.0, 1800.0, 4500.0,2100.0]

salarios[2] = 2300.0
print("\nSalario id 2 alterado: ",salarios,"\n")

pesquisa = float(input("Digite um salario para verificação: "))

for i in salarios:
    if i == pesquisa:
        print("\nEste numero está na lista!")
        salarios.remove(i)
        print("Salario removido: ", salarios)

print("\nUltimo salarios:",salarios.pop())
print("\nSalarios finais: ", salarios)