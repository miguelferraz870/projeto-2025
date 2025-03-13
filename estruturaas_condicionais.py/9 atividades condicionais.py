import os 

os.system("clear") # limpa o terminal

primeiro_numero = int(input("Digite seu primeiro numero: "))
segundo_numero = int(input("Digite seu segundo numero: "))
terceiro_numero = int(input("Digite seu terceiro numero: "))

maior = max (primeiro_numero, segundo_numero,terceiro_numero)
menor = min (primeiro_numero, segundo_numero,terceiro_numero)

print()
print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")