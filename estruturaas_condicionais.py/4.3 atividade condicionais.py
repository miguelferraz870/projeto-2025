import os 

os.system("clear") # limpa o terminal

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Nao pode votar.")

if idade >= 16 and idade <=17:
    print("voce tem o voto opcional")

if idade >= 18 and idade <=65:
    print("voce é obrigado a votar!")
else:
    print("voce nao é obrigado a votar")