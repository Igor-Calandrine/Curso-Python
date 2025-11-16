"""Ordenando uma lista temporariamente 

Para preservar a ordem original de uma lista, mas apresentá-la de forma ordenada, podemos usar a função sorted(). A função sorted() permite exibir sua lista em uma ordem em particular, mas não afeta a ordem propriamente dita da lista.
Observe que a lista preserva sua ordem original em x, depois que a função sorted() foi usada. Essa função também pode aceitar um argumento reverse=True se você quiser exibir uma lista em ordem alfabética inversa."""

print("Exemplo 1")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(sorted(cars, reverse=True))
print(cars)

"""Temos também o método .sort(), que altera a lista e a coloca em ordem, aceita também o argumento reverse=True"""

print("\nExemplo 2")
numbers = [1,5,2,7,3,6]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

"""Ordenar uma lista em ordem alfabética é um pouco mais complicado quando todos os valores não utilizam letras minúsculas. Há várias maneiras de interpretar letras maiúsculas quando decidimos por uma sequência de
ordenação, e especificar a ordem exata pode apresentar um nível de complexidade maior que aquele com que queremos lidar no momento. No entanto, a maior parte das abordagens à ordenação terá diretamente como base o que aprendemos nesta seção."""

"""O método reverse() muda a ordem de uma lista de forma permanente, mas podemos restaurar a ordem original a qualquer momento aplicando reverse() à mesma lista uma segunda vez."""

print("\nExemplo 3")
cars.reverse()
print(cars)