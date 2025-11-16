# Verificar se a letra digitada é maiúscula.
letra = input("Digite uma letra:\n")

letra_maiuscula = letra.upper()

if letra == letra_maiuscula:
    print(f"A letra {letra} é maiúscula")
else:
    print(f"A letra é minúscula")