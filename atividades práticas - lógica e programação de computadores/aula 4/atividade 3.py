# 2022 - inss e irrf

bruto = float(input("\nDigite seu salário bruto: "))
dependentes = int(input("Digite a quantidade de dependentes que você possui: "))

print("\n")

# calculando o desconto do inss

if (bruto < 1212):
    inss = bruto * 0.075 # sem parcela a deduzir
elif (bruto > 1212.01 and bruto < 2427.35):
    inss = (bruto * 0.09) - 18.18
elif (bruto > 2427.36 and bruto < 3641.03):
    inss = (bruto * 0.12) - 91
elif (bruto > 3641.04 and bruto < 7087.22):
    inss = (bruto * 0.14) - 163.82
else:
    inss = 828.39

# calculando o desconto do irrf

base = bruto - inss - (dependentes * 189.59)

if (base < 1903.98):
    irrf = 0
elif (base > 1903.99 and base < 2826.65):
    irrf = (base * 0.075) - 142.80
elif (base > 2826.66 and base < 3751.05):
    irrf = (base * 0.15) - 354.80
elif (base > 3751.06 and base < 4664.68):
    irrf = (base * 0.225) - 636.16
else:
    irrf = (base * 0.275) - 869.36

# calculando o salário líquido

liquido = bruto - inss - irrf
print("INSS -> %.2f" %inss)
print("IRRF -> %.2F" %irrf)
print("Seu salário líquido com %d dependente(s) é de %.2f\n" %(dependentes, liquido))
