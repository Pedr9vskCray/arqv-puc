import math

a = float(input("Digite o valor para a: "))
b = float(input("Digite o valor para b: "))
c = float(input("Digite o valor para c: "))

# se assegurando que a != 0

if a == 0:
    print("Para evitar uma divisão por zero, 'a' não pode ser zero.")
    exit(1)

# calculando o delta

delta = math.pow(b, 2) - (4 * a * c)

# se assegurando que o delta > 0

if delta < 0:
    print("Impossível continuar o cálculo pois não existe raiz quadrada de um número negativo.")
    exit(1)

# calculando x1 e x2

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print("x1 = %.2f" %x1)
print("x2 = %.2f" %x2)