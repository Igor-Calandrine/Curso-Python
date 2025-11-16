"""Sem pastrami: Usando o exercícios anterior, garanta que o sanduíche de 'pastrami'  apareça  na lista pelo menos três vezes. Acrescente um código próximo ao início de seu programa para exibir  uma mensagem informando que a lanchonete está sem pastrami e, então, use um laço while para remover todas as ocorrências de  'pastrami' e sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em finished_sandwiches."""

sandubas = ["sanduba", "x-sanduba", "frango-sanduba", "pastrami"]
sandubas_pedido = ["pastrami", "pastrami", "pastrami"]
sandubas_feito = []
sandubas_falta = ["pastrami"]

pedido_ativo = True
sanduba_pedido = ""

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

while "pastrami" in sandubas_pedido:
    print("pastrami retirado do pedido")
    sandubas_pedido.remove("pastrami")

while sandubas_pedido:
    sanduba_feito = sandubas_pedido.pop()
    sandubas_feito.append(sanduba_feito)

print(sandubas_pedido)
print(sandubas_feito)

for sanduba_feito in sandubas_feito:
    print(f"Sanduba {sanduba_feito} preparado!")