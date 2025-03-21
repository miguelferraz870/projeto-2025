import os 

os.system("clear")
soma = 0
contador = -0


while True:
        nota = float(input("Digite uma nota: "))
        soma += nota
        contador  += 1

  
        if nota < 0:
           break
        resposta = input("deseja digitar mais uma nota? \nResponda com 'S' ou 'N' :").lower()
        if resposta == "n":
            break

media = soma / contador

print()
print(f"\nQuantidade de notas informadas: {contador}")
print(f"\nMedia : {media}")        


