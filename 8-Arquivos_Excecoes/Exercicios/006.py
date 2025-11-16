"""Adição: Um problema comum quando pedir entradas numéricas ocorre quando as pessoas  fornecem texto no lugar de números. Ao tentar converter a entrada para um int, você obterá um TypeError. Escreva um programa que peça dois números ao usuário. Some-os e mostre o resultado. Capture o TypeError caso algum dos valores de entrada não seja um número e apresente uma mensagem de erro simpática. Teste seu programa fornecendo dois números e, em seguida, digite um texto no lugar de um número."""


def soma_numeros():
    numeros = []
    print("Soma de números")
    
    while True:
        a = input("Digite um números para somar \n\tou 'q' para ver o resultado da soma: ")
        
        try:
            if a == "q":
                break
            else:
                a_int = float(a)
        except ValueError:
            print("Não foi possível converter os dados para números, tente novamente.")
        else:
            numeros.append(a_int)
    
    soma = sum(numeros)
    msg = f"A soma dos números é {soma}"
    print(msg)

soma_numeros()