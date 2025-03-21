import os 

os.system("clear") # limpa o terminal


while True < 10:
    nota_1 = float(input("Digite sua nota:"))
    nota_2 = float(input("Digite sua nota:"))
    media = (nota_1 + nota_2) / 2

    if media < 0 or media > 10:
        print("Nota invalida, tente novamente. \n")
    else:
        break

    print(f"Nota {nota_1}")
    print(f"Nota {nota_2}")
    print(f"Media {media}")    

    
    


