def main():
    def nova_imagem(foto):
        img_final = []
        pixel_preto = 0
        for pixel in foto:
            soma = 0
            for i in pixel:
                soma += i
            media = soma // 3
            img_final.append(media)
            if media == 0:
                pixel_preto += 1

        return img_final, pixel_preto


    foto = [
        (0, 0, 0),       
        (255, 0, 0),     
        (0, 255, 0),     
        (0, 0, 255),     
        (255, 255, 255), 
        (0, 0, 0),       
        (128, 128, 128), 
        (255, 165, 0)    
    ]
    img_final, pixel_preto = nova_imagem(foto)
    print("Nova Imagem Processada:", img_final)
    print("Quantidade de Pixels pretos:", pixel_preto)

main()