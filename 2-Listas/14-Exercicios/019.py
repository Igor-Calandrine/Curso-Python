"""Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada pizza.
• Modifique seu laço for para mostrar uma frase usando o nome da pizza em vez de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha na saída contendo uma frase simples como Gosto de pizza de pepperoni.
• Acrescente uma linha no final de seu programa, fora do laço for, que informe quanto você gosta de pizza. A saída deve ser constituída de três ou mais linhas sobre os tipos de pizza que você gosta e de uma frase adicional, por exemplo, Eu realmente adoro pizza!"""

pizzas = ["Pepperoni", "Mussarela", "Frango", "Calabresa", "Catupiry"]

for pizza in pizzas:
    print(pizza)

print()

for x, pizza in enumerate(pizzas, 1):
    print(f"{x}º - Eu gosto da pizza de sabor {pizza}")

print()
print(f"Minha pizza preferida é {pizzas[-1]}")
print(f"Sempre que possível vou pedir {pizzas[0]}")
print(f"A pizza de {pizzas[1]} é simples e boa")
print(f"Sempre com os amigos eu vou pedir pizza de {pizzas[2]}")
print(f"A pizza de {pizzas[-2]} sempre me faz mal em excesso")