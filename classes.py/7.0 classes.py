import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Carro:
    marca: str
    modelo: str
    categoria: str
    preço: float

quantidade_carro = 2
     
for i in range(quantidade_carro):
    
    carro = Carro(
        marca = input("Digite a marca do carro:"),
        modelo = input("Digite o modelo do carro:"),
        categoria = input("Digite a categoria do carro:"),
        preço = float(input("Digite o preço do carro:"))
     )
    nome_arquivos = "dados_carros.txt"
    with open(nome_arquivos, "a") as arquivo:
        arquivo.write(f"{carro.marca},{carro.modelo},{carro.categoria},{carro.preço}\n")
        
    
print()    
print("salvandos dados dos carros")


print("\nSalvo com sucesso!")
                      