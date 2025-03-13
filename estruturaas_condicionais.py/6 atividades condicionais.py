import os 

os.system("clear") # limpa o terminal

login_cadastrado = "aluno"
senha_cadastrada = "123"

login = input("Digite seu login: ")
senha = input(" Digite sua senha: ")

if login_cadastrado == login and senha_cadastrada == senha:
   print("bem vindo!")
else:
     print("login ou senha invalidos!")