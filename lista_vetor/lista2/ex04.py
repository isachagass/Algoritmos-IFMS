precos = []
num = 1
while num != 0:
    num = int(input("Digite o preco do produto: "))
    if num == 0:
        continue
    precos.append(num)

total_bruto = sum(precos)
desconto, total_pago = 0, 0

if len(precos) > 10:
    desconto = total_bruto*0.05

total_pago = total_bruto - desconto
print(f"Qauntidade de produtos: {len(precos)}\nValor Bruto: {total_bruto}\nDesconto: {desconto}\nValor a ser pago: {total_pago}")