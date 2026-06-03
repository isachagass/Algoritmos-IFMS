votos = [1, 2, 3, 2, 2, 1, 3, 1, 2, 3, 2, 2, 1, 3,1, 2, 3, 2, 2, 2]
ruim = boa = excelente = 0
for i in votos:
    if i == 1:
        ruim += 1
    elif i == 2:
        boa += 1
    else:
        excelente += 1
vencedora = 0
if ruim > boa and ruim > excelente:
    vencedora = "Ruim"
elif boa > ruim and boa > excelente:
    vencedora = "Boa"
else: 
    vencedora = "Excelente"
print(f"Ruim: {ruim} = {ruim*5}%\nBoa: {boa} = {boa*5}%\nExcelente: {excelente} = {excelente * 5}% \nVencedora: {vencedora}")
# print(ruim, boa, excelente)
# print(f"{boa * 5}")