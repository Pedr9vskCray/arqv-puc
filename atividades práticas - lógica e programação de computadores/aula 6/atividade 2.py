stop = False

numbers = []

while not stop:
    entry = int(input("Digite um número inteiro positivo: "))
    if entry < 0:
        stop = True
    else:
        numbers.append(entry)

# variáveis de controle de quantidade

qnt0_25 = 0
qnt26_50 = 0
qnt51_75 = 0
qnt76_100 = 0

for num in numbers:
    if num <= 25:
        qnt0_25 += 1
    elif num >= 26 and num <= 50:
        qnt26_50 += 1
    elif num >= 50 and num <= 75:
        qnt51_75 += 1
    else:
        qnt76_100 += 1

# printando os valores

print(f"Quantidade de números entre 0-25: {qnt0_25}")
print(f"Quantidade de números entre 26-50: {qnt26_50}")
print(f"Quantidade de números entre 51-75: {qnt51_75}")
print(f"Quantidade de números entre 76-100: {qnt76_100}")