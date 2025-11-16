# Verificar se o nome não está na lista de bloqueados.

L_bloquedos = ["João", "Maria", "Igor", "Cristina"]

name_input = input("Digite um nome para saber se ele está na lista de bloqueados: ")

if name_input in L_bloquedos:
    print(f"O nome {name_input} está na lista de bloqueados")
else:
    print(f"O nome {name_input} não está na lista de bloqueados")