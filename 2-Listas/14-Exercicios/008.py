"""Imprima o menor elemento da lista."""

numeros = [numero for numero in range(5,16)]
minimo = numeros[0]

for numero in numeros:
    if numero < minimo:
        minimo = numero

print(minimo)
print(min(numeros))