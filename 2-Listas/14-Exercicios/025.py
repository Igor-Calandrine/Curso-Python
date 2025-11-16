"""Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para exibir os números de sua lista."""

multiplos_3 = list(range(3, 31, 3))

for multiplo_3 in multiplos_3:
    print(multiplo_3, end=" ")

multiplos_3_2 = [value for value in range(3, 31, 3)]
print()
print(multiplos_3_2)