# Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

num_input = input("Escreva um número inteiro: ")

try:
    num_int = int(num_input)
except ValueError:
    print("Não foi digitado um número")
    exit()

contador = 0

while contador < 10:
    if (num_int % 3 == 0):
        contador += 1
        print(f"{contador}º - {num_int}")
        
    num_int += 1
else:
    print("Fim do programa")
    exit()





    
