def conversao(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60
    return print(f"{horas} horas, {minutos} minutos e {segundos} segundos")

segundos = int(input("Digite a  quantidade de segundos: "))
conversao(segundos)