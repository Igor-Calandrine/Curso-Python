"""f-strings - irão ajudar na formatação de strigs para inserir variáveis em textos
Inicia-se com 'f' e depois a string
A variavel fica entre {}"""
idade = 30
cor = "azul"
trocado = 3.3

print(f"A sua idade é de {idade} anos")
print(f"A cor é {cor}")
print(f"Seu troco é R${trocado:.2f}")

"""format - é uma outra maneira de fomatar strigns. As variáveis nas frases devem estar na mesma ordem"""

frase = "O suco de {} acabou {} vezes".format("laranja", 4)
print(frase)

"""Pode-se nomear por índices"""

frase1 = "Foram feitas {0} receitas de {1} no {2}".format(4, "comida", "restaurante")
print(frase1)

"""Pode-se utilizar variáveis no format"""

roupa = "nova"
valor = 50
quantidade = 4

print("A roupa é {}, seu valor é de R${:.2f}, foram {} unidades".format(roupa, valor, quantidade))

"""Pode-se nomear os parâmetros, mas uma vez feito, os demais seguintes tabém deverão ser nomeados"""
frase2 = "A roupa é {0}, seu valor é de R${name_b:.2f}, foram {name_c} unidades".format(roupa, name_b=valor, name_c=quantidade)
print(frase2)



