import os
os.system("clear")

lista_boletos = []
lista_pratos = []
lista_escolhas = []


while True:
    print("""
    ================= MENU =================
    1 \t Picanha \t\tR$ 25,00
    2 \t Lasanha \t\tR$ 20,00
    3 \t Strogonoff \t\tR$ 18,00
    4 \t Bife acebolado \tR$ 15,00
    5 \t Pão com ovo \t\tR$ 5,00
          """)
   
    opcao = int(input("Digite o número da opção desejada: "))  