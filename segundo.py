lista = [("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9), ("João", 4), ("Bia", 6)]

dicionario = {}

for chave, valor in lista:
    if chave not in dicionario:
        dicionario[chave] = []
    dicionario[chave].append(valor)

medias = {}

for chave, valor in dicionario.items():
    soma = 0
    for i in valor:
        soma += i
    
    media = soma/len(valor)
    medias[chave] = media

print(sorted(medias.items()))
