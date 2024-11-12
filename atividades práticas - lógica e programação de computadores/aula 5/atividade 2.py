import random

# simulando as entrevistas

info = {}

for i in range(0, 2000):
    info[i] = [
        random.randint(18, 80), # idade
        random.randint(1200, 12000), # renda
        random.choice(["Masculino", "Feminino"]), # gênero
        random.randint(0, 5) # qnt de filhos
    ]

# preparando o armazenamento dos cálculos

data = {}

# calculando a renda média entre os entrevistados
# calculando a media das idades de quem tem mais que 3 filhos
# calculando a media do número de filhos

mediaRenda = 0

mediaIdades = 0
qntIdades = 0

mediaFilhos = 0

for core in info.values():
    mediaRenda = mediaRenda + core[1] # renda média

    if core[3] > 3:
        mediaIdades = mediaIdades + core[0] # média das idades de quem tem mais que 3 filhos
        qntIdades += 1 # quantidade de pessoas com mais de 3 filhos

    mediaFilhos = mediaFilhos + core[3] # média do número de filhos

data["a"] = round(mediaRenda/2000, 2)
data["b"] = round(mediaIdades/qntIdades, 2)
data["d"] = round(mediaFilhos/2000, 2)

# calculando a quantidade homens com menos de 30 anos
# calculando a renda do homem mais velho
# calculando a idade da mulher com mais renda

qntHomens = 0

posMaisVelho = 0

posMulherRenda = 0

contador = 0

for core in info.values():
    
    if core[0] < 30: # quantidade homens com menos de 30 anos
        qntHomens += 1

    if core[2] == "Masculino" and core[0] >= info[posMaisVelho][0]: # posição do homem mais velho
        posMaisVelho = contador

    if core[2] == "Feminino" and core[1] >= info[posMulherRenda][1]: # posição da mulher com maior renda
        posMulherRenda = contador

    contador += 1

data["c"] = qntHomens
data["e"] = info[posMaisVelho][1]
data["f"] = info[posMulherRenda][0]

# printando os valores na tela

print(f'Média de Renda: {data["a"]}')
print(f'Média da idade de quem tem mais que 3 filhos: {data["b"]}')
print(f'Quantidade de homens com menos de 30 anos: {data["c"]}')
print(f'Média do número de filhos: {data["d"]}')
print(f'Renda do homem mais velho: {data["e"]}')
print(f'Idade da mulher com a maior renda: {data["f"]}')
