"""Copiando uma lista

Para copiar uma lista, podemos criar uma fatia que inclua a lista original inteira omitindo o primeiro e o segundo índices ([:]). Isso diz a Python para criar uma lista que começa no primeiro item e termina no último, gerando uma cópia da lista toda."""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(my_foods)
print(friend_foods)

"""Para provar que realmente temos duas listas separadas, acrescentaremos um alimento em cada lista e mostraremos que cada lista mantém um registro apropriado das comidas favoritas de cada pessoa:"""

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)

"""Se tivéssemos simplesmente definido friend_foods como igual a my_foods, não teríamos gerado duas listas separadas. Em vez de armazenar uma cópia de my_foods em friend_foods, definimos que friend_foods é igual a my_foods. Essa sintaxe, na verdade, diz a Python para conectar a nova variável friend_foods à lista que já está em
my_foods, de modo que, agora, as duas variáveis apontam para a mesma lista. """

my_drinks =["water", "juice", "beer"]

friend_drinks = my_drinks
my_drinks.append("coke")

print(my_drinks)
print(friend_drinks)