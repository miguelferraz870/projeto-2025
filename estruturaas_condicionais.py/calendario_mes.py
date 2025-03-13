import os 

os.system("clear") # limpa o terminal


print("""
========== calendario ==========
Codigo  \tdia da semana
         
1   \t\tjaneiro
2   \t\tfeveiro
3   \t\tmarço
4   \t\tabril
5   \t\tmaio
6   \t\tjunho
7   \t\tjulho
8   \t\tagosto
9   \t\tsetembro
10  \t\toutubro
11  \t\tnovembro
12  \t\tdezembro
      

""")

dia = input("Digite um numero para um mes do ano:")

match dia:
    case 1 | 12:
        resultado = "Fim de semana."
    case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
        resultado = "Dia util."
    case _:
        resultado = "Opçao invalida"   


print()
print(f"Resultado: {resultado}")             