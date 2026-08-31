def main():
    def streaming(lista, genero, nota_corte):
        filtro = []
        mais_antigo= []
        ano = 2027
        for filme in lista:
            if filme[2] == genero and filme[3] >= nota_corte:
                filtro.append(filme[0])
                if filme[1] < ano:
                    mais_antigo = ((filme[0], filme[1]))
                    ano = filme[1]
        filme_mais_antigo = tuple(mais_antigo)

        return filtro, filme_mais_antigo


    filmes = (
        ("Inception", 2010, "Ficção", 8.8),
        ("O Poderoso Chefão", 1972, "Drama", 9.2),
        ("Parasita", 2019, "Thriller", 8.5),
        ("Interstellar", 2014, "Ficção", 8.7),
        ("Matrix", 1999, "Ação", 8.7)
    )
    filtro, filme_mais_antigo = streaming(filmes, "Ficção", 8)
    print("Filmes filtrados:", filtro)
    print("Filme mais antigo:", filme_mais_antigo)
main()