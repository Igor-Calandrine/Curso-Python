# Altere o programa anterior de forma a perguntar também o valor
# depositado mensalmente. Esse valor será depositado no início de cada mês, e você
# deve considerá-lo para o cálculo de juros do mês seguinte.

deposito_inicial = input("Digite o depósito inicial: \nR$")
taxa_juros = input("Digite a taxa de juros: \n")
deposito_mensal = input("Digite a quantidade depositada mensalmente: \nR$")
meses = input("Digite a quantidade de meses \n")

try:
    deposito_inicial_i = float(deposito_inicial)
    taxa_juros_i = float(taxa_juros)
    deposito_mensal_i = float(deposito_mensal)
    meses_i = int(meses)
except ValueError:
    print("Não foi digitado um número")
    exit()

i = 1
while i <= meses_i:
    
    if i > 1:
        deposito_inicial_i = deposito_inicial_i + deposito_mensal_i
    
    deposito_inicial_i = deposito_inicial_i + (deposito_inicial_i * (taxa_juros_i/100))
    print(f"Mês {i} - Total: R${deposito_inicial_i:.2f}")
    i += 1