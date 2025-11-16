# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10

while True:
    num_input = input("Digite um número inteiro para saber sua tabuada. (0) Encerrar: \n")

    if num_input == "0":
        exit()
    i = input("Digite um número para inicicar os valores da tabuada. (0) Encerrar: \n")

    if i == "0":
        exit()

    try:
        num_int = int(num_input)
        i_int = int(i)
        break
    except ValueError:
        print("Não foi inserido um número inteiro")

while i_int <= 10:
    print(f"{num_int} x {i_int} = {num_int * i_int}")
    i_int += 1

else:
    print("Fim ------")
    exit()




