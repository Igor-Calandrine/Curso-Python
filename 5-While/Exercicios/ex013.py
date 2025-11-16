# Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução,
# exiba a quantidade de números digitados, assim como a soma e a média aritmética.

total = 0
quantidade = 0
numero = ""

while True:
    numero = input("Digite um número inteiro e (0) para sair do programa:\n")

    if not numero.isdigit():
        print(f"O valor digitado não é um inteiro positivo")
        break
    elif int(numero) == 0:
        print("Programa encerrado")
        break

    if int(numero) > 0:
        print(f"Número:{numero}")
        total = total + int(numero)
        quantidade = quantidade + 1
        media = total / quantidade

print("Menu ------")
print(f"Total: {total}")
print(f"Quantidade: {quantidade}")
if quantidade > 0:
    print(f"Média: {media:.2f}")

exit()

