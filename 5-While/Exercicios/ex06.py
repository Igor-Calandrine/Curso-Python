# Escreva um programa que leia dois números. Imprima o resultado da
# multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
# subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
# + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

num_input = input("Digite um número inteiro: ")
try:
    num_int = int(num_input)
except ValueError:
    print("Não foi inserido um número inteiro")
    exit()

num_mult_input = input("Digite um número para multiplicar: ")
try:
    num_mult_int = int(num_mult_input)
except ValueError:
    print("Não foi inserido um número inteiro")
    exit()

resultado = 0
calculo = ""
i = 0

while i < num_mult_int:
    if num_mult_int == 0 or num_int == 0:
        print(f"{num_int} x {num_mult_int} = 0"  )
        print(resultado)
        break

    if i == (num_mult_int - 1):
        resultado += num_int
        calculo = calculo + (f"{num_input} = {resultado}")
        break

    i += 1
    resultado += num_int
    calculo = calculo + (f"{num_input} + ")
    
print(calculo)  
    


# i = 0
# while i != num_mult_int:
#     print(num_input + f"+ {num_int}")
    
# else:
#     print("Programa encerrado")



