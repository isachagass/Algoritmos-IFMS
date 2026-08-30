def escala(lista):

    dias_unicos = []
    for dias_medico in lista:
        for dia in dias_medico:
            if dia not in dias_unicos:
                dias_unicos.append(dia)

    dia_qtdMed = []
    for dia in dias_unicos:
        qtd_medicos = 0
        for dias_um_med in lista:
            if dia in dias_um_med:
                qtd_medicos += 1

        dia_qtdMed.append([dia,qtd_medicos])

    menor_dia = 0
    menor_qtd_medicos = 999
    for item in dia_qtdMed:
        if menor_qtd_medicos > item[1]:
            menor_qtd_medicos = item[1]
            menor_dia = item[0]

    ids_medicos = []
    for medico in lista:
        for dia in medico:
            if dia == menor_dia:
                ids_medicos.append(lista.index(medico))
    

    return menor_dia, ids_medicos
        

lista = [
    [1, 2, 3, 4],  # Médico ID 0
    [2, 3, 4, 5],  # Médico ID 1
    [1, 2, 4, 6],  # Médico ID 2
    [3, 4,6]         # Médico ID 3
]

menor_dia, ids_medicos = escala(lista)
print("Dia com menos medicos: ", menor_dia)
print("Medicos disponíveis no dia:", ids_medicos)