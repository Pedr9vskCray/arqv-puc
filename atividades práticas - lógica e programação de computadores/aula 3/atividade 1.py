try:
    num = int(input("Digite um número de 1-7: "))
except ValueError:
    print("Você digitou uma entrada inválida.")
    exit(1)

if (num >= 1 and num <= 7):
    semana = {
        1: "Segunda-Feira",
        2: "Terça-Feira",
        3: "Quarta-Feira",
        4: "Quinta-Feira",
        5: "Sexta-Feira",
        6: "Sábado",
        7: "Domingo"
    }

    print("O dia da semana que corresponde ao número %d é %s" %(num, semana[num]))
else:
    print("O número que você digitou não corresponde a um dia da semana.")
    exit(1)