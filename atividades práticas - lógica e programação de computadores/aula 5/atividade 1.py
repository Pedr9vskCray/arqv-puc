import random

# gerando o número aleatório

num = random.randint(1, 100)

# criando o loop de adivinhação do usuário

acertou = False

for chances in range(10, 0, -1):
    # recebendo o chute do usuário
    guess = int(input("Tente adivinhar o número de 1-100 que eu estou pensando: "))
    if (guess > 100 or guess < 0):
        print("Você digitou um número inválido e perdeu 1 chance.")
        print(f"Você ainda tem {chances-1} chances")
    # fazendo os testes
    elif guess == num:
        print("Parabéns você adivinhou!")
        print(f"Você ainda tem {chances-1} chances restantes, essa é sua pontuação final.")
        acertou = True
        break
    elif guess > num:
        print("Você errou, o número que você digitou é maior do que o número que eu estou pensando")
        print(f"Você ainda tem {chances-1} chances")
    else:
        print("Você errou, o número que você digitou é menor do que o número que eu estou pensando")
        print(f"Você ainda tem {chances-1} chances")

# verificando se o jogador acertou o número

if acertou:
    pass
else:
    print("Você gastou todas as suas chances e não conseguiu adivinhar o número correto.")
    print(f"O número que eu estava pensando era o número {num}")