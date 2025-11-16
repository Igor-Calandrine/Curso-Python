"""Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será procurado. Na impressão, indique qual dos dois valores foi achado primeiro."""

L = [15,7,27,39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor: "))

x = 0
while x < len(L):
    if L[x] == p:
        break 
    x+=1

y = 0
while x < len(L):
    if L[y] == v:
        break 
    y+=1

if L[x] == p:
    print("%d achado na posição %d" % (p,x))
else:
    print("%d não encontrado" % p)

if L[y] == v:
    print("%d achado na posição %d" % (v,y))
else:
    print("%d não encontrado" % v)

if L[x] == p and L[y] == v:
    if x < y:
        print(f"O valor {p} foi encontrado primeiro")
    else:
        print(f"O valor {v} foi encontrado primeiro")



