# Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...

num_input = input("Digite um número inteiro para saber sua tabuada: ")

try:
    num_int = int(num_input)
except ValueError:
    print("Não foi digitado um número inteiro.")
    exit()

i = 1
while i <= 10:
    print(f"{num_int} X {i} = {num_int * i}")
    i += 1
else:
    print("----")
    exit()





