"""Modifique o primeiro exemplo de forma a realizar a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de saída do while."""

L = [15,7,27,39]
p = int(input("Digite o valor a procurar:"))

x = 0
while x < len(L):
    if L[x] == p:
        break 
    x+=1

if L[x] == p:
    print("%d achado na posição %d" % (p,x))
else:
    print("%d não encontrado" % p)