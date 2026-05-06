senha = 2024
tentativas = 0

while tentativas < 5:
    codigo = int(input("Digite a senha: "))

    if codigo < senha:
        print(f"A senha digitada é menor que a senha real")
    elif codigo > senha:
        print("A senha digitada é maior que a senha real")
    else:
        print("Cofre Aberto!")
        break
    
    tentativas +=1

if tentativas >= 5:
    print("Acesso Bloqueado!")