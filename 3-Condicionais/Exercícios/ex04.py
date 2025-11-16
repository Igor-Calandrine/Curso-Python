# Verificar se um nome está na lista.

name_list = ["Maria", "João", "Igor", "Cristina"]

name_input = input("Difite um nome para procurar na lista:\n")

if name_input in name_list:
    print(f"O nome {name_input} está na lista")
else:
    print(f"O nome {name_input} não está na lista")
