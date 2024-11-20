texto = str(input("Digite um texto para verificar a frequência de cada letra: "))

letter_freq = {}

for letra in texto:
    if letra == ' ' or letra == '\n':
        pass
    else:
        if letra in letter_freq:
            letter_freq[letra] += 1
        else:
            letter_freq[letra] = 1

key, value = zip(*letter_freq.items())

for letra in sorted(key):
    print(f"\nA letra {letra} aparece {letter_freq[letra]} vezes na frase.")