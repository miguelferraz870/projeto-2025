import os 


os.system("clear") # limpa o terminal


while True:
    idade = int(input("Digite sua idade:"))


    if idade < 18:
        print("Não autorizado. \nSomente maiores de 18.\n")

    else:
        break


print("Acesso Permitido.")
print("Fim")        
