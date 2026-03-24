'''
*---------------------------------------------------------------------------------------------------------------------------*
*                            Fatec São Cetano do Sul                                                                        *
*                                 Atividade B1-1                                                                            *
*  Autor: Ana Beatriz Gonçalves                                                                                             *
*  Objetivo: complete as lacunas (TODO) nas funções abaixo para que o sistema de catálogo de filmes funcione corretamente   *
*  data: 24/02/2026                                                                                                          *
*---------------------------------------------------------------------------------------------------------------------------*
'''

catalogo = {}

def adicionar_filme(id_filme, titulo, diretor):
    if id_filme in catalogo:
        print("ID já existente.")
        return
    catalogo[id_filme] = {
        "titulo": titulo,
        "diretor": diretor
    }
    print("Filme adicionado")

def buscar_filme(id_filme):
    filme = catalogo.get(id_filme)
    if not filme:
        print("Filme não encontrado.")
        return
    print("Filme encontrado:")
    print("Título:", filme["titulo"])
    print("Diretor:", filme["diretor"])

def remover_filme(id_filme):
    filme = catalogo.get(id_filme)
    if not filme:
        print("Filme não encontrado.")
        return
    catalogo.pop(id_filme)
    print("Filme removido")

def listar_todos():
    if not catalogo:
        print("O catálogo está vazio")
        return
    print(" Listagem de Filmes ")
    for id_f, dados in catalogo.items():
        print("ID:", id_f,
              "| Título:", dados["titulo"],
              "| Diretor:", dados["diretor"])

adicionar_filme(1, "As Patricinhas de Beverly Hills", "Amy Heckerling")
adicionar_filme(2, "Para Todos os Garotos que Já Amei", "Susan Johnson")

buscar_filme(1)
listar_todos()
remover_filme(1)
listar_todos()