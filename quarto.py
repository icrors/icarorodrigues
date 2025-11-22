lista_a = [2, 3, 5]
lista_b = [1, 4, 2]

def escalar(a, b):
    aux = 0
    if len(a) != len(b): 
        return print("Vetores de tamanhos diferentes.")
    else:
        for i in range(len(a)):
            aux += a[i] * b[i]
        return print(aux)

escalar(lista_a, lista_b)