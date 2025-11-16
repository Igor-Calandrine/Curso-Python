"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas_input = input("Digite a hora atual: \n")

try:
    horas_int = int(horas_input) 
    DIA = 0 <= horas_int <= 11
    TARDE = 12 <= horas_int <= 17
    NOITE = 18 <= horas_int <= 23

    if DIA:
        print("Bom dia!")
    elif TARDE:
        print("Boa tarde")
    elif NOITE:
        print("Boa noite")
    else:
        print("Não foi digitado um número no intervalo de 0 a 23 horas")
      
except:
    print("Não foi digitado um valor numérico inteiro no intervalo de 0 a 23 horas")