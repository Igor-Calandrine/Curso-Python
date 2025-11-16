"""Enquete: Utilize o código em favorite_languages.
• Crie uma lista de pessoas que devam participar da enquete sobre linguagem favorita.  Inclua  alguns  nomes  que  já  estejam  no  dicionário  e  outros  que  não estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por responder. Se ainda não participaram da enquete, apresente uma mensagem convidando-as
a responder"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

persons_list = ["jen", "sarah", "igor", "yuri"]

for person in persons_list:
    if person in favorite_languages.keys():
        print(f"{person.title()}, obrigado por sua participação na enquete.")
    else:
        print(f"Por favor {person.title()}, participe de nossa enquete.")