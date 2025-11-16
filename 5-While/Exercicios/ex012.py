# Escreva um programa que pergunte o valor inicial de uma dívida e
# o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número
# de meses para que a dívida seja paga, o total pago e o total de juros pago.

divida = input("Digite o valor de sua dívida:\nR$")
juros_m = input("Digite o juros mensal(%):\n")
pagamento_m = input("Digite o valor pago mensalmente:\nR$")

juros_total = 0
meses_total = 0
total_pago = 0

try:
    divida_f = float(divida)
    juros_m_f = float(juros_m)
    pagamento_m_f = float(pagamento_m)
except:
    print("Não foi digitado um número")
    exit()

print(f"Dívida: R${divida_f}")
print(f"Pagamento Mensal: R${pagamento_m_f}")
print(f"Juros mensal: {juros_m_f}%")


while divida_f > 0:
    divida_f = divida_f + (divida_f * juros_m_f/100) - pagamento_m_f
    juros_total = juros_total + (divida_f * juros_m_f/100)
    total_pago = total_pago + pagamento_m_f
    meses_total = meses_total + 1

    print(f"Meses {meses_total} - Dívida:R${divida_f:.2f} - Juros total:{juros_total:.2f} - Pagamento total: {total_pago:.2f}")

    if (divida_f + (divida_f * juros_m_f/100) - pagamento_m_f) < 0:
        divida_f = divida_f + (divida_f * juros_m_f/100)
        juros_total = juros_total + (divida_f * juros_m_f/100)
        total_pago = total_pago + divida_f
        meses_total = meses_total + 1
        divida_f = divida_f - divida_f
        print(f"Meses {meses_total} - Dívida:R${divida_f:.2f} - Juros total:{juros_total:.2f} - Pagamento total: {total_pago:.2f}")
        break


