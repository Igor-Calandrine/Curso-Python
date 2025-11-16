"""Sua própria lista: Pense em seu meio de transporte preferido, como motocicleta ou carro, e crie uma lista que armazene vários exemplos. Utilize sua lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter uma moto Honda”."""

carros = ["Corola", "C3", "Cronos", "Basalt", "Pegeout 208", "HRV"]

print(f"O {carros[0]} é absurdamente caro")
print(f"O {carros[1]} é o meu carro do coração")
print(f"O {carros[2]} é muito top")
print(f"Quase eu tive um {carros[3]}")
print(f"O {carros[3]} é muito bonito")
print(f"O {carros[-1]} é um carro espaçoso")

for x, carro in enumerate(carros, 1):
    print(f"{x}º - Gostaria que o {carro} fosse bem mais barato")
