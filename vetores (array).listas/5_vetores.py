import os
os.system("clear")


listapar = []
listaimpar = []


def contar_pares_impares():
    
    pares = 0
    impares = 0


    for i in range(6):
        numero = int(input("Digite um numero:"))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
                

quantidade_pares, quantidade_impares = contar_pares_impares()

print(f"\nQuantidade de pares: {quantidade_pares}")
print(f"Quantidade de impares: {quantidade_impares}")                             
