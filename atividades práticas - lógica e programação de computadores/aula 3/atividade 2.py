# verificando se todos os valores digitados são números inteiros

try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
except ValueError:
    print("Você digitou valores inválidos.")

# organizando a menor nota na nota1

if (nota2 < nota1):
    aux = nota1
    nota1 = nota2
    nota2 = aux

if (nota3 < nota1):
    aux = nota1
    nota1 = nota3
    nota3 = aux

# organizando a maior nota na nota3

if (nota3 < nota2):
    aux = nota2
    nota2 = nota3
    nota3 = aux

# verificando se as notas estão em um intervalo de 0-10

if (nota1 < 0 or nota3 > 10):
    print("Notas inválidas, os valores devem estar entre 0-10.")
    exit(1)

# calculando a média ponderada

media = ((0.5 * nota3) + (0.25 * nota2) + (0.25 * nota1))

print("A média é %.2f" %media)


