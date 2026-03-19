tipo = input("Qual é tipo do seu bilhete: ")
valor = int(input("Quanto você vai dar: "))

unit = 1.3
duplo = 2.6
viagens = 12

if str.lower(tipo) == 'unitário':
    resto = valor
    quant = 0
    while resto >= unit:
        resto -= unit
        quant += 1
    print(f"Qunatidade de bilhetes: {quant}\nTroco: {resto}")