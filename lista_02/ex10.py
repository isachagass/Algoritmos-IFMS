sexo = input("qual é o seu sexo: ")
idade = int(input("Digite sua idade: "))
if str.lower(sexo) == "masculino":
    if idade >= 18:
        print("Você precisa se alistar")
    else:
        print("Você não precisa se alistar")
else:
    print("Você não precisa se alistar")

