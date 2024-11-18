import random

valores = [random.randint(1, 5) for i in range(0, 26)]

conceitos = {
    "Excelente": 0,
    "Bom": 0,
    "Regular": 0,
    "Ruim": 0,
    "Péssimo": 0
}

keys = list(conceitos.keys())

for nota in valores:
    match nota:
        case 1:
            conceitos[keys[4]] += 1
        case 2:
            conceitos[keys[3]] += 1
        case 3:
            conceitos[keys[2]] += 1
        case 4:
            conceitos[keys[1]] += 1
        case 5:
            conceitos[keys[0]] += 1


values = list(conceitos.values())

posMaisVotado = values.index(max(values))

print(conceitos)

print(f"O conceito mais votado foi: {keys[posMaisVotado]}")
print(f"Que recebeu: {conceitos[keys[posMaisVotado]]} votos")