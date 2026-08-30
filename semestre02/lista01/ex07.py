def tubulencia(altitudes):
    maior_queda = 0
    turbulencia = False

    for i in range(1, len(altitudes)):
        if altitudes[i] < altitudes[i-1]:
            queda = altitudes[i-1] - altitudes[i]
            if queda > maior_queda:
                maior_queda = queda
            if queda > 500:
                turbulencia = True

    return maior_queda, turbulencia

altitudes = [1000, 1200, 600, 900, 800, 700, 600, 500]
queda_max, turbulencia = tubulencia(altitudes)
print("Queda Máxima:", queda_max)
print("Turbulência:", turbulencia)