import math

segundos = int(input("Digite o tempo em segundos: "))
tempo_original = segundos
minutos = 0
horas = 0

if (segundos > 59):
    minutos = segundos // 60
    segundos = segundos - (minutos * 60)

    if (minutos > 59):
        horas = minutos // 60
        minutos = minutos - (horas * 60)

print("O tempo de %d segundos corresponde a:\n" %tempo_original)
print(" - %d horas" %horas)
print(" - %d minutos" %minutos)
print(" - %d segundos" %segundos)
print("\n")