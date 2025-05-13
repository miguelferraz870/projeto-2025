import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Person:
    nomer: str
    idade: int

pessoa1 = Person("Lucas",30)
pessoa2 = Person("joao",25)    

print(f"Nome: {pessoa1.nomer}, Idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nomer}, Idade: {pessoa2.idade}")

