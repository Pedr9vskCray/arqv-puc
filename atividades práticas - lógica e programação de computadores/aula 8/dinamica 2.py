import random

idades = [random.randint(18, 70) for i in range(1, 21)]

print(idades)

print(f"Idade da pessoa mais velha: {max(idades)}")
print(f"Idade da pessoa mais nova: {min(idades)}")
print(f"Média das idades da pessoas: {(sum(idades)/len(idades)):.2f}")