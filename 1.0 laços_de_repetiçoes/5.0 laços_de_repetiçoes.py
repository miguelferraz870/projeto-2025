import os 
import time

os.system("clear") # limpa o terminal

soma = 0

for i in range(1, 6):
    numero = int(input("Digite um numero:"))
    soma = soma + numero
    soma += numero 

print(f"Soma: {soma}")    