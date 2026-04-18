def par_impar(num):
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")
    return num

numero = int(input("Digite um número: "))
par_impar(numero)