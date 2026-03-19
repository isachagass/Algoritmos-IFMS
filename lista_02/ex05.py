numeros = list(map(int, input("Digite 5 números: ").split(",")))

maiores = []
for num in numeros:
    if num > 100:
        maiores.append(num) 
    
print(f"Numeros maiores que 100 = {maiores}")