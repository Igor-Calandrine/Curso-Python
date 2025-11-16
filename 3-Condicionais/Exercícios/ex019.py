# Verificar se uma senha tem pelo menos 8 caracteres.

senha = input("Digite uma senha com no mínimo 8 caracteres: ")

caracteres = len(senha)

if caracteres < 8:
    print("Sua senha não tem caracteres o suficiente")
else:
    print(f"Sua senha tem {caracteres} caracteres")