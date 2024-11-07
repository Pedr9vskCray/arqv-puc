import math

try:
    value1 = int(input("Por favor digite o primeiro número inteiro: "))
    value2 = int(input("\nPor favor digite o segundo número inteiro: "))
except ValueError:
    print("\nVocê digitou números inválidos.")
    exit(1)

print("Soma: %d + %d = %d" %(value1, value2, value1 + value2))
print("Diferença: %d - %d = %d" %(value1, value2, value1 - value2))
print("Média: (%d + %d) / 2 = %d" %(value1, value2, (value1 + value2) / 2))
print("Distância: |%d - %d| = %d" %(value1, value2, math.fabs(value1 - value2)))
print("Maior: %d" %((value1 + value2 + math.fabs(value1 - value2)) / 2))
print("Menor: %d" %((value1 + value2 - math.fabs(value1 - value2)) / 2))