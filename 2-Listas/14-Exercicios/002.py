"""Faça um programa que percorra duas listas e gere uma terceira sem
elementos repetidos."""

numbers_1 = list(range(1,11))
numbers_2 = [number for number in range(5,11)]
numbers_3 = [2]

for number_1 in numbers_1:
    if number_1 not in numbers_3:
        numbers_3.append(number_1)

for number_2 in numbers_2:
    if number_2 not in numbers_3:
        numbers_3.append(number_2)

print(numbers_3)