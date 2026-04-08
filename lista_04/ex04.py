import math

def bhaskara(a,b,c):
    delta = (b*b) - (4*a*c)
    if delta < 0 :
        return print("não é possivel calcular raízes")
    elif delta == 0:
        delta = math.sqrt(delta)

        x = (-b + delta) / (2*a)
        return print("x=",x)
    else:
        delta = math.sqrt(delta)
        x1 = (-b + delta) / (2*a)
        x2 = (-b - delta) / (2*a)
        return print(f"x1={x1}\nx2={x2}")

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

bhaskara(a,b,c)