lista = []
primos = []
nao_primos = []

for i in range(1,11): lista.append(i)

for n in lista:
    divisores = 0

    for i in range(1, n+1):
        if n % i == 0: divisores += 1
    
    if divisores == 2: primos.append(n)
    else: nao_primos.append(n)
    