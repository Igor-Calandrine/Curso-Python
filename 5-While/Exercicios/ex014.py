# Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

import os 

preço_1 = 0.5 
preço_2 = 1
preço_3 = 4
preço_4 = 7
preço_5 = 8

preço_total = 0

id = 0
qntd = 0

while True:
    
    os.system("cls")
    id = int(input("Digite o código do produto || (0) para encerrar compras: \n"))
    
    if id == 0:
        break
    elif id == 1:
        print(f"Preço unid: R${preço_1}")
        qntd = int(input("Digite a quantidade de produtos: "))
        preço_total = preço_total + preço_1 * qntd
        print(f"Total R${preço_1 * qntd}.......R${preço_1} x {qntd}")
        input("Enter para continuar")
    elif id == 2:
        print(f"Preço unid: R${preço_2}")
        qntd = int(input("Digite a quantidade de produtos: "))
        preço_total = preço_total + preço_2 * qntd
        print(f"Total R${preço_2 * qntd}.......R${preço_2} x {qntd}")
        input("Enter para continuar")
    elif id == 3:
        print(f"Preço unid: R${preço_3}")
        qntd = int(input("Digite a quantidade de produtos: "))
        preço_total = preço_total + preço_3 * qntd
        print(f"Total R${preço_3 * qntd}.......R${preço_3} x {qntd}")
        input("Enter para continuar")
    elif id == 4:
        print(f"Preço unid: R${preço_4}")
        qntd = int(input("Digite a quantidade de produtos: "))
        preço_total = preço_total + preço_4 * qntd
        print(f"Total R${preço_4 * qntd}.......R${preço_4} x {qntd}")
        input("Enter para continuar")
    elif id == 5:
        print(f"Preço unid: R${preço_5}")
        qntd = int(input("Digite a quantidade de produtos: "))
        preço_total = preço_total + preço_5 * qntd
        print(f"Total R${preço_5 * qntd}.......R${preço_5} x {qntd}")
        input("Enter para continuar")
    else:
        print("Código inválido")
        input("Enter para continuar")

print(f"Total: R${preço_total}")


