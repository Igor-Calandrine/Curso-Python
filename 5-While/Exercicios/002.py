"""Ingressos  para  o  cinema: Um  cinema  cobra  preços  diferentes  para  os ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3 anos de idade, o ingresso será gratuito, se tiver entre 3 e 12 anos, o ingresso custará  10  dólares, se  tiver  mais  de  12  anos, o  ingresso  custará  15  dólares. Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o preço do ingresso do cinema."""
import os

ingresso_2 = 0
ingresso_3_12 = 10
ingresso_13 = 15

prompt = "Digite a idade para adquirir a entrada do cinema ou (0)zero para encerrar.\nIdade: "
idade = ""

while True:
    idade = int(input(prompt))
    os.system("cls")
    
    if idade == 0:
        break

    if 1 <= idade < 3:
        print("Entrada grátis")
        print(f"R${ingresso_2},00")
    elif 3 <= idade <= 12:
        print(f"R${ingresso_3_12},00")
    elif idade >= 13:
        print(f"R${ingresso_13},00")
    else:
        continue

