"""Mais convidados: Você acabou de encontrar uma mesa de jantar maior, portanto agora tem mais espaço disponível. Pense em mais três convidados para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente uma instrução print no final de seu programa informando às pessoas que você encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista."""

convidados = ["Goku", "Samurai-X", "Neo", "Gohan", "Sasami"]

print("Será acrescentado mais 3 convidados: Vegeta, Trunks, Bulma")

convidados.insert(0, "Vegeta")
convidados.insert(int(len(convidados)/2), "Trunks")
convidados.append("Bulma")

for convidado in convidados:
    print(f"{convidado}, compareça a Estação 3/11 ás 5hrs da tarde")

print(convidados)