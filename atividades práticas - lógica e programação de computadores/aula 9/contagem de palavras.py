import nltk
import string

palavras = {}

#nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

with open("Don Casmurro - Machado de Assis.txt", "rt") as livro:
    for linha in livro.readlines():
        texto = linha.replace('\n', '').split(' ')
        if texto == ['']:
            pass
        else:
            for item in texto:
                if (item in stopwords) or (item in string.punctuation): # removendo os conectivos mais comuns usando o nltk
                    pass
                else:
                    if item in palavras:
                        palavras[item] += 1
                    else:
                        palavras[item] = 1

contador = 1

# função lambda para organizar os items em ordem decrescente com base no valor

for key, value in sorted(palavras.items(), key=lambda foo: foo[1], reverse=True):
    if contador < 30:
        print(f"\n{contador} - {key} => {value}")
    else:
        break
    contador += 1
    




