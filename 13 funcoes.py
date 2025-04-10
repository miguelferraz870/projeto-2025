import os
os.system("clear")
 

def calcular_idade(ano_nascimento):
    return 2025 - ano_nascimento


ano_nascimento = int(input("Digite o ano de nascimento:"))

idade = calcular_idade(ano_nascimento)

print(f"Idade: {idade} ")