import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class funcionaria:
    nome: str
    data_de_admissao: str
    matricula: str
    endereço: str

@dataclass
class cliente:
    nome: str
    data_de_nascimento: str
    endereço: str

lista_funcionarios = []
lista_clientes = []
quantidade_funcionario = 3
quantidade_cliente = 3

print("Informe os dados dos funcionarios")
for i in range(quantidade_funcionario):
    funcionario = funcionaria(
        nome=input("Nome:"),
        data_de_admissao=input("Data de Admissao:"),
        matricula=input("Matricula:"),
        endereço=input("Endereço:")
    )
    lista_funcionarios.append(funcionario)
    print()

    os.system("cls || clear") 

    with open("dados_funcionarios.txt", "a") as arquivo:
        for funcionario in lista_funcionarios:
            arquivo.write(f"{funcionario.nome}, {funcionario.data_de_admissao}, {funcionario.matricula}, {funcionario.endereço}\n")
            

 

    


