import os
os.system("clear")

quantidade_numeros = 5
lista_num = []

for i in range(quantidade_numeros):
    num = int(input(f"Digite o seu numero:")) 
    if numero < 0:
        numero = 0
        lista_num.append(numero)  

print("\n Numeros")        
for i, numero in enumerate(lista_num, start=1):
    print(f"{i}: {numero}")
    