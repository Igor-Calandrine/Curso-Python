"""
Informações aninhadas
    Às vezes, você vai querer armazenar um conjunto de dicionários em uma lista  ou  uma  lista  de  itens  como  um  valor  em  um  dicionário.  Isso  é conhecido como aninhar informações. Podemos aninhar um conjunto de dicionários  em  uma  lista,  uma  lista  de  itens  em  um  dicionário  ou  até mesmo  um  dicionário  em  outro  dicionário. 

Uma lista de dicionários
    Como podemos administrar uma frota de alienígenas? Uma maneira é criar uma lista de alienígenas, em que cada  alienígena  seja  representado  por  um  dicionário  com  informações sobre  ele.  Por  exemplo,  o  código  a  seguir  cria  uma  lista  com  três alienígenas:"""

print("Exemplo 1")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

""" 
    No exemplo a seguir, usamos range() para criar uma frota de 10 alienígenas:"""

print("\nExemplo 2")
aliens = []

for alien_num in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print(aliens[:3])
print(f"Total de aliens: {len(aliens)}")

"""
    Como podemos trabalhar com um conjunto de alienígenas como esse? Suponha  que  um  aspecto  do  jogo  consista  em  fazer  alguns  alienígenas mudarem  de  cor  e  moverem-se  mais  rápido  à  medida  que  o  jogo prosseguir. Quando for o momento de mudar de cor, podemos usar um laço for e uma instrução if para alterar a cor dos alienígenas"""

print("\nExemplo 3")
for alien in aliens[:4]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens:
    print(alien)

"""
Uma lista em um dicionário
    Em vez de colocar um dicionário em uma lista, às vezes é conveniente colocar uma lista em um dicionário. Por  exemplo, considere como podemos descrever uma pizza que alguém está pedindo. Se usássemos apenas uma lista, tudo que poderíamos realmente armazenar é uma lista dos ingredientes da pizza. Com um dicionário, uma lista de ingredientes pode ser apenas um dos aspectos da pizza que estamos descrevendo"""

print("\nExemplo 4")
pizza = {
    "borda": "grossa",
    "acrescimos": ["cogumelos", "queijo extra"]
}

print(f"O pedido é de uma borda {pizza["borda"]}, e com acrescimo de: ")

for acrescimo in pizza["acrescimos"]:
    print(f"\t {acrescimo}")

"""
Um dicionário em um dicionário
    Podemos aninhar um dicionário em outro dicionário, mas o código poderá ficar complicado rapidamente se isso for feito. Por exemplo, se você tiver vários usuários em um site, cada um com um nome único, os nomes dos usuários poderão ser usados como chaves em um dicionário. Você poderá então armazenar informações sobre cada usuário usando um dicionário como o valor associado a cada nome de usuário."""

print("\nExemplo 5")
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
 
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for user, user_info in users.items():
    print(f"\nNome de usuário: {user}")
    nome_completo = user_info["first"] + " " + user_info["last"]
    localizacao = user_info["location"]
    print(f"\tNome completo: {nome_completo.title()}")
    print(f"\tLocalização: {localizacao.title()}")