# conjectura de goldbach

n = int(input("Digite um número inteiro: "))

# calculando os números primos de 2 até n

primeNum = []

for i in range(2, n+1):
    aux = 2
    isPrime = True
    while (aux <= i/2):
        if i % aux == 0:
            isPrime = False
            break
        else:
            aux += 1
    if isPrime:
        primeNum.append(i)

# fazendo os testes para as diferentes partes dos números

for num in range(4, n+1):
    if num % 2 == 0:
        for x in primeNum: # parte 1
            for y in primeNum: # parte 2
                if (x + y) == num:
                    print(f"{num} = {x} + {y}")
