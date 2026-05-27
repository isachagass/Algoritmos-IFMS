numeros = [1,2,3,4,5,6,7,8]
mult_2 = []
mult_3 = []
for i in numeros:
    if i % 2 == 0:
        mult_2.append(i)
    if i % 3 == 0:
        mult_3.append(i)
print(f"Multiplos de 2: {mult_2}")
print(f"Multiplos de 3: {mult_3}")
