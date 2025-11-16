"""Cidades:  Crie  um  dicionário  chamado  cities.  Use  os  nomes  de  três cidades como chaves em seu dicionário. Crie um dicionário com informações sobre cada  cidade  e  inclua  o  país  em  que  a  cidade  está  localizada,  a  população aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade devem ser algo como country, population e fact. Apresente o nome de cada cidade e todas as informações que você armazenou sobre ela"""

cities = {
    "belém": {
    "country": "brazil",
    "population": "200 mi",
    "fact": "corrupito",
    },
    "nagasak": {
        "country": "japão",
        "population": "124mi",
        "fact": "respeitoso",
    },
    "amsterdã": {
    "country":"holanda",
    "population": "80mi",
    "fact": "liberal",}
}

for citie, values in cities.items():
    print(citie.upper())
    for key, value in values.items():
        if key == "country":
            print(f"\t{key}: {value.title()}")
        else:
            print(f"\t{key}: {value}")
    print("")