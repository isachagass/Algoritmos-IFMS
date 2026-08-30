def descodificar(lista):
    id_pacotes = []
    for i in range(len(lista)):
        if lista[i] == 1:
            if i+2 < len(lista) and lista[i+1] == 0  and lista[i+2] == 0:
                id_pacotes.append(i)

    return len(id_pacotes), id_pacotes

dados = [0,1,0,0,1,0,1,0,0,1,0]
pacotes_validos, id_pacotes = descodificar(dados)
print("Quantidade de pacotes válidos:", pacotes_validos)
print("Ids dos pacotes:", id_pacotes)