"""
Percorrendo um dicionário com um laço
    Como um dicionário pode conter uma grande quantidade de dados, Python permite percorrer um dicionário com um laço. Dicionários podem ser usados para armazenar informações de várias maneiras, assim há diversos modos diferentes de percorrê-los com um laço. Podemos percorrer todos os pares chave-valor de um dicionário usando suas chaves ou seus valores.

Percorrendo todos os pares chave-valor com um laço
    Como vemos em u, para escrever um laço for para um dicionário, devemos criar nomes para as duas variáveis que armazenarão a chave e o valor de cada par chave-valor. Você pode escolher qualquer nome que quiser para essas duas variáveis. Esse código também funcionaria bem se usássemos abreviaturas para os nomes das variáveis:"""

print("Exemplo 1")
user_0 = {
    'username': 'user_fermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items(): #u
    print("\nKey: " + key) #v
    print("Value: " + value) #w

"""
    A segunda metade da instrução for em u inclui o nome do dicionário, seguido do método items(), que devolve uma lista de pares chave-valor, assim o laço for então armazena cada um desses pares nas duas variáveis especificadas. No exemplo anterior, usamos as variáveis para exibir cada chave (key) v, seguido do valor associado (value) w. Esses nomes descritivos fazem com que seja muito mais fácil ver o que a instrução print em m faz."""

print("\nExemplo 2")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items(): #m
    print(f"A linguagem favorita de {name.title()} é {language.title()}")

"""
Percorrendo todas as chaves de um dicionário com um laço
    O método keys() é conveniente quando não precisamos trabalhar com todos os valores de um dicionário. Vamos  percorrer o dicionário favorite_languages com um laço e exibir os nomes de todos que responderam à enquete:"""

print("\nExemplo 3")
for name in favorite_languages.keys():
    print(name.title())

"""
    O método keys() não serve apenas para laços: na verdade, ele devolve uma lista de todas as chaves, e a linha em u simplesmente verifica se 'erin' está nessa lista. Como ela não está, uma mensagem é exibida convidando-a a participar da enquete:"""

print("\nExemplo 4")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take it!")

"""
    Você pode optar por usar o método keys() explicitamente se isso deixar seu código mais fácil de ler, ou pode omiti-lo, se quiser. Percorrer  as  chaves,  na  verdade,  é  o  comportamento-padrão  quando percorremos um dicionário com um laço, portanto este código produzirá a mesma saída se escrevêssemos:"""

print("\nExemplo 5")
for name in favorite_languages:
    print(name.title())

"""
Percorrendo todos os valores de um dicionário com um laço
    Se você estiver mais interessado nos valores contidos em um dicionário, o método values() pode ser usado para devolver uma lista de valores sem as chaves"""

print("\nExemplo 6")
for language in sorted(favorite_languages.values()):
    print(language.title())

"""
    Essa abordagem extrai todos os valores do dicionário, sem verificar se há repetições.  Isso  pode  funcionar  bem com uma quantidade pequena de valores, mas em uma enquete com um número grande de entrevistados, o resultado seria uma lista com muitas repetições. Para ver cada linguagem escolhida sem repetições, podemos usar um conjunto (set)."""

print("\nExemplo 7")
for language in sorted(set(favorite_languages.values())):
    print(language.title())