nomes = []
medias = []

for i in range(5):
    nome = input("Digite o nome: ")
    media = int(input("Digite a media: "))
    nomes.append(nome)
    medias.append(media)

media_geral = sum(medias) / len(medias)
print(f"medias: {medias}\nMedia Geral: {media_geral}")

for i in range(5):
    print(f"{nomes[i]}: {medias[i]}")
    if medias[i] < media_geral:
        print("Aluno abaixo da media geral")