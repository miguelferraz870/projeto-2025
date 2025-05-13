import os
from dataclasses import dataclass

os.system("cls || clear")


@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereço.logradouro}, numero {self.endereco.numero}")


        

endereco1 = Endereco("Rua A, 23")
pessoa1 = Pessoa("Marta", 44, endereco1)
pessoa1.exibir_dados()

print()
endereco2 = Endereco("Rua B, 47")
pessoa2 = Pessoa("Maria" , 50,endereco2)
pessoa2.exibir_dados()

