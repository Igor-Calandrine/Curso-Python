"""Estágios da vida: Escreva uma cadeia if-elif-else que determine oestágio da vida de uma pessoa. Defina um valor para a variável age e então:
• Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo que ela é um bebê.
• Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma mensagem dizendo que ela é uma criança.
• Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma mensagem dizendo que ela é um(a) garoto(a).
• Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma mensagem dizendo que ela é um(a) adolescente.
• Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma mensagem dizendo que ela é adulto.
• Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa pessoa é idoso.
"""

idade = int(input("Digite sua idade: "))

if 0 <= idade < 2:
    print("É um bebê")
elif 2 <= idade < 4:
    print("É uma criança")
elif 4 <= idade < 13:
    print("É um garoto")
elif 13 <= idade < 20:
    print("É um adolescente")
elif 20 <= idade < 65:
    print("É um adulto")
elif idade >= 65:
    print("É um idoso")
else:
    print("Idade inválida")