"""
Escreva seu nome na forma:
nova_string += '*L*u*i*z* *O*t*á*v*i*o'
"""


nome = input("Escreva o seu nome e (0) para encerrar o programa: \n")

if len(nome) == 0 or nome == "0":
    print("Não há algo escrito, tente novamente")
    exit()
elif nome == "0":
    print("Programa encerrado")
    exit()

nome_2 = ""

i = 0
while i < len(nome):
    nome_2 = nome_2 + ("*" + nome[i])
    i += 1

print(nome_2)




    
