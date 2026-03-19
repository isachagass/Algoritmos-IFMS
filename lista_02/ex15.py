numeros = list(map(int, input("Digite suas 3 notas: ").split(',')))
soma = 0
for num in numeros:
    soma += num
media = soma/3
if media >= 0 and media < 3:
    print(f"Sua nota foi {media}, você está REPROVADO!")
elif media >= 3 and media <7:
    print(f"Sua nota foi {media}, EXAME!")
elif media >= 7 and media <= 10:
    print(f"Sua nota foi {media}, você está APROVADO!")

    