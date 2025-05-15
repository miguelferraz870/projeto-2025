import os

import time

os.system("cls || clear")

def verificar_lista_vazia(lista_nomes):
    if not lista_nomes:
        print("\nA lista esta vazia.")
        return True
    return False

def adicionar(lista_nomes):
    nome = input("Digite o nome que deseja adicionar:")
    lista_nomes.append(nome)
    print(f"\n{nome} adicionado com sucesso.")


def mostrar(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return


    print("\nLista de nomes:")
    for nome in lista_nomes:
     print(f"- {nome}")

def atualizar(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return
    

    mostrar(lista_nomes)
    
    nome_antigo = input("\nDigite o nome que deseja atualizar:")
    if nome_antigo in lista_nomes:
     novo_nome = input(f"Digite o novo nome para {nome_antigo}:")
     indice = lista_nomes.index(nome_antigo)            
     lista_nomes[indice] = novo_nome
     print(f"\n{nome_antigo} foi atualizado para {novo_nome}")
    
    else:
     print(f"\nO nome {nome_antigo} nao foi encotrado.")
 


nomes = []


while True:
    print("= Gerenciador de nomes =\n")
    print("1. adicionar")
    print("2. listar nomes")
    print("3. atualizar")
    print("4. excluir")
    print("5. sair...\n")
    
    opcao = int(input("Escolha uma das opçoes acima:"))

    match opcao:
        case 1:
            adicionar(nomes)
        case 2:
            mostrar(nomes)
        case 3:
            atualizar(nomes)
        case 4:
            excluir(nomes)
        case 5: 
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpçao invalida. \nTente novamente.")

    if opcao != 1:
        time.sleep(5)
        os.sytem("cls || clear ")           
