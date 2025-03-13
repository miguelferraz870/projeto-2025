import os 

os.system("clear") # limpa o terminal

dia = input("Digite dia de semana:")

match dia:
    case "segunda":
        print("hoje é segunda-feira.")
        print("dia util!")
    case "terça":
        print("hoje é terça-feira.")
        print("dia util!")
    case "quarta":
        print("hoje é quarta-feira.")
        print("dia util!")
    case "quinta":
        print("hoje é qunita-feira.")
        print("dia util!")
    case "sexta":
        print("hoje é sexta-feira.")
        print("dia util!")
    case "sabado" | "domingo":
        print("hoje é fim de semana!")
    case _:
        print("dia invalido.")




print("===== FIM =====")       

        
    
        





