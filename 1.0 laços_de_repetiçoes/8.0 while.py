import os 


os.system("clear") # limpa o terminal


idade = int(input("Digite sua idade:"))


while idade < 18:
    print("Não autorizado. \nSomente maiores de 18.\n")
    idade = int(input("Digite sua idade:"))


print("Acesso permitido.")
print("fim.")   