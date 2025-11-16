"""Listas

As listas permitem armazenar conjuntos de informações em um só lugar, independentemente de termos alguns itens ou milhões deles. 
Você pode colocar qualquer informação que quiser em uma lista, e os itens de sua lista não precisam estar relacionados de nenhum modo em particular. Como uma lista geralmente contém mais de um elemento, é uma boa ideia deixar seu nome no plural, por exemplo, letters, digits ou names.
Em Python, colchetes ([]) indicam uma lista, e elementos individuais da lista são separados por vírgulas. Eis um exemplo simples de uma lista que contém alguns tipos de bicicleta:"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

"""A posição dos índices começa em 0

Acessando elementos de uma lista Python considera que o primeiro item de uma lista está na posição 0, e não na posição 1. Isso é válido para a maioria das linguagens de programação, e o motivo tem a ver com o modo como as operações em lista são implementadas em um nível mais baixo. Se estiver recebendo resultados inesperados, verifique se você não está cometendo um erro simples de deslocamento de um."""

"""Acessando elementos de uma lista

Se você pode acessar qualquer elemento de uma lista informando a posição – ou índice – do item desejado ao interpretador Python. Para acessar um elemento de uma lista, escreva o nome da lista seguido do índice do item entre colchetes."""

print(bicycles[0])
print(bicycles[2])

"""Python tem uma sintaxe especial para acessar o último elemento de uma lista. Ao solicitar o item no índice -1, Python sempre devolve o último item da lista. Essa sintaxe é bem útil, pois, com frequência, você vai querer acessar os últimos itens de uma lista sem
saber exatamente o tamanho dela. Essa convenção também se estende a outros valores negativos de índice. O índice -2 devolve o segundo item a partir do final da lista, o índice -3 devolve o terceiro item a partir do final, e assim sucessivamente."""

print(bicycles[-1])

"""Também podemos usar os métodos de string em qualquer elemento de uma lista. Por exemplo, podemos formatar o elemento 'trek' de modo mais bonito usando o método title():"""

print(bicycles[0].title())
print(bicycles[1].upper())

