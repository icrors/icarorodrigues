produtos = {
    "Alimentação" : [12.50, 8.99, 15.30],
    "Limpeza" : [5.20, 7.80],
    "Higiene" : [10.00,12.00, 9.50, 14.00]
}

medias = {}

for chave, valor in produtos.items():
    soma = 0
    for i in valor:
        soma += i
    
    media = soma/len(valor)
    medias[chave] = media

aux = {}
aux = sorted(medias.items())

nome = list(medias.keys())[0]
valor = list(medias.values())[0]

print(f"O vencedor foi {nome}\nCom a média de R${round(valor, 2)}")
