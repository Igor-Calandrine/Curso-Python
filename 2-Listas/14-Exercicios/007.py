"""do for. Explique por que nem todos os while podem ser transformados em for."""
"""L=[]

while True:
    n=int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)

x=0
while x < len(L):
    print(L[x])
    x=x+1"""

numeros = []

while True:
    n=int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    numeros.append(n)

for numero in numeros:
    print(numero)
