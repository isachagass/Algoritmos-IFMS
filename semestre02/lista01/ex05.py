def controle_qualidade(pesos, min_peso, max_peso):
    aprovados = []
    descartados = []

    for i in pesos:
        if i >= min_peso and i <= max_peso:
            aprovados.append(i)
        else:
            descartados.append(i)

    porcentagem = len(descartados) * 100 / len(pesos)
    return aprovados, descartados, porcentagem

pesos = [10,15,20,25,5,2,32]
min_peso = 10
max_peso = 30

aprovados, descartados, porcentagem = controle_qualidade(pesos, min_peso, max_peso)

print("Aprovadas:", aprovados)
print("Descartados:", descartados)
print(f"Percentual de Descarte: {porcentagem:.2f}%")