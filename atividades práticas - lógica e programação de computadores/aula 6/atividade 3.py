# variáveis de controle

qntHabitantes = 0
somaSalario = 0

maiorIdade = 0

menorIdade = 0

qntMulheres = 0

# loop de coleta de informações

while True:

    idade = int(input("Digite a idade do habitante: "))
    if idade < 0:
        break

    sexo = str(input("Digite o sexo do habitante (m-f): "))
    if sexo not in "mf":
        print("Sexo inválido.")
        continue

    salario = float(input("Digite o salário do habitante: "))

    print("\n")

    qntHabitantes += 1

    # somando salario

    somaSalario += salario

    # setando a primeira idade como a maior e menor

    if maiorIdade == 0 and menorIdade == 0:
        maiorIdade = idade
        menorIdade = idade

    # maior e menor idade do grupo

    if idade > maiorIdade:
        maiorIdade = idade

    if idade < menorIdade:
        menorIdade = idade

    # quantidade de mulheres com salário acima de 3500

    if sexo == "f" and salario > 3500:
        qntMulheres += 1

# printando as informações

print(f"A média salarial do grupo é {somaSalario / qntHabitantes}.")
print(f"A pessoa mais velha tem {maiorIdade} anos e a pessoa mais nova tem {menorIdade} anos.")
print(f"A quantidade de mulheres com o salário acima de 3500 são {qntMulheres}")
