import os 

os.system("clear") # limpa o terminal



quantidade_maça= float(input("Digite a quantidade de maça desejada: "))

if quantidade_maça < 12:
    preço_maça = 1.30
else:
    preço_maça = 1.00

valor_total = quantidade_maça * preço_maça

print()
print(f"valor total da compra R$ {valor_total: .2f}")

