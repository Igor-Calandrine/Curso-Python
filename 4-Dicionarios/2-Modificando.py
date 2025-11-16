"""Dicionário vazio
    Para começar a preencher um dicionário vazio, defina-o com um conjunto de chaves vazio e depois acrescente cada  par chave-valor em sua própria linha. Por exemplo, eis o modo de criar o dicionário alien_0 usando esta abordagem:"""

print("Exemplo 1")
alien_0 = {}

"""Adicionando novos pares chave-valor
    Dicionários são estruturas dinâmicas, e você pode adicionar novos pares chave-valor a um dicionário a qualquer  momento. Por exemplo, para acrescentar um novo par chave-valor, especifique o nome do dicionário, seguido da nova chave entre colchetes, juntamente com o novo valor."""

print("\nExemplo 2")
alien_0 = {'color': 'green', 'points': 5}

alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

"""Modificando valores em um dicionário
    Para  modificar  um  valor  em  um  dicionário,  especifique  o  nome  do dicionário  com  a  chave  entre  colchetes  e  o  novo  valor  que  você  quer associar a essa chave. Por exemplo, considere um alienígena que muda de verde para amarelo à medida que o jogo prossegue:"""

print("\nExemplo 3")
alien_0["color"] = "yellow"

print(alien_0)

"""Removendo pares chave-valor
    Quando não houver mais necessidade de uma informação armazenada em um dicionário, podemos usar a instrução del para remover totalmente um par chave-valor. Tudo de que del precisa é do nome do dicionário e da chave que você deseja remover.
    A linha em u diz a Python para apagar a chave 'points' do dicionário alien_0 e remover o valor associado a essa chave também. A saída mostra que a chave 'points' e seu valor igual a 5 foram apagados, porém o restante do dicionário não foi afetado."""

print("\nExemplo 4")
del alien_0["points"] #u

print(alien_0)

