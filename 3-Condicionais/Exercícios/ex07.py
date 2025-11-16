# Verificar se uma letra é vogal.

letra = input("Digite uma letra para verificar se é vogal: \n")

if letra in "aeiou":
    print(f"A letra {letra} é uma consoante")
else:
    print(f"A letra {letra} não é uma vogal")

