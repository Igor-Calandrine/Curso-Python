"""Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em três nomes para usar como chaves do dicionário e armazene de um a três lugares favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante, peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o dicionário  com  um  laço  e  apresente  o  nome  de  cada  pessoa  e  seus  lugares favoritos."""

favorite_places = {
    "jatene": ["belém", "cotijuba", "icoaraci"], 
    "farias": ["belém", "manaus", "bragança"],
    "victor": ["belém", "salinas", "mosqueiro"]}

for name, places in favorite_places.items():
    print(name.title())
    print(f"Lugares favoritos:")
    for place in places:
        print(f"\t{place.title()}")
    print()