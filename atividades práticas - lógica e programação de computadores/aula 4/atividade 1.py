ano = int(input("Digite o ano: "))

# considerando que um ano que é divisível por 400 também é divisível por 100 e por 4
if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
    print(f"O ano {ano} é um ano bissexto.")
else:
    print(f"O ano {ano} não é um ano bissexto.")

# resolver esse exercício requer uma tabela de casos de teste para análise de padrões de soluções

# anos para teste:

# 2021
# 2000
# 2004
# 1900
