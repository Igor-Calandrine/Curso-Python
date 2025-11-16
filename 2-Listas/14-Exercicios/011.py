"""Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas. O texto de cada mensagem deve ser o mesmo, porém cada mensagem deve estar personalizada com o nome da pessoa."""

amigos = ["Gustavo", "Rafael", "Victor", "Farias", "Jatene", "Eduardo"]


for x, amigo in enumerate(amigos, 1):
    print(f"{x}º - Bom dia, boa tarde e boa noite {amigo}")