# Verificar se um número é par ou ímpar.

numero = input("Digite um número para verificar se ele é par: \n")

numero_int = int(numero)

if numero_int % 2 == 0:
    print(f"O número {numero_int} é par")
else:
    print(f"O número {numero_int} é ímpar")
