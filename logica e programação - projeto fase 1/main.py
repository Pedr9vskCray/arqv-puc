# declarando a estrutura para armazenamento dos dados coletados

data = {}

# declarando a relação dos meses do ano com os números

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

# considerando que cada mês do ano corresponde a um número de 1-12, podemos também declarar uma lista simples para
# acompanhar quais meses já foram informados, aonde caso o número não esteja na lista, a informação já foi declarada

udcl_months = [i for i in range(1,13)]

# iniciando o loop de coleta de dados

while len(udcl_months) > 0:
    try:
        current_month = int(input("Por favor insira o mês do ano que você deseja informar a temperatura (1-12): "))
    # verificando a validade da informação declarada
    except ValueError:
        print("\nPor favor digite somente números inteiros referentes aos meses do ano.\n")
        continue
    if current_month > 12:
        print("\nPor favor digite somente números inteiros referentes aos meses do ano.\n")
        continue
    # verificando se o mês escolhido já possui informações de temperatura declaradas
    if (current_month in udcl_months):
        # coletando as informações de temperatura do mês escolhido
        try:
            current_temperature = float(input(f"Por favor insira a temperatura máxima referente o mês de {months[current_month]}: "))
            print("\n")
        except ValueError:
            print("\nPor favor informe somente valores numéricos decimais referentes as temperaturas.\n")
            continue
        # armazenando as informações coletadas na nossa estrutura
        data[current_month] = current_temperature
        # removendo o mês que acabamos de coletar da lista de meses não declarados
        udcl_months.remove(current_month)
    else:
        print(f"\nO mês de {months[current_month]} já possui sua temperatura máxima declarada.\n")
        continue

print("\n")

# agora que temos os dados de todos os meses do ano, basta calcularmos as saídas com base nos dados coletados

avg_temp = 0
n_months = 0
hottest_month = None
coldiest_month = None

keys = list(data.keys())
values = list(data.values())

# calculando a temperatura média e a quantidade de meses escaldantes

for temp in values:
    if temp > 33:
        n_months += 1
    
    avg_temp += temp

avg_temp = avg_temp / 12

# calculando qual foi o mês mais quente do ano

max_temp = max(values)

max_idx = values.index(max_temp)

max_month = keys[max_idx]

hottest_month = months[max_month]

# calculando qual foi o mês mais frio do ano

min_temp = min(values)

min_idx = values.index(min_temp)

min_month = keys[min_idx]

coldiest_month = months[min_month]

# printando as informações calculadas

print("A temperatura média máxima anual foi de %.2f°." %avg_temp)
print(f"A quantidade de meses considerados escaldantes foi de {n_months} meses.")
print(f"O mês mais escaldante do ano foi o mês de {hottest_month}.")
print(f"O mês menos quente do ano foi o mês de {coldiest_month}.")
    
    