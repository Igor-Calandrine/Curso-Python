"""Verificando se um valor está em uma lista
Para descobrir se um valor em particular já está em uma lista, utilize a palavra reservada in. Vamos observar um código que você poderia escrever para uma pizzaria. Criaremos uma lista de ingredientes que um cliente pediu em sua pizza e, então, verificaremos se determinados ingredientes estão na lista."""

print("Exemplo 1")
ingredientes = ["queijo", "trigo", "frango", "cebola", "alho"]

print("queijo" in ingredientes)
print("requeijão" in ingredientes)

"""Verificando se um valor não está em uma lista
Em outras ocasiões, é importante saber se um valor não está em uma lista. Podemos usar a palavra reservada not nesse caso."""

print("Exemplo 2")
print("presunto" not in ingredientes)
print("trigo" not in ingredientes)

"""Verificando se uma lista não esta vazia
Dessa vez, começamos com uma lista vazia de ingredientes solicitados em u. Em vez de passar diretamente para um laço for, fazemos uma verificação rápida em v. Quando o nome de uma lista é usado em uma instrução if,
Python devolve True se a lista contiver pelo menos um item; uma lista vazia é avaliada como False. """

print("Exemplo 3")
requested_toppings = [] #u

if requested_toppings: #v
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

