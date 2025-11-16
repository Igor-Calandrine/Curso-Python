"""Lanchonete: Crie uma lista chamada sandwich_pedidos e a preencha com os nomes de vários sanduíches. Em  seguida,  crie uma lista vazia chamada sandwiches_finalizados. Percorra a lista de pedidos de sanduíches com um laço e mostre uma mensagem para cada pedido, por exemplo, Preparei seu sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem prontos, mostre uma mensagem que liste cada sanduíche preparado."""

sandubas = ["sanduba", "x-sanduba", "frango-sanduba"]
sandubas_pedido = []
sandubas_feito = []

pedido_ativo = True

while pedido_ativo:
    print("Escolha um dos sandubas abaixo ou (0)zero para finalizar o pedido.")

    for sanduba in sandubas:
        print(sanduba, end= " | ")

    sanduba_pedido = input("\nSanduba: ")

    if sanduba_pedido in sandubas:
        print(f"Pedido: {sanduba_pedido} sendo realizado.")
        sandubas_pedido.append(sanduba_pedido)
    elif sanduba_pedido == "0":
        pedido_ativo = False
    else:
        print("Esse sanduba não esta disponível.")

print(sandubas_pedido)

while sandubas_pedido:
    sanduba_feito = sandubas_pedido.pop()
    sandubas_feito.append(sanduba_feito)

print(sandubas_pedido)
print(sandubas_feito)

for sanduba_feito in sandubas_feito:
    print(f"Sanduba {sanduba_feito} preparado!")


