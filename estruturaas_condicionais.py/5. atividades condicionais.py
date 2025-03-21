import os 

os.system("clear") # limpa o terminal

# solicitando dados.

primeiro_numero = float(input("Digite a primeira nota: "))
segundo_numero = float(input("Digite a segunda nota: "))


media = () / 2
soma = (primeiro_numero + segundo_numero)
produto = (primeiro_numero * segundo_numero)
igual = (primeiro_numero == segundo_numero)




if primeiro_numero < segundo_numero:
    maior_numero = segundo_numero
    menor_numero = primeiro_numero


else:
    maior_numero = primeiro_numero
    menor_numero = segundo_numero




print()
print(f"Media: {media}")  
print(f"Soma: {soma}")  
print(f"Produto: {produto}")
print(f"Maior numero: {maior_numero}")
print(f"Menor numero: {menor_numero}")


if maior_numero == menor_numero:
    print("os numeros sao iguais")

else:
    print("os numeros nao sao iguais")   







