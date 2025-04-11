import os
os.system("clear")


lista = []

for i in range(5):
    numero = float(input("Digite o numero':"))
    lista.append(numero)

numero_maior = max(lista) 
numero_menor = min(lista)

print()
print(f"O Maior numero é: {numero_maior}")
print(f"O Menor numero é: {numero_menor}")