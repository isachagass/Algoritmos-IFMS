def main():

    def microcontrolador(tuplas): 
        ids_alerta = []
        maior_temperatura = 0
        menor_umidade = 999
        for sensor in tuplas:
            if sensor[1] > 35 or sensor[2] < 20:
                ids_alerta.append(sensor[0])
            if sensor[1] > maior_temperatura:
                maior_temperatura = sensor[1]
            if sensor[2] < menor_umidade:
                menor_umidade = sensor[2]

        max_min = (maior_temperatura, menor_umidade)
        return ids_alerta, max_min
    tuplas = [
        [0,29,25],
        [1,38,29],
        [2,28,19],
        [3,30,20],
    ]
    ids_alerta, max_min = microcontrolador(tuplas)
    print("IDs de alerta:", ids_alerta)
    print("Temperatura Máxima:", max_min[0])
    print("Umidade Mínima:", max_min[1])
main()