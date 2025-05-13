import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    autor: Autor
    ano_publicacao: int
    genero: str

    def exibir_dados(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor.nome}")
        print(f"Biografia: {self.autor.biografia}")
        print(f"Ano de Publicaçao: {self.ano_publicacao}")
        print(f"Genero: {self.genero}") 
        print()

artista = Autor("Artista", "Biografia do artista")
livro1 = Livro("Livro 1", artista, 2023, "Ficçao")
livro2 = Livro("Livro 2", artista, 2024, "Aventura")
livro1.exibir_dados()
livro2.exibir_dados()


 