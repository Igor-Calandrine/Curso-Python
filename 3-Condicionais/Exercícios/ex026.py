"""Cores de alienígenas #2: Escolha uma cor para um alienígena, como foi feito no Exercício anterior, e escreva uma cadeia if-else.
• Se a cor do alienígena for verde, mostre uma frase informando que o jogador acabou de ganhar cinco pontos por atingir o alienígena.
• Se a cor do alienígena não for verde, mostre uma frase informando que o jogador acabou de ganhar dez pontos.
• Escreva uma versão desse programa que execute o bloco if e outro que execute o bloco else."""

alien_color = "green"

if alien_color == "green":
    print("5 pontos!")
else:
    print("10 pontos")

alien_color = "yellow"

if alien_color == "green":
    print("5 pontos!")
else:
    print("10 pontos")
