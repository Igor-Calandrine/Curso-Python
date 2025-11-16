"""Alterando a lista de convidados: Você acabou de saber que um de seus convidados não poderá comparecer ao jantar, portanto será necessário enviar um novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.

Comece com seu programa do Exercício 3.4. Acrescente uma instrução print no final de seu programa, especificando o nome do convidado que não poderá comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada
pessoa que continua presente em sua lista"""

convidados = ["Goku", "Samurai-X", "Neo", "Gohan", "Sasami"]

print(convidados)
print("O convidadeo Goku não poderá comparecer")
print("O convidadeo Gohan não poderá comparecer")

convidados[0] = "Vegeta"
convidados[-2] = "Trunks"
print(convidados)

for convidado in convidados:
    print(f"O Sr.(a) {convidado} está convidado para as Dunas do Infinito")