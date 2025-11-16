"""Férias dos sonhos: Escreva um programa que faça uma enquete sobre as férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que
apresente os resultados da enquete."""

lugares = {"igor": "japão"}

nome = ""
lugar = ""

while True:
    nome = input("Digite o seu nome  ou (0)zero para encerrar a enquete.\n")
    
    if nome == "0":
        break

    lugar = input(f"{nome.title()}, se pudesse visitar um lugar do mundo, para onde você iria?\n\t")
    lugares[nome] = lugar
    
for nome, lugar in lugares.items():
    print(f"Nome: {nome.title()} - Local: {lugar.title()}")
