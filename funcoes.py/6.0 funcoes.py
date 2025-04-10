import os
os.system("clear")

def verificar(numero):
    if numero > 0:
        print(f" {numero} é positivo")

    elif numero ==0:
        print(" 0 é neutro")

    else:
        print(f" {numero} é negativo")


print("Verificando se um numero é positivo ou negativo.")
numero = int(input("Digite um numero :"))
verificar(numero)