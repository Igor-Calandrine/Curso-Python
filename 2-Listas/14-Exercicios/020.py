"""Animais: Pense em pelo menos três animais diferentes que tenham uma característica em comum. Armazene os nomes desses animais em uma lista e, então, utilize um laço for para exibir o nome de cada animal.
• Modifique seu programa para exibir uma frase sobre cada animal, por exemplo,
Um cachorro seria um ótimo animal de estimação.
• Acrescente uma linha no final de seu programa informando o que esses animais têm em comum. Você poderia exibir uma frase como Qualquer um desses animais seria um ótimo animal de estimação!"""

animais = ["cachorro", "gato", "pato"]

for animal in animais:
    print(animal)

for animal in animais:
    print(f"Um {animal} seria um ótimo pet para eu ter em casa")

print(f"Todos os animais da lista, {animais[0]}, {animais[1]}, {animais[2]} são muito legais para se ter em casa")