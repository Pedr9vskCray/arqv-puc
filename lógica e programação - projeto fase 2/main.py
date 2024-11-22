import csv
import matplotlib.pyplot as plt

data = {}

# lendo os dados do arquivo

with open("dados.csv", "r", newline="") as dados:

    myreader = csv.reader(dados, delimiter=',')

    info = []

    for line in myreader:
        info.append(line)

    keys = info[0]
    info.pop(0)

    for key in keys: data[key] = []

    for iol in info:
        for idx, value in enumerate(iol):
            data[keys[idx]].append(value)

# função para verificar o último dia de um mês informado

def return_date(data: str) -> str:
    mes = data[0:2]
    ano = data[3:7]

    if mes == '02':
        if int(ano) % 400 == 0 or int(ano) % 4 == 0:
            return '29/' + data
        else:
            return '28/' + data
    elif mes in ['01', '03', '05', '07', '08', '10', '12']:
        return '31/' + data 
    else:
        return '30/' + data

# recebendo as entradas do usuário - a)

while True:
    tempoInicial = str(input("Digite o mês e ano inicial da sua consulta (mm/yyyy): "))
    tempoFinal = str(input("Digite o mês e ano final da sua consulta (mm/yyyy): "))
    print("\n1 - Todos os Dados\n2 - Apenas os de Precipitação")
    print("3 - Apenas os de Temperatura\n4 - Apenas os de Umidade e Vento\n")
    try:
        valorOpcional = int(input("Escolha uma das opções: "))
    except ValueError:
        print("\nVocê não digitou um número correspondente a uma opção válida.")
        break

    tempoInicial = "01/" + tempoInicial

    tempoFinal = return_date(tempoFinal)

    # verificação de erros na entrada do usuário

    if tempoInicial not in data["data"] or tempoFinal not in data["data"]:
        print("\nVocê digitou uma data errada ou fora do escopo dos dados disponíveis.")
        exit(1)
        break

    if valorOpcional < 1 or valorOpcional > 4:
        print("\nVocê escolheu uma opção inválida.")
        exit(1)
        break

    # efetuando a filtragem com base nas datas informadas

    filtered_data = {}

    idx_inicial = data["data"].index(tempoInicial)
    idx_final = data["data"].index(tempoFinal)

    for idx in range(idx_inicial, idx_final+1):
        filtered_data[data["data"][idx]] = []
        for key in data.keys():
            if key == "data":
                pass
            else:
                filtered_data[data["data"][idx]].append(data[key][idx])

    # printando as informações na tela de acordo com as entradas do usuário
    
    match valorOpcional:
        case 1:
            print("\n")
            print("data -> precip - maxima - minima - horas_insol - temp_media - um_relativa - vel_vento")
            for key, value in filtered_data.items():
                print(key, "->", value)
            print("\n")
            break

        case 2:
            print("\n")
            print("data -> precip")
            for key, value in filtered_data.items():
                print(key, "->", value[0])
            print("\n")
            break

        case 3:
            print("\n")
            print("data -> maxima - minima")
            for key, value in filtered_data.items():
                print(key, "->", value[1], " - ", value[2])
            print("\n")
            break

        case 4:
            print("\n")
            print("data -> um_relativa - vel_vento")
            for key, value in filtered_data.items():
                print(key, "->", value[-2], " - ", value[-1])
            print("\n")
            break

# calculando o mês mais chuvoso - b)

def retornaMaiorPos(lista: list)->tuple:
    maior = 0

    for item in lista:
        if float(item) > maior:
            maior = float(item)

    idx_maior = lista.index(str(maior))

    return (maior, idx_maior)

while True:
    chuvosoInfo = retornaMaiorPos(data["precip"])
    chuvosoMes = data["data"][chuvosoInfo[1]]
    print(f"A data mais chuvosa (maior precipitação) foi o dia {chuvosoMes} com {chuvosoInfo[0]} de precipitação.")
    print("\n")
    break

# reorganizando os dados armazenados

data_new = {}

for idx, value in enumerate(data["data"]):
    data_new[value] = []
    for key in data.keys():
        if key == "data":
            pass
        else:
            data_new[value].append(data[key][idx])

# meses do ano relacionados com o seu número

months = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
    }

# calculando a média da temperatura mínima de um determinado mês - c)

medias = {}

while True:

    # validação de entrada

    mes = str(input("Digite o número do mês do ano (01-12): "))
    print("\n")

    if mes not in ['01', '02', '03', '04', '05', '06']:
        diaFinal = return_date(mes + "/" + "2015")
    else:
        diaFinal = return_date(mes + "/" + "2016")

    if diaFinal not in data["data"]:
        print("\nVocê digitou uma informação inválida que não corresponde a um mês do ano.")
        exit(1)
        break

    # determinando o nome do mes

    if mes[0] == "0":
        mesNome = months[int(mes[1])]
    else:
        mesNome = months[int(mes)]

    # determinando a quantidade de dias no mes

    qntDias = int(diaFinal[0:2])

    # efetuando o loop de coleta de dados

    if diaFinal[8:] == "15":
        for year in range(2006, 2016):
            ano = []
            for day in range(1, qntDias+1):
                if len(str(day)) < 2:
                    diaAtual = "0" + str(day) + "/" + mes + "/" + str(year)
                else:
                    diaAtual = str(day) + "/" + mes + "/" + str(year)
                min_temp = data_new[diaAtual][2]
                ano.append(float(min_temp))
            tag = mesNome + str(year)
            medias[tag] = sum(ano)/qntDias
            ano.clear()

    elif diaFinal[8:] == "16":
        for year in range(2006, 2017):
            ano = []
            if year % 4 == 0 and mes == "02":
                qntDias = 29
            elif year % 4 != 0 and mes == "02":
                qntDias = 28
            for day in range(1, qntDias+1):
                if len(str(day)) < 2:
                    diaAtual = "0" + str(day) + "/" + mes + "/" + str(year)
                else:
                    diaAtual = str(day) + "/" + mes + "/" + str(year)
                min_temp = data_new[diaAtual][2]
                ano.append(float(min_temp))
            tag = mesNome + str(year)
            medias[tag] = sum(ano)/qntDias
            ano.clear()

    for key, value in medias.items():
        print(f"{key} -> {value:.2f}")
    print("\n")
    break

# calculando a média geral da temperatura mínima de um determinado mês - e)

media_geral = 0
for value in medias.values():
    media_geral = media_geral + value

print(f"A média geral de temperatura no mês de {mesNome} no período de {len(medias.values())} é {(media_geral/len(medias.values())):.2f}")

print("\n")

# plotando o gráfico de barras vertical - d)

plt.figure(figsize=(17, 8))

fonts_properties = {
    'family' : 'Times New Roman',
    'color' : 'grey',
    'weight' : 'medium',
    'size' : 16
}

plt.grid(
    c='grey',
    ls='solid',
    lw=1.5,
    alpha=0.15
)

x, y = zip(*medias.items())

plt.title(f"Gráfico da temperatura média mínima do mês de {mesNome} ao longo dos anos.", fontdict=fonts_properties)
plt.xlabel("Anos", fontdict=fonts_properties)
plt.ylabel("Temperaturas", fontdict=fonts_properties)

plt.bar(x, y, color="#7690ac", width=0.4)

plt.show()







            
    

    


