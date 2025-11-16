"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_input = input("Digite um número inteiro: \n")

try:
    num_int = int(num_input)

    num_par = (num_int % 2 == 0)
    
    if (num_par):
        print(f"O número digitado ({num_int}) é par")
    else:
        print(f"O número digitado ({num_int}) é ímpar")
    
except:
    print("Valor digitado não é um número inteiro")

