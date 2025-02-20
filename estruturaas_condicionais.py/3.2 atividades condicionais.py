import os

from sympy import resultant

os.system("clear")

# utilizando condicionais aninhadas.
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota)

print()
print(f"media: {media}")

if media < 7:
    print("Reprovado!")
else:
    print("aprovado!")

print(f"\nMedia:  {media}")
print(f"Resultado:  {resultant}")

