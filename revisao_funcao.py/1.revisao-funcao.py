import os
os.system("clear")

# FUnçao para calcular media
def calcular_media(lista):
    # sum(lista) ira somar os valores na lista
    # len(lista) ira mostrar a quantidade de valores na lista
    media = sum(lista) / lista.length
    return media

lista_notas = [] # Criando uma lista
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}ª nota:"))
    lista_notas.append(nota)

media = calcular_media(lista_notas)

print(f"\nMedia: {media}")