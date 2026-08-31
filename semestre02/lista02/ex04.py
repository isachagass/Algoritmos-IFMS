def main():
    def colisao(obstaculos, jogador):
        colidiu = False
        num_colisoes = 0
        for obstaculo in obstaculos:
            diferenca_x = abs(jogador[0] - obstaculo[0])
            diferenca_y = abs(jogador[1] - obstaculo[1])

            distancia = diferenca_x + diferenca_y
            soma_raios = jogador[2] + obstaculo[2]

            if distancia < soma_raios:
                colidiu = True
                num_colisoes += 1

        return colidiu, num_colisoes
    
    
    obstaculos = (
        (390, 300, 15),  
        (410, 310, 15),  
        (100, 250, 15),  
        (750, 320, 30)   
    )

    jogador = (
        (400, 300, 20)
    )

    colidiu, num_obstaculos = colisao(obstaculos, jogador)
    print(f"{'Impacto Detectado!' if colidiu else 'Caminho Livre!'}")
    print("Número de colisões:", num_obstaculos)

main()