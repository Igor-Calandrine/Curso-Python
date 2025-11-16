# Escreva um programa que pergunte o depósito inicial e a taxa de
# juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total ganho com juros no período.

deposito_inicial = input("Digite o depósito inicial \n R$")
taxa_juros = input("Digite a taxa de juros \n")
meses = input("Digite a quantidade de meses \n")

try:
    deposito_inicial_i = float(deposito_inicial)
    taxa_juros_i = float(taxa_juros)
    meses_i = int(meses)
except ValueError:
    print("Não foi digitado um número")
    exit()

i = 1
while i <= meses_i:
    deposito_inicial_i = deposito_inicial_i + (deposito_inicial_i * (taxa_juros_i/100))
    print(f"Mês {i} - Total: R${deposito_inicial_i:.2f}")
    i += 1
