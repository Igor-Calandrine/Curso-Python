"""Fatias: Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte:
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir os três últimos itens da lista."""

pizzas = ["Pepperoni", "Mussarela", "Frango", "Calabresa", "Catupiry"]

print(pizzas[:3])

print(f"Os 3 primeiros itens da lista são: {", ".join(pizzas[:3])}.")
print()
print(f"Os 3 itens da lista do meio são: {", ".join(pizzas[int((len(pizzas)/2) -1):int((len(pizzas)/2) +2)])}")
print()
print(f"Os 3 últimos itens da lista são: {", ".join(pizzas[-3:])}")
