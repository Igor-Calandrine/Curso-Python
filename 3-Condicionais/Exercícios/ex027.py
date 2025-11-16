"""Cores de alienígenas #3: Transforme sua cadeia if-else do anterior em uma cadeia if-elif-else.
• Se o alienígena for verde, mostre uma mensagem informando que o jogador ganhou cinco pontos.
• Se o alienígena for amarelo, mostre uma mensagem informando que o jogador ganhou dez pontos.
• Se o alienígena for vermelho, mostre uma mensagem informando que o jogador ganhou quinze pontos.
• Escreva três versões desse programa, garantindo que cada mensagem seja exibida para a cor apropriada do alienígena."""

aliens_color = ["green", "yellow", "red"]
pontos = 0

for alien_color in aliens_color:
    if alien_color == "green":
        pontos = 5
    elif alien_color == "yellow":
        pontos = 10
    else:
        pontos = 15
    print(f"{pontos} pontos!")
