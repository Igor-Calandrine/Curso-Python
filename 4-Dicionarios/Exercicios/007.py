"""Pessoas: Crie dois novos dicionários que representem pessoas diferentes e armazene os três dicionários em uma lista chamada people. Percorra sua lista de pessoas com um laço. À medida que percorrer a lista, apresente tudo que você sabe sobre cada pessoa"""

user_1 = {"nome": "alex", "cor": "pardo", "sexo": "masculino"}
user_2 = {"nome": "betina", "cor": "branca", "sexo": "feminino"}

users_list = [user_1, user_2]

for user_list in users_list:
    for key, value in user_list.items():
        if key == "nome":
            print(f"Nome: {user_list['nome'].title()}")
        else:
            print(f"\t{key}: {value}")


