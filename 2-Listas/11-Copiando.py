"""
Copiando uma lista
   Para copiar uma lista, podemos criar uma fatia que inclua a lista original inteira omitindo o primeiro e o segundo índices ([:]). Isso diz a Python para criar uma lista que começa no primeiro item e termina no último, gerando uma cópia da lista toda."""

print("\tExemplo 1")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(my_foods)
print(friend_foods)

"""
   Para provar que realmente temos duas listas separadas, acrescentaremos um alimento em cada lista e mostraremos que cada lista mantém um registro apropriado das comidas favoritas de cada pessoa:"""

print("\n\tExemplo 2")

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)

"""
   Se tivéssemos simplesmente definido friend_foods como igual a my_foods, não teríamos gerado duas listas separadas. Em vez de armazenar uma cópia de my_foods em friend_foods, definimos que friend_foods é igual a my_foods. Essa sintaxe, na verdade, diz a Python para conectar a nova variável friend_foods à lista que já está em my_foods, de modo que, agora, as duas variáveis apontam para a mesma lista. """

print("\n\tExemplo 3")

my_drinks = ["water", "juice", "beer"]

friend_drinks = my_drinks
my_drinks.append("coke")

print(my_drinks)
print(friend_drinks)

"""
lista.copy()
   A função lista.copy() em Python é utilizada para criar uma cópia de uma lista, independente da original, copiando apenas os elementos de primeiro nível. Assim, alterações na lista copiada, como adicionar ou remover itens, não afetam a lista original.
   A principal vantagem de lista.copy() é a clareza e legibilidade do código, tornando explícita a intenção de criar uma cópia, sendo geralmente preferida em relação a técnicas como lista[:]."""

print("\n\tExemplo 4")

my_food41 = ["icecream", "pizza", "rice"]

my_food42 = my_food41.copy()
my_food42.append("beans")

print(my_food41)
print(my_food42)