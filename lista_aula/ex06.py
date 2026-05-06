lado1 = int(input("Digite o valor do lado 1: "))
lado2 = int(input("Digite o valor do lado 2: "))
lado3 = int(input("Digite o valor do lado 3: "))
angulo = int(input("Digite o valor do maior ângulo interno: "))

if lado1+lado2 > lado3:
    if lado2+lado3 > 1:
        if lado1+lado3 > lado2:
            print("O triângulo existe")

            match lado1:
                case lado1 if lado1 == lado2 and lado2 == lado3:
                        print("Triângulo Equilátero")
                case lado1 if lado1 == lado2 and lado2 != lado3:
                        print("Triângulo Isósceles")
                case lado1 if lado2 == lado3 and lado2 != lado1:
                        print("Triângulo Isósceles")
                case lado1 if lado1 == lado3 and lado1 != lado2:
                        print("Triângulo Isósceles")
                case lado1 if lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
                        print("Triângulo Escaleno")

            match angulo:
                case angulo if angulo == 90:
                    print("Triângulo Retângulo")
                case angulo if angulo > 90:
                    print("Triângulo Obtusângulo")
                case angulo if angulo < 90:
                    print("Triângulo Acutângulo ")
                

        else:
            print("Medidas Inválidas")
    else:
            print("Medidas Inválidas")
else:
            print("Medidas Inválidas")

