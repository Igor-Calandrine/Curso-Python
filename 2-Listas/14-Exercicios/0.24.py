"""Números ímpares: Use o terceiro argumento da função range() para criar uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos os números."""

impares = list(range(1, 21, 2))

print(impares)

for impar in impares:
    print(impar, end=" ")

print()
impares_2 = [value for value in range(1, 21, 2)]
print(impares_2)