import os 

os.system("clear") # limpa o terminal


while True:
     login = input("Digite seu login:")
     senha = input("Digite sua senha:")
     login_cadastrado = "miguel"
     senha_cadastrada = "12345"

     if login != login_cadastrado and senha != senha_cadastrada:
        print("Login ou senha estão invalidos")
     elif login == login_cadastrado and senha == senha_cadastrada:
        print("Login e senha estão corretos ")
     else:
         break   
        
     
print() 
print(f"login cadastrado : {login}")
print(f"Senha cadastrada : {senha}")
            


