cadastros = 0 
valor = 0
maior = 0
produto = 1

while produto != 0:
    produto = float(input("Digite o preço do produto: "))
    valor += produto
    if produto != 0:
        cadastros +=1

    if produto > 50:
        maior += 1
media = valor / cadastros

print(f"Total de itens cadastrados: {cadastros}\nValor total da compra: R${valor}\nMédia de preços: R${media}\nQuantidade de produtos que custam mais que R$50.00: {maior}")