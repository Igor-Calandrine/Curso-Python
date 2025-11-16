# Verificar se uma palavra está contida em uma frase.

frase = "O rato roeu o roupa do rei de Roma"

palavra = input("Digite uma palavra para procurar na frase: ")

if bool(palavra) == True:

    if palavra in frase:
        print("A palavra foi encontrada")
    else:
        print("A palavra não foi encontrada")

else:
    print("Não há palavra a ser procurada")