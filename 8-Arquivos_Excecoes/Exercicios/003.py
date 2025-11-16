"""Convidado: Escreva um programa que pergunte o nome ao usuário. Quando ele responder, escreva o nome em um arquivo chamado guest.txt."""

def nome_usuario():
    nome = ""
    idade = ""

    nome = input("Escreve o nome do usuário:\n\t")
    idade = input("Escreva a idade do usuário:\n\t")

    return nome, idade

nome, idade = nome_usuario()

arquivo_003 = r"8-Arquivos_Excecoes\Exercicios\003.txt"

with open(arquivo_003, "a") as objeto:
    objeto.write(f"Nome: {nome}\n")
    objeto.write(f"Idade: {idade}\n")
    
with open(arquivo_003) as objeto:
    conteudo = objeto.read()
    print(conteudo)