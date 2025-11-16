"""Acrescentando elementos em uma lista

A maneira mais simples de acrescentar um novo elemento em uma lista é concatenar o item na lista. Quando concatenamos um item em uma lista, o novo elemento é acrescentado no final.
Criar listas dessa maneira é bem comum, pois, com frequência, você não conhecerá os dados que seus usuários querem armazenar em um programa até que ele esteja executando. Para deixar que seus usuários tenham o controle, comece definindo uma lista vazia que armazenará os valores dos usuários. Em seguida, concatene cada novo valor fornecido à lista que você acabou de criar."""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append("ducati")
print(motorcycles)

"""Inserindo elementos em uma lista

Você pode adicionar um novo elemento em qualquer posição de sua lista usando o método insert(). Faça isso especificando o índice do novo elemento e o valor do novo item."""

motorcycles.insert(0, "mercedes")
print(motorcycles)

"""O método extend sequer aceita parâmetros que não sejam listas. Se você utilizar o método append com uma lista como parâmetro, em vez de adicionar os elementos no fim da lista, append adicionará a lista inteira, mas como apenas um novo elemento, teremos então listas dentro de listas"""

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.extend(["ducati", "mercedes"])
print(motorcycles)
motorcycles.append(["ducati", "mercedes"])
print(motorcycles)

