import random

valores = [random.randint(1, 500) for i in range(1, 31)]

print(valores)

print("O maior valor da lista é: %d" %(max(valores)))
print("A quantidade de pares na lista é: %d" %len([i for i in valores if i % 2 == 0]))