"""Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta."""

parenteses = []
controle_parenteses = []

entrada = input("Digite os parênteses: ")

for entrada_f in entrada:
    parenteses.append(entrada_f)
    
    if entrada_f == "(":
        controle_parenteses.append(entrada_f)

    if entrada_f == ")":
        if len(controle_parenteses) > 0:
            retirar = controle_parenteses.pop()
        else:
            controle_parenteses.append(entrada_f)
            break


if len(controle_parenteses) == 0:
    print(parenteses, "Ok")
    print(controle_parenteses)
else:
    print(parenteses, "Erro")



    



    






