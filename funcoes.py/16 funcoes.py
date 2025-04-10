import os
os.system("clear")

altura = float(input("Digite a sua altura:"))
peso = float(input("Digite o seu peso:"))

def massa():
    imc = peso / (altura * altura)
    return imc

imc = massa()

def resultado(imc):
    if imc < 18.5:
        print("Abaixo do peso | consulte um nutricionista para orientaçao")
    elif imc >= 18.5 and imc < 24.9:
        print("Peso normal | Mantenha abitos saudaveis!")
    elif imc >= 25 and imc < 29.9:
        print("Sobrepes | considere que tu tem que fazer uma dieta bem rigida")
    elif imc >= 30 and imc < 34.9:
        print("Obsedidade grau 1 | procure um medico proficional pfv")
    elif imc >= 35 and imc < 39.9:
        print("Obesidade grau 2 | procure um medico antes que tu jogue no vasco")
    elif imc >= 40:
        print("Obesidade grau 3 | tu vai jogar no vasco")
        
print()
print(f"Seu IMC é: {imc}")


