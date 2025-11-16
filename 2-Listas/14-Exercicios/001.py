"""Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras."""

numbers_1 = list(range(1,11))
numbers_2 = [number for number in range(21,31)]
numbers_3 = []

print(numbers_1)
print(numbers_2)

for number_1 in numbers_1:
    numbers_3.append(number_1)

for number_2 in numbers_2:
    numbers_3.append(number_2)

print(numbers_3)
