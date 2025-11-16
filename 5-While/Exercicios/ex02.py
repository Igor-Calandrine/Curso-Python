# Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas dessa vez, apenas os números ímpares.


num_input = input("Digite um número inteiro positivo para contar pelos ímpares: ")

try:
    num_int = int(num_input)
except ValueError:
    print("Não é um número")
    exit()

contador = 1

while contador <= num_int:
   
    if (contador % 2 != 0):
        print(contador, "- Ímpar")
    
    contador += 1
else:
    print("Programa encerrado")

