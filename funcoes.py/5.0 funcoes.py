import os
os.system("clear")

def verificar(numero):
    if numero %2 == 0:
        print("O numero é par.")

    else:
        print("O numero é impar.")

print("Verificando se um numero é par ou impar.")
numero = int(input("Digite um numero : ")) 
verificar(numero)       
