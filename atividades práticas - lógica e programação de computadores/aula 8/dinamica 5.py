# lendo as frases

n = int(input("Digite a quantidade de frases que você deseja ler: "))

frases = []

for i in range(n):
    frases.append(str(input("Digite a frase: ")))

# segmentando as frases

tokens = []

for frase in frases:
    tokens.append(frase.split(' '))

# printando os resultados

for info in tokens:
    print(info)