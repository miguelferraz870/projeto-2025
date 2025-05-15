import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class funcionario:
    nome: str
    data_de_admissao: str
    matricula: str
    endereco: str

@dataclass
class cliente:
    nome: str
    data_de_nascimento: str
    endereco: str

lista_funcionarios = []
lista_clientes = []
quantidade_funcionario = 3
quantidade_cliente = 3


for i in range(quantidade_funcionario):
    print("Informe os dados dos funcionarios")
    funcionario = funcionario(
        nome=input("Nome:"),
        data_de_admissao=input("Data de nascimento:"),
        matricula=input("Matricula:"),
        endereço=input("Endereço:")
    )
    lista_funcionarios.append(funcionario)
    print()

    os.system("cls || clear") 

    with open("dados_funcionarios.txt", "a") as arquivo:
        for funcionario in lista_funcionarios:
            arquivo.write(f"{funcionario.nome}, {funcionario.data_de_admissao}, {funcionario.matricula}, {funcionario.endereço}\n")
            

 

    


