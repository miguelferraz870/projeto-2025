import os
from unittest import case 

os.system("clear") # limpa o terminal

valor_produto =  float(input("Digite o valor do produto: "))

print("""
========== forma de pagamento ==========
               
1   \t\tA vista
2   \t\tA prazo
      
""")

forma_de_pagamento = int(input("Digite a forma de pagamento: "))

match forma_de_pagamento:
    case "1":
        desconto = valor_produto * 0.10
        valo_com_desconto = valor_produto - desconto

        
    case "2":
        parcelas = int(input("Digite a quantidade de parcelas: "))
        if quantidade_parcelas < 1 or quantidade_parcelas > 6:
            print ("Opçao invalida")
    case _:
        print("opçao invalida.")   

print()
print = ("Valorfinal:{valorfinal}")