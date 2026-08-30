def verificacao(trajetos, limite):
    km_total = sum(trajetos)

    if km_total >= limite:
        passou_limite = True
        dia = 0
        soma = 0
        for i in trajetos:
            soma += i
            if soma >= limite:
                break
            dia += 1
    else:
        passou_limite = False
        dia = None
    return km_total, dia, passou_limite

trajeto = [15,16,17,13,10,16,18]
km_total, dia, passou_limite = verificacao(trajeto, 80)
print("Quilometragem total:", km_total)
print("Precisa ser recolhido:", passou_limite)
print("Dia em que o limite foi ultrapassado:", dia)