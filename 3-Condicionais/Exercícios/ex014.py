# Verificar se o número é divisível por 3 e por 5.

numero = float(input("Digite um número para saber se ele é difísil por 3 ou por 5: "))

div_3 = numero % 3
div_5 = numero % 5

if (div_3 == 0 and div_5 == 0):
    print(f"O número {numero} é divisível por 3 e por 5")
else:
    print(f"O número {numero} não é divisível por 3 e por 5")