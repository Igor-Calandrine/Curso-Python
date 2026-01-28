"""Ordenando uma lista temporariamente 

Para preservar a ordem original de uma lista, mas apresentá-la de forma ordenada, podemos usar a função sorted(). A função sorted() permite exibir sua lista em uma ordem em particular, mas não afeta a ordem propriamente dita da lista.
Observe que a lista preserva sua ordem original em x, depois que a função sorted() foi usada. Essa função também pode aceitar um argumento reverse=True se você quiser exibir uma lista em ordem alfabética inversa."""

print("\tExemplo 1")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(sorted(cars, reverse=True))
print(cars)

"""Temos também o método .sort(), que altera a lista e a coloca em ordem, aceita também o argumento reverse=True"""

print("\n\tExemplo 2")

numbers = [1,5,2,7,3,6]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

"""Ordenar uma lista em ordem alfabética é um pouco mais complicado quando todos os valores não utilizam letras minúsculas. Há várias maneiras de interpretar letras maiúsculas quando decidimos por uma sequência de
ordenação, e especificar a ordem exata pode apresentar um nível de complexidade maior que aquele com que queremos lidar no momento. No entanto, a maior parte das abordagens à ordenação terá diretamente como base o que aprendemos nesta seção."""

"""O método reverse() muda a ordem de uma lista de forma permanente, mas podemos restaurar a ordem original a qualquer momento aplicando reverse() à mesma lista uma segunda vez."""

print("\n\tExemplo 3")
cars.reverse()
print(cars)

"""
Embaralhando uma lista
Para embaralhar um lista com um método é necessário importar antes o módulo random para chamar seu método. Lembrando que é possível fazer sem um método."""

print("\n\tExemplo 4")

numeros4 = list(range(1,11))
print(numeros4)

import random

random.shuffle(numeros4)
print(numeros4)