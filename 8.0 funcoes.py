import os
os.system("clear")

def somar(n1, n2):
    calcular = n1 + n2
    return calcular

def subtrair(n1 , n2):
    calcular = n1 - n2
    return calcular

def multiplicar(n1, n2):
    calcular = n1 * n2
    return calcular

def dividir(n1, n2):
    calcular = n1 / n2
    return calcular

n1 = int(input("Digite o primeiro numero:"))
n2 =  int(input("Digite o segundo numero:"))


soma = somar(n1, n2)
subtracao = subtrair(n1, n2)
multiplicar = multiplicar(n1, n2)
dividir = dividir(n1, n2)


print(f"Soma: {soma}")
print(f"Subtracao: {subtracao}")
print(f"Multiplicacao: {multiplicar}")
print(f"Divisao: {dividir}")
print("FIm")