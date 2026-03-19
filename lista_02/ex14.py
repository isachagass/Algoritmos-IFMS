numeros = list(map(int, input("Digite suas 3 notas: ").split(',')))
soma = 0
for num in numeros:
    soma += num
media = soma/3
if media >= 8 and media <= 10:
    print(f"Sua nota foi {media}, A")
elif media >= 7 and media < 8:
    print(f"Sua nota foi {media}, B!")
elif media >= 6 and media < 7:
    print(f"Sua nota foi {media}, C!")
elif media >= 5 and media < 6:
    print(f"Sua nota foi {media}, D!")
elif media >= 0 and media < 5:
    print(f"Sua nota foi {media}, E!")

    