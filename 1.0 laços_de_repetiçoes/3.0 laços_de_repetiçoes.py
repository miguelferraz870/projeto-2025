import os 
import time

os.system("clear") # limpa o terminal


numero = int(input("Digite um numero para tabuada:"))










print(f"\nTabuada do numero {numero}:")
for i in range(1,100):
    print(f"{numero} x {i} = {i*numero}")   
    time.sleep(0.1)

print("ACABOU")    