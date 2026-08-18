numeros = (100, 20) #tupla (),
numeros = "100", "30" #tupla tambem com "" e ,

# print(numeros[0])

tupla = ("oi",) # se tiver só um elemneto tem que colocar virgula depois 
# print(type(tupla))

tupla_ = tuple() #declara uma tupla
# print(tupla_)

texto = tuple("isabelli") # quebra a palavra em caracteres
# print(texto) # ("i", "s", "a")

# if (0,1,2) < (0,3,4): # é comparado por posição, a 1 com 1 em ordem - até dar true or false - o primeiro que der já garante o resultado 
#     print(True)
# else:
#     print(False)

txt = "textooo mais de uma frase alecrin a"
palavras = txt.split() #split separa a string
lista = list()
for palavra in palavras:
    lista.append((palavra, len(palavra)))
# print(lista)

lista.sort() #ordena pelo primeiro parametro da lista -> lista = (par1, par2)
res= list()
for tamanho, palavra in lista:
    res.append(tamanho)
    # print(res)

exemplo = ("palavra1", "palavra2")
(x,y) = exemplo #distribui os valores nas variaveis
# print(x)
# print(y)

# inverter valores sem variavel auxiliar
x = 10
y = 20

print(x, y)
x, y = y, x
print(x, y)