# Verificar se uma lista não está vazia.

L = [1, 2, 3, 4, 5, 6, 7]
N = []

verificar = input("Digite para verificar de a lista L ou N esta vazia:\n")

if verificar == "L":
    if len(L) > 0:
        print(f"A lista não esta vazia")
        print(f"{L}")
    else:
        print(f"A lista esta vazia")
elif verificar == "N":
    if len(N) > 0:
        print(f"A lista não esta vazia")
        print(f"{N}")
    else:
        print(f"A lista esta vazia")
else:
    print(f"Não foi digitada uma lista válida")