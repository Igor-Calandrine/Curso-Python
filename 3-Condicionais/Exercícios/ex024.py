"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_input = input("Digite seu nome: ")

nome = nome_input.strip()

CURTO = 1 <= len(nome) <= 4
NORMAL = 5 <= len(nome) <= 6
GRANDE = len(nome) > 6

if CURTO:
    print(f"Seu nome tem {len(nome)} caracteres, é curto")
elif NORMAL:
    print(f"Seu nome tem {len(nome)} caracteres, é normal")
elif GRANDE:
    print(f"Seu nome é tem {len(nome)} caracteres, é grande")
else:
    print("Nada foi digitado")
