"""Tuplas

As listas funcionam bem para armazenar conjuntos de itens que podem mudar durante a vida de um programa. A capacidade de modificar listas é particularmente importante quando trabalhamos com uma lista de usuários em um site ou com uma lista de personagens em um jogo. No entanto, às vezes, você vai querer criar uma lista de itens que não poderá mudar. As tuplas permitir fazer exatamente isso. Python refere-se a valores que não podem mudar como imutáveis, e uma lista imutável é chamada de tupla.

Uma tupla se parece exatamente com uma lista, exceto por usar parênteses no lugar de colchetes. Depois de definir uma tupla, podemos acessar elementos individuais usando o índice de cada item, como faríamos com uma lista."""

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

"""Vamos ver o que acontece se tentarmos alterar um dos itens da tupla dimensions:"""

dimensions[0] = 100 #u
print(dimensions)

"""O código em u tenta mudar o valor da primeira dimensão, mas Python devolve um erro de tipo. Basicamente, pelo fato de estarmos tentando alterar uma tupla, o que não pode ser feito para esse tipo de objeto. Isso é um ponto positivo, pois queremos que Python gere um erro se uma linha de código tentar alterar as dimensões do retângulo."""

"""Sobrescrevendo uma tupla

Embora não seja possível modificar uma tupla, podemos atribuir um novo valor a uma variável que armazena uma tupla. Portanto, se quiséssemos alterar nossas dimensões, poderíamos redefinir a tupla toda, Python não gera nenhum erro dessa vez, pois sobrescrever uma variável é uma operação válida"""

dimensions = (100, 25)
print(dimensions)

"""Podemos percorrer todos os valores de uma tupla usando um laço for, assim como fizemos com uma lista:"""

for dimension in dimensions:
    print(dimension)

