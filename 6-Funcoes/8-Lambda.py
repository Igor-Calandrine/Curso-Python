"""
Funções Lambda
    Podemos criar funções simples, sem nome, chamadas de funções lambda, essa fução pode levar qualquer número de argumentos, mas só pode ter uma expressão."""

print("Exemplo 1")

resultado = lambda a, b:  a / b #a

print (resultado(10, 5)) #b

#a,
"""Observe que primeiro foi definida como uma função lambda e fornecido a sua quantidade de parâmetros para que seu resultado seja armazenado na variável."""
#b,
"""Assim como em #def, devemos fornecer os argumentos ordenados na mesma quantidade.

Lambida com fuções incorporadas
    As funções lambdas são comumentes usadas com funções internas como:
        *map() - aplica uma função a cada item de uam lista
        
        *filter() - cria uma lista de itens para os quais uma função retorna True
        
        *sorted() - criar uma chave de para classificação personalizada"""

print("\nExemplo 2.1")

numeros_21 = [1, 2, 3, 4, 5, 6]
dobrar = list(map(lambda x: x * 2, numeros_21))
print(dobrar)

print("\nExemplo 2.2")

numeros = [1, 2, 3, 4, 5, 6]
impares = list(filter(lambda x: x % 2 !=0, numeros))
print(impares)

print("\nExemplo 2.3")

estudantes = [("Emilly", 18), ("Andressa", 20), ("Igor", 17)]
sorted_estudantes = sorted(estudantes, key=lambda x: x[1])
print(sorted_estudantes)