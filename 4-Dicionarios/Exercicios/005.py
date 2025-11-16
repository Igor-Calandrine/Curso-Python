"""Rios: Crie  um  dicionário que contenha três rios importantes e o país que cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário."""

rios = {
    "nilo": "egito",
    "amazonas": "brazil",
    "shinano": "japão",
    }

for rio, paiz in sorted(rios.items()):
    print(f"O Rio {rio.title()} corre pelo {paiz.title()}")

for paiz in sorted(rios.values()):
    print(f"Paíz: {paiz.title()}")

for rio in sorted(rios.keys()):
    print(f"Rio {rio.title()}")

