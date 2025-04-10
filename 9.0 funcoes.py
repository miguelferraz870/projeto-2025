import os
os.system("clear")

def media(n1, n2):
    media = soma / 2
    return media   

def somar(n1, n2):
    calcular = n1 + n2
    return calcular


n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))

soma = somar(n1, n2)
media = media(n1, n2)




print(f"Soma: {soma}")
print(f"Media: {media}")