import os
from dataclasses import dataclass

os.system("cls || clear")


@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str
@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco
    email: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereço.logradouro}, numero {self.endereco.numero}")
        print(f"Email: {self.email}")

        

endereco1 = Endereco("Digite o seu endereco")
pessoa1 = Pessoa("Marta", 44, endereco1)
pessoa1.exibir_dados()

print()
endereco2 = Endereco("Digite o endereco da 2º pessoa")
pessoa2 = Pessoa("D")
pessoa2.exibir_dados()

