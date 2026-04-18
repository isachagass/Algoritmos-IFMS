def temperatura(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def medida(metros):
    centimetros = metros * 100
    return centimetros

menu = 0
while menu != 3:
    menu = int(input("Escolha uma alternativa:\n1- Converter Celsius para Fahrenheit\n2- Converter Metros para Centímetros\n3- Sair\n"))

    match menu:
        case 1:
            celsius = int(input("Digite a temperatura para a conversão: "))
            print(f"\n{celsius} °C = {temperatura(celsius):.2f} °F\n")          
        case 2:
            metros = float(input("Digite a medida para a conversão: "))
            print(f"\n{metros} metros = {medida(metros)} centímetros\n")
        case 3:
            break
        case _:
            print("Digite uma opção válida")
            continue

