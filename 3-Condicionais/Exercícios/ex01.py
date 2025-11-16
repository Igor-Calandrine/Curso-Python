# Verificar se um número é positivo ou negativo.

number = input("Digite um número: ")

number_int = int(number)

if number_int > 0:
    print(f"O número {number_int} é positivo")
elif number_int < 0:
    print(f"O número {number_int} é negativo")
else:
    print("O número é um vazio")