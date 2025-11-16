# Verificar se o primeiro e último caracteres de uma string são iguais.

palavra = "oooojjjjffffoooo"

if palavra[0] == palavra[-1]:
    print(f"O 1º caractere ({palavra[0]}) é igual ao último caractere ({palavra[-1]}) da palavra '{palavra}'")
else:
    print("Os caracteres eles são diferentes")