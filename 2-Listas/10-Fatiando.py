"""Fatiando uma lista

Para criar uma fatia, especifique o índice do primeiro e do último elemento com os quais você quer trabalhar. Como ocorre na função range(), Python para em um item antes do segundo índice que você especificar. Para exibir
os três primeiros elementos de uma lista, solicite os índices de 0 a 3; os elementos 0, 1 e 2 serão devolvidos."""

print("Exemplo 1")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])

"""Você pode gerar qualquer subconjunto de uma lista. Por exemplo, se quiser o segundo, o terceiro e o quarto itens de uma lista, comece a fatia no índice 1 e termine no índice 4:"""

print("\nExemplo 2")
print(players[1:3])

"""Se o primeiro índice de uma fatia for omitido, Python começará sua fatia automaticamente no início da lista:"""

print("\nExemplo 3")
print(players[:4])

"""Uma sintaxe semelhante funcionará se você quiser uma fatia que inclua o final de uma lista. Por exemplo, se quiser todos os itens do terceiro até o último item, podemos começar com o índice 2 e omitir o segundo índice:"""

print("\nExemplo 4")
print(players[2:])

"""Esse código exibe os nomes dos três últimos jogadores e continuaria a funcionar à medida que a lista de jogadores mudar de tamanho."""

print("\nExemplo 5")
print(players[-3:])

"""Percorrendo uma fatia com um laço

Você pode usar uma fatia em um laço for se quiser percorrer um subconjunto de elementos de uma lista. No próximo exemplo, percorreremos os três primeiros jogadores e exibiremos seus nomes como parte de uma lista simples:"""

print("\nExemplo 6")
print("Temos os três primeiros jogadores aqui")
for player in players[:3]:
    print(player.title())