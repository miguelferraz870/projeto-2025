import os
os.system("clear")

lista_de_compras = []
QUANTIDADE = 3


print("Digite os produtos que deseja comprar:")
for i in range(QUANTIDADE):
    item = input(f"Digite um item para lista de compras {i + 1}:")
    lista_de_compras.append(item)


print("\n= ITENS DA LISTA =")
for item in lista_de_compras:
    print(item)    