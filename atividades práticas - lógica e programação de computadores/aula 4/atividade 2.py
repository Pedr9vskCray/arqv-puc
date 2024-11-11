ano = int(input("Por favor digite o ano: "))
mes = int(input("Por favor digite o mês (1-12): "))
bissexto = None

# verificação de validade dos meses do ano

if (mes > 12 or mes < 1):
    print("Você digitou um mês inválido.")
    exit(1)

# hashmap com meses escritos por extenso

meses = {
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

# array com o número correspondente aos meses que tem 30 dias

days30 = [4, 6, 9, 11]

# verificação de ano bissexto

if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
    bissexto = True
else:
    bissexto = False

# verificação de meses e retorno do resultado

if mes == 2:
    if bissexto:
        print(f"O mês de {meses[mes]} do ano {ano} tem 29 dias.")
    else:
        print(f"O mês de {meses[mes]} do ano {ano} tem 28 dias.")
elif mes in days30:
    print(f"O mês de {meses[mes]} do ano {ano} tem 30 dias.")
else:
    print(f"O mês de {meses[mes]} do ano {ano} tem 31 dias.")