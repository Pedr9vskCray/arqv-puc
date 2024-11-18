import random

lista1 = [random.randint(1, 301) for i in range(1, 31)]
lista2 = []

print(lista1)
print(lista2)
print("\n")

while len(lista2) < 10:
    aux = max(lista1)
    lista1.remove(aux)
    lista2.append(aux)
    print(lista1)
    print(lista2)
    print('\n')