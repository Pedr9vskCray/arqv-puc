try:
    saldoMedio = float(input("Digite seu saldo bancário médio: "))
except ValueError:
    print("Por favor digite somente valores válidos.")
    exit(1)

if (saldoMedio < 500):
    print("Você não possui limite.")
elif (saldoMedio >= 500 and saldoMedio < 1000):
    limite = saldoMedio * 0.08
    print("Seu limite atual é de %.2f reais" %limite)
elif (saldoMedio >= 1000):
    limite = saldoMedio * 0.15
    print("Seu limite atual é %.2f" %limite)