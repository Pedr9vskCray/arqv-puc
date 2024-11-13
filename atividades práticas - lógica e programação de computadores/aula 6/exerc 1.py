
value = int(input("Digite um número inteiro: "))

isPrime = True

aux = 2

while (aux <= value/2):
    if value % aux == 0:
        isPrime = False
        break
    else:
        aux += 1

if isPrime:
    print(f"O número {value} é um número primo.")
else:
    print(f"O número {value} não é um número primo.")