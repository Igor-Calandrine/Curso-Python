""" Verificando nomes de usuários: Faça o seguinte para criar um programa que simule o modo como os sites garantem que todos tenham um nome de usuário único.
• Crie uma lista chamada current_users com cinco ou mais nomes de usuários
• Crie outra lista chamada new_users com cinco nomes de usuários. Garanta que um ou dois dos novos usuários também estejam na lista current_users.
• Percorra a lista new_users com um laço para ver se cada novo nome de usuário já foi usado. Em caso afirmativo, mostre uma mensagem informando que a pessoa deverá fornecer um novo nome. Se um nome de usuário não foi usado,
apresente uma mensagem dizendo que o nome do usuário está disponível.
• Certifique-se de que sua comparação não levará em conta as diferenças entre letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá ser aceito"""

users_current = ["Igor", "Bianca", "Yuri", "Mário", "Cristina"]
users_new = ["IGOR", "BiancA", "joana", "BiancA", "Nataly", "Juliana" ]

user_disponível = True

for user_new in users_new:
    
    for user_current in users_current:
        if user_new.lower() == user_current.lower():
            user_disponível = False
            break
        else:
            user_disponível = True
    
    if user_disponível == True:
        users_current.append(user_new)
        print(f"Nome {user_new} disponível, suário adicionado")
    else:
        print(f"Nome de usuário indisponível, {user_new}")
        print("Tente outro nome")

print(users_current)







