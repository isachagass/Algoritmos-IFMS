saldo_atual: float = 0

def deposito(valor, saldo_atual):
    if valor > 0:
        saldo_atual += valor
    else:
        print("Não é permitido um depósito negativo")
    return saldo_atual

def saque(valor, saldo_atual):
    if valor <= saldo_atual:
        saldo_atual -= valor
    else:
        print("Saldo insuficiente")
    return saldo_atual

menu = 0
while menu != 4:
    menu  = int(input("Escolha uma opção:\n1- Ver Saldo\n2- Depositar\n3- Saque\n4-Sair\n"))
    match menu:
        case 1:
            print(f"\nSaldo atual: {saldo_atual:.2f}\n")
        case 2: 
            valor = float(input("Digite o valor que será depositado: "))
            saldo_atual = deposito(valor, saldo_atual)
            print(f"\nSaldo atual: {saldo_atual:.2f}\n")
        case 3: 
            valor = float(input("Digite o valor que será sacado: "))
            saldo_atual = saque(valor, saldo_atual)
            print(f"\nSaldo atual: {saldo_atual:.2f}\n")
        case 4: 
            break
        case _:
            print("Digite uma opção válida,\n")
            continue