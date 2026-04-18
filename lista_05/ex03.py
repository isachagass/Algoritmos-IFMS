def verifica(numero):
    if numero > 0:
        print(f"O número {numero} é positivo.")
    else:
        print(f"O número {numero} é negativo.")

    return numero

numero = int(input("Digite um número: "))
verifica(numero)