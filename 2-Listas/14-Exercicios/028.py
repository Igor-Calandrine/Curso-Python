"""4.11 – Minhas pizzas, suas pizzas: Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte:
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja armazenada na lista apropriada."""

pizzas = ["Pepperoni", "Mussarela", "Frango", "Calabresa", "Catupiry"]
friend_pizzas = pizzas[:]

pizzas.append("Baicon")
friend_pizzas.append("Toscana")

print(pizzas)
print(friend_pizzas)

print(f"As minhas pizzas favoritas são: {", ".join(pizzas[:])}")
print(f"As minhas pizzas favoritas do meu amigo são: {", ".join(friend_pizzas[:])}")

for pizza in pizzas:
    print(f"Pizza Lista 1: {pizza}")

for friend_pizza in friend_pizzas:
    print(f"Pizza Lista 2: {friend_pizza}")