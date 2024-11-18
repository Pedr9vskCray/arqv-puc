import random

roupas = []

for i in range(1, 51):
    roupas.append((random.choice(["P", "M", "G"]), random.choice(["Branco", "Preto", "Azul"])))

dadosTamanho = {
    "P": 0,
    "M": 0,
    "G": 0
}

dadosCor = {
    "Branco": 0,
    "Preto": 0,
    "Azul": 0
}

for roupa in roupas:
    match roupa[0]:
        case "P":
            dadosTamanho["P"] += 1
        case "M":
            dadosTamanho["M"] += 1
        case "G":
            dadosTamanho["G"] += 1

    match roupa[1]:
        case "Branco":
            dadosCor["Branco"] += 1
        case "Preto":
            dadosCor["Preto"] += 1
        case "Azul":
            dadosCor["Azul"] += 1

posMaisVendido = list(dadosTamanho.values()).index(max(dadosTamanho.values()))

qntVendidoM = dadosTamanho["M"]

posCorPreferida = list(dadosCor.values()).index(max(dadosCor.values()))

print(dadosTamanho)
print(dadosCor)

print("\n")

print(f"O tamanho que mais vendeu foi o: {list(dadosTamanho.keys())[posMaisVendido]}")

print(f"A quantidade de peças de tamanho M vendidas foram: {qntVendidoM}")

print(f"A cor preferida dos clientes com base nas últimas 50 vendas foi a cor: {list(dadosCor.keys())[posCorPreferida]}")