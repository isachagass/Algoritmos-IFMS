valores = []
num = 1
while num != 0:
    num = int(input("digite 0 para para de registra\nDigite o valor da movimentação: "))
    valores.append(num)

arrecadacao = 0
gasto = 0
for i in valores:
    if i < 0 :
        gasto += i
    else:
        arrecadacao += i
gasto = gasto * -1
saldo_final = arrecadacao - gasto
if saldo_final < 0:
    result = "Prejuizo"
else:
    result = "Lucro"
print(f"Arrecadação: {arrecadacao}\nGastos: {gasto}\nSaldo Final: {saldo_final} - {result}")