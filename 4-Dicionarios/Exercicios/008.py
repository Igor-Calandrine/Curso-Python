"""Animais de estimação: Crie vários dicionários, em que o nome de cada dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o tipo  do  animal  e  o  nome  do  dono.  Armazene  esses  dicionários  em  uma  lista chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer isso, apresente tudo que você sabe sobre cada animal de estimação"""

pet_1 = {"nome": "pudge", "tipo": "cachorro", "tamanho": "pequeno", "idade": "10"}
pet_2 = {"nome": "cookie", "tipo": "gato", "tamanho": "médio", "idade": "8"}
pet_3 = {"nome": "babi", "tipo": "peixe", "tamanho": "minúsculo", "idade": "1"}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for key, value in pet.items():
        if key == "nome":
            print(f"{key.upper()}: {value.title()} ")
        else:
            print(f"  {key}: {value}")
    print("")