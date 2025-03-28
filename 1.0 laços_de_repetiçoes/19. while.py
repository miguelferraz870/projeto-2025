import os 
import time
os.system("clear")


sexo = input("Digite seu sexo:")
idade = int(input("Digite sua idade"))
salario = float(input("Digite seu salario"))
contador = 0
menor_idade = 9999
maior_idade = 0
mulheres5k = 0
soma_salario = 0

while True:
    print("""
============== Menu =============    
\tCodigo     \tDescriçao
     1      | adicionar pessoa
     2      | exibir resultados   
     3      | sair
    """)
    
    opçao = int(input("DIgite sua opçao:"))    

    match opçao:
        case 1:
            salario = float(input("Digite seu salario:"))
            sexo = input("Informe seu sexo usando Ma para masculino ou Fe para feminino")
            idade = int(input("DIgite sua idade:"))
            contador += 1
            soma_salario += salario

            if idade > maior_idade:
                maior_idade = idade

            if idade < menor_idade:  
                menor_idade = idade  

            if sexo == "F" and salario >= 5000:
             mulheres5k += 1

            os.system("clear")
        case 2:
            if contador > 0:
                media_salario_grupo = soma_salario / contador
                print(f" A media de salario do grupo é:  {media_salario_grupo}")
                print(f" A maior idade do grupo é:  {maior_idade}")
                print(f" a menor idade do grupo é:  {menor_idade}")
                print(f" o numero de mulheres com salario maior que 5000 é: {mulheres5k}")
            else:
                0
                print("Nenhuma pessoa foi cadastrada.")
            
        case 3:
          time.sleep(2)
          os.system("clear")
          print("Saindo do programa...")       
        

        case _:
            print("Opçao invalida.")
            time.sleep(3)
            os.system("clear")