import os 
import time

os.system("clear") # limpa o terminal


pares = 0
impares = 0


for i in range(5):
    numero = int(input(f"Digite o {i+1} numero inteiro: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print()
print(f"quantidade de numeros pares: {pares}") 
print(f"quantidade de numeros impares: {impares}")         