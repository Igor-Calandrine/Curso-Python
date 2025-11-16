# Verificar se o número é negativo ou zero usando not.

numero = input("Digite um número: \n")

if bool(numero) == True:
    numero_int = int(numero)

    if not (numero_int > 0) and not (numero_int == 0):
        print(f"Esse número ({numero_int}) é menor que zero")
    elif (not numero_int < 0 ) and (not numero_int == 0):
        print(f"Esse número ({numero_int}) é maior que zero")
    else:
        print(f"Esse número é o zero (0)")

else:
    print("Não há número a ser verificado")