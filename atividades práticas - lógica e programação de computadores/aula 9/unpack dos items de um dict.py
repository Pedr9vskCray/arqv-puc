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

# unpack dos items de um dicionário de forma elegante

keys, values = zip(*months.items())

print(keys, end="\n")
print(values, end="\n")