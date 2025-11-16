# Escreva um programa que leia dois números. Imprima a divisão
# inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
# os operadores de soma e subtração para calcular o resultado. Lembre-se de que
# podemos entender o quociente da divisão de dois números como a quantidade
# de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez
# que podemos subtrair 4 cinco vezes de 20.

numero = input("Digite um número inteiro: \n")
divisor = input("Digite outro número para dividir: \n")

try:
    numero_int = int(numero)
    divisor_int = int(divisor)
except ValueError:
    print("Não foi digitado um número inteiro")
    exit()

i = 0
while numero_int > 0:
    numero_int = numero_int - divisor_int
    i += 1

    if ((numero_int - divisor_int) < 0):
        break

if (numero_int - divisor_int) < 0:
    print(f"Divide: {i} vezes")
    print(f"O resto: {numero_int}")





