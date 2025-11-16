"""Ingredientes para uma pizza: Escreva um laço que peça ao usuário para fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja fornecido.  À  medida  que  cada  ingrediente  é  especificado,  apresente  uma mensagem informando que você acrescentará esse ingrediente à pizza."""

import os

ingredientes = ["queijo", "ovo", "presunto", "calabresa", "bacon"]
pedidos = []
ingrediente = ""

while True:
    os.system("cls")

    for ingrediente in ingredientes:
        if ingrediente == ingredientes[-1]:
            print(ingrediente, end=".")
            print()
        else:
            print(ingrediente, end=", ")
        

    prompt = "Digite os ingredientes para fazer sua pizza, ou 'quit' para encerrar."
    prompt = prompt + "\nIngredientes: "
    ingrediente = input(prompt)

    if ingrediente == "quit":
        break

    if ingrediente in ingredientes:
        pedidos.append(ingrediente)
        print(f"Ingrediente {ingrediente} adicionado.")
    else:
        print("Ingrediente não disponível.")

print(pedidos)

