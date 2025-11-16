# Verificar se uma palavra começa com uma vogal.

palavra = "Oportunidade"
palavra_low = palavra.lower()

vogal = input("Digite uma vogal: ")
vogal_lower = vogal.lower()


if bool(vogal) == True and (vogal_lower in "aeiou"):
    
    if vogal_lower == palavra_low[0]:
        print(f"A palavra {palavra} começa com a vogal ({vogal}) escolhida")
    else:
        print(f"A palavra {palavra} não começa com a vogal ({vogal}) escolhida")

else:
    print("Não há vogal para verificar")