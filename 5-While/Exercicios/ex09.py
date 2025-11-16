# Escreva um programa para que aceite respostas com letras maiúsculas e minúsculas em todas as questões
# e faça a contagem de acertos.

resposta_1 = "a"
resposta_2 = "a"
resposta_3 = "a"
resposta_4 = "a"
resposta_5 = "a"

resposta = ""

acertos = 0
questao = 1

while questao <= 5: 
    resposta = input(f'Questão {questao} - Digite a alternativa correta: ')

    if questao == 1 and resposta.lower() == resposta_1:
        acertos = acertos + 1
    if questao == 2 and resposta.lower() == resposta_2:
        acertos = acertos + 1
    if questao == 3 and resposta.lower() == resposta_3:
        acertos = acertos + 1
    if questao == 4 and resposta.lower() == resposta_4:
        acertos = acertos + 1
    if questao == 5 and resposta.lower() == resposta_5:
        acertos = acertos + 1

    questao += 1

print(f"Acertos: {acertos}")
