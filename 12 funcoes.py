import os
os.system("clear")

produto_preco = float(input("Digite o preço do produto:"))

def inflacao():
    if produto_preco < 100:
        inflacao = produto_preco * 0.1

    else: 
        produto_preco > 100
        inflacionar = produto_preco * 1.20
    return inflacao

inflacionar = inflacao()

print(f"Preço do produto: {produto_preco}:.2f")
print(f"Preço do produto com a inflacao: {inflacionar}:.2f")
