"""Números favoritos: Modifique o seu programa do Exercício para que cada pessoa possa ter mais de um número favorito. Em seguida, apresente o nome de cada pessoa, juntamente com seus números favoritos"""

favorite_numbers = {
    "igor": [73, 25, 78, 99],
    "bianca": [54, 21, 76, 4],
    "yuri": [14, 32, 65, 16, 78],
    "cristina": {18, 78, 45, 15},
    "mario": [23, 45, 87, 81],
}

for name, numbers in favorite_numbers.items():
    print(name.title())
    print(f"Números favoritos: ", end="")
    for number in numbers:
        print(number, end=" ")
    print("\n")
