"""Removendo elementos de uma lista

Se a posição do item que você quer remover de uma lista for conhecida, a instrução del poderá ser usada. Não podemos mais acessar o valor que foi removido da lista após a instrução del ter sido usada."""

motorcycles = ['mercedes', 'honda', 'yamaha', 'suzuki', 'ducati']
del motorcycles[-1]
print(motorcycles)

"""O método pop() remove o último item de uma lista, mas permite que você trabalhe com esse item depois da remoção.Você também pode usar pop() para remover um item de qualquer posição em uma lista se incluir o índice do item que você deseja remover entre parênteses."""

ultima_compra = motorcycles.pop()
primeiro_item_pop = motorcycles.pop(0)
print(ultima_compra.title())
print(primeiro_item_pop.title())

"""Às vezes, você são saberá a posição do valor que quer remover de uma lista. Se conhecer apenas o valor do item que deseja remover, o método remove() poderá ser usado.
O método remove() apaga apenas a primeira ocorrência do valor que você especificar. Se houver a possibilidade de o valor aparecer mais de uma vez na lista, será necessário usar um laço para determinar se todas as ocorrências valor foram removidas."""

motorcycles = ['mercedes', 'ducati', 'honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)