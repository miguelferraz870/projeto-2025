import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Person:
    nome: str
    idade: int 
    Peso: float
    Altura: float

pessoa1 = Person("Lucas",30,50.0,1.75)
pessoa2 = Person("joao",25,50.0,1.75)    

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.Peso}, Altura: {pessoa1.Altura}\n")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}, Peso: {pessoa2.Peso}, Altura: {pessoa2.Altura}")
