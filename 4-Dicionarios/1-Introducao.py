"""Dicionários - Introduçao
    Entender os dicionários permite modelar uma diversidade de objetos do mundo real de modo mais preciso. Você será capaz de criar um dicionário que representa uma pessoa e armazenar quantas informações quiser sobre ela.  Poderá armazenar o nome, a idade, a localização, a profissão e qualquer outro aspecto de uma pessoa que possa ser descrito.

Trabalhando com dicionários
    Um dicionário em Python é uma coleção de pares chave-valor. Cada chave é conectada a um valor, e você pode usar uma chave para acessar o valor associado a ela. O valor de uma chave pode ser um número, uma string, uma lista ou até mesmo outro dicionário. De fato, podemos usar qualquer objeto que possa ser criado em Python como valor de um dicionário. Em Python, um dicionário é representado entre chaves, {}, com uma série de pares chave-valor entre elas.
    Um par chave-valor é um conjunto de valores associados um ao outro. Quando fornecemos uma chave, Python devolve o valor associado a essa chave. Toda chave é associada a seu valor por meio de dois-pontos, e pares chave-valor  individuais  são  separados  por  vírgulas.  Podemos  armazenar quantos pares chave-valor quisermos em um dicionário"""

print("Exemplo 1")
alien_0 = {'color': 'green', 'points': 5}

"""Acessando valores em um dicionário
    Para  obter  o  valor  associado  a  uma  chave,  especifique  o  nome  do dicionário e coloque a chave entre colchetes, como vemos a seguir:"""

print("Exemplo 2")
print(alien_0['color'])
print(alien_0['points'])

"""Um dicionário de objetos semelhantes
    Também podemos usar um dicionário para armazenar um tipo de informação sobre vários objetos. Por exemplo, suponha que você queira fazer uma enquete com várias pessoas e perguntar-lhes qual é a sua linguagem de programação favorita. Um dicionário é conveniente para armazenar os resultados de uma enquete simples, desta.
    Quando souber que precisará de mais de uma linha para definir um dicionário, tecle ENTER depois da chave de abertura. Em  seguida,  indente  a  próxima  linha  em  um  nível  (quatro  espaços)  e escreva o primeiro par chave-valor, seguido de uma vírgula.
    Depois  que  acabar  de  definir  o  dicionário,  acrescente  uma  chave  de fechamento em uma nova linha após o último par chave-valor e indente-a em um nível para que esteja alinhada com as chaves do dicionário. Incluir uma vírgula após o último par chave-valor também é uma boa prática, assim você estará preparado para acrescentar um novo par chave-valor na próxima linha."""

print("Exemplo 3")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
