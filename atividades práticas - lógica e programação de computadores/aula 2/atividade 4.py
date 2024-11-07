import math

# verificação de entrada 1
try:
    valor = int(input("Digite um valor inteiro de 4 dígitos: "))
except ValueError:
    print("Você digitou um valor inválido.")
    exit(1)

# verificação de entrada 2
teste = str(valor)
if (len(teste) != 4):
    print("O número deve conter exatamente 4 dígitos.")
    exit(1)

# invertendo os valores de posição

primeiro = valor // 1000
segundo = (valor - primeiro*1000) // 100
terceiro = ((valor - primeiro*1000) - segundo*100) // 10
quarto = (((valor - primeiro*1000) - segundo*100) - terceiro * 10) // 1

invertido = str(quarto) + str(terceiro) + str(segundo) + str(primeiro)

print("O número %d invertido é igual a %d" %(valor, int(invertido)))