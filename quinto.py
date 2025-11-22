num = input("Digite um número: ")

try: 
    num = float(num)
    
    if  num.is_integer():
        num = int(num)
        if num % 2 == 0: print("Número é inteiro e Par.")
        else: print("Número é inteiro e Impar.")
    else:
        print(f"Inteiro: {int(num)}")
        print(f"Decimal: {num - int(num)}")
except:
    print("O valor não pode ser convertido para float.")