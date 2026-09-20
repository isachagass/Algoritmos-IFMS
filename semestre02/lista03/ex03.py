lista = [1,2,3,4,5,6,7,8,9,10]

sub_a = lista[::2]

sub_b = []
for i in lista:
    if i % 2 != 0:
        sub_b.append(i)

sub_c = lista[::-1]

print("Elementos em indices pares:",sub_a)
print("Elementos ímpares:", sub_b)
print("Lista invertida: ",sub_c)