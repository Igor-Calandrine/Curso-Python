"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

name = input("Digite seu nome: \n")
age = input("Digite sua idade: \n")

age_int = int(age)

if (bool(name) == True and bool(age) == True):
    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")
    
    if (" " in name):
        print("Seu nome há espaços")
    else:
        print("Não há espaços no seu nome")

    print(f"Seu nome tem tem {len(name)} letras")
    print(f"A primeiro letra do seu nome é {name[0]}")
    print(f"A última letra do seu nome é {name[-1]}")

else:
    print("Desculpe, há campos abertos")