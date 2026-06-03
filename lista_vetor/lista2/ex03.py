funcionarios = ['Ana', 'Bruno', 'Carlos', 'Diana']
salarios = [1500.0, 3200.0, 1800.0, 4500.0]
for i in range(len(salarios)):
    if salarios[i] <= 2000:
        salarios[i] += salarios[i]*0.15
    elif salarios[i] > 2000:
        salarios[i] += salarios[i]*0.10
    
    print(f"Nome: {funcionarios[i]} - Novo Salario: R${salarios[i]}")
