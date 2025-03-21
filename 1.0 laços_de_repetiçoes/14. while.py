import os 

os.system("clear") 

quantidade_notas = 2
soma = 0

for i in range(quantidade_notas):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota invalida, tente novamente. \n")
        else:
            soma += nota
            break    

media = soma / quantidade_notas

if media >= 7:
    resultado = "aprovado"
elif media >= 5:
    resultado = "Recuperaçao" 
else:
    resultado = "Reprovado."

print(f"\nMedia: {media}")
print(f"Resultado: {resultado}")           