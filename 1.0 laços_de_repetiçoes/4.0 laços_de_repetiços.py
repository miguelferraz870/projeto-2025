
import os 
import time
os.system("clear") # limpa o terminal


numero = int(input("Digite seu numero para a contagem:"))

print("Contagem regressiva.")
for i in range(0,numero):
    print(f"{i}")
    time.sleep(1)

print("ACABOU")    