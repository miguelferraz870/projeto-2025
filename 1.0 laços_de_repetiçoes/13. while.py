import os 

os.system("clear") # limpa o terminal

login = "miguel"
senha = "12345"

for i in range(3):

    login = input("Digite seu login:")
    senha_cadastrada = input("Digite sua senha:")
    if login == login and senha == senha:
        print("====== Acesso Concedido ======")
        break
    else:
        print("====== Acesso Negado ======")
        if i == 2:
            print("===== tente novamente =====")

print()
print(f"login digitado : {login}") 
print(f" senha digitada : {senha}") 
  