import os 
import time

os.system("clear") # limpa o termina

nota = 0
soma = 0


for i in range(3):
 nota += float(input("informe suas notas:"))
    
media = nota / 3

if media >= 7:
    print("Aprovado")

elif media <= 4:
    print("Reprovado")
 









print(f"Media {nota}")
 
