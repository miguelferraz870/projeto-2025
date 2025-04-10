import os
os.system("clear")

lista = []

for i in range(3):
    nota = float(input("Digite a nota:"))
    lista.append(nota)

media = sum(lista) / 3

if media >= 7:
    print("Aprovado")
elif media < 5:
    print("Reprovado")
elif media >= 5 and media < 7:
    print("Recupereçao")
else:
   print("Nota invalida")

print()
for nota in lista:
    print(f"Nota: {nota}")   

print()
print(f"Media: {media}")    