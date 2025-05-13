import os
from dataclasses import dataclass
os.system("cls || clear")



@dataclass
class Livro:
    titulo: str
    autor: str
    categoria: str
    preço: float
    
Lista_livros = []
quantidade_Livro = 3

print("Informe os dados do livro")     
for i in range(quantidade_Livro,):
    
    dados_livro = Livro(
        titulo = input("Digite o titulo do livro: "),
        autor = input("Digite o nome do autor: "),
        categoria = input("Digite a categoria: "),
        preço = input("Digite o preço: ")  
    )
    Lista_livros.append(dados_livro)
    print()


os.system("cls || clear")

with open("dados_livros.txt", "a") as arquivo:
    for dados_livro in Lista_livros:
        arquivo.write(f" {dados_livro.titulo}, {dados_livro.autor}, {dados_livro.categoria} {dados_livro.preço} ") 


print("\n== Exibindo dados dos livros ==")
for dados_livro in Lista_livros:
    print(f"Titulo: {dados_livro.titulo}")
    print(f"Autor: {dados_livro.autor}")
    print(f"Categoria: {dados_livro.categoria}")
    print(f"Preço: {dados_livro.preço}")
    print()


print("\nSalvo com sucesso!")

print("== Exibindo dados dos livros ==")



