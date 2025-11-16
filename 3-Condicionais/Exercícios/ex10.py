# Verificar se um número não está entre 50 e 100.

número = int(input("Digite um número de 0 a 200:\n"))

if número < 50 or número > 100:
    print(f"O número {número} não está no intervalo de 50 á 100.")
else:
    print(f"O número {número} está no intervalo de 50 á 100.")