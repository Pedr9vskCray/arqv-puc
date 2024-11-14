import random

# função para escolher uma palavra

def word()->str:
    palavras = [
    "esquema", "sutileza", "pandemia", "certeza", "acender", "embaraço", 
    "gigante", "empatia", "ambiente", "sossego", "influência", "abundante", 
    "frenético", "destemido", "surpreender", "harmonia", "manutenção", 
    "abstrato", "detalhado", "versátil", "infinito", "claridade", "liberdade", 
    "singular", "explosivo", "conquista", "otimismo", "frequente", "serenidade", 
    "notável", "gentileza", "complexo", "vigoroso", "profundo", "triunfo", 
    "curiosidade", "imprevisto", "magnitude", "deslumbrar", "poderoso", 
    "impressionante", "realidade", "estratégia", "eficiência", "melhoria", 
    "disciplina", "avançado", "espetáculo", "discreta", "idealizar"
    ]
    return random.choice(palavras)

# definindo o esboço do jogo

vidas = 5

palavra = word()

certo = list(palavra)

chutes = []

while vidas > 0:

    print(f"\nVocê tem {vidas} vidas.\n")

    for letra in palavra:
        if letra not in certo:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    
    print("\n")

    if len(certo) == 0:
        print("\nVocê ganhou, parabéns!")
        break

    chute = str(input("Digite uma letra: "))

    if len(chute) > 1:
        print("Você digitou uma entrada inválida.")
        continue

    if chute in chutes:
        print("Você já tentou essa letra.")
        continue

    if chute in palavra:
        print("Você acertou uma letra.")
        chutes.append(chute)

        while chute in certo:
            certo.remove(chute)

    elif chute not in palavra:
        print("Você errou.")
        chutes.append(chute)
        vidas = vidas - 1

if vidas == 0:
    print("\nVocê perdeu, tente mais uma vez!")