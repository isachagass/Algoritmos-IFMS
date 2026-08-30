def urna(votos):
    contagem = []
    for i in set(votos):
        quatidade = votos.count(i)
        contagem.append([i, quatidade])

    id_vencedor = None
    max_votos = 0
    for item in contagem:
        candidato = item[0]
        total_votos = item[1]
        if candidato == 0:
            qtd_branco = total_votos
            procentagem_branco = qtd_branco * 100 / len(votos)

        if candidato != 0 and total_votos > max_votos:
            max_votos = total_votos
            id_vencedor = candidato
            
    return contagem, id_vencedor, max_votos, procentagem_branco


votos = [1,2,3,1,3,0,2,1]
contagem, id_vencedor, max_votos, procentagem_branco = urna(votos)

print("Resumo dos votos:", contagem)
print("Vencedor:", id_vencedor, "com", max_votos, "votos")
print("Percentual de votos em branco:", procentagem_branco, "%")