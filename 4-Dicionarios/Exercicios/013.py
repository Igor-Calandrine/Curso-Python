"""Escreva um programa que gere um dicionário, onde cada chave seja um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida. Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}"""

# frase = input("Digite uma frase para contarmos as letras: ")
frase = "O rato O rato"

letras = {}

for letra in frase.lower():
    if letra == " ":
        continue
    elif letra in letras:
        letras[letra] = letras[letra] + 1
    else:
        letras[letra] = 1

for letra, qnt in letras.items():
    print(f"{letra}: {qnt}")


