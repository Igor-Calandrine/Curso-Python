"""
    Com frequência, a programação envolve analisar um conjunto de condições e decidir qual ação deve ser executada de acordo com essas condições. A instrução if de Python permite analisar o estado atual de um programa e responder de forma apropriada a esse estado.

Testes condicionais
    No coração de cada instrução if está uma expressão que pode ser avaliada como True ou False, chamada de teste condicional. Python usa os valores True e False para decidir se o código em uma instrução if deve ser executado. Se um teste condicional for avaliado como True, Python executará o código após a instrução if. Se o teste for avaliado como False, o interpretador ignorará o código depois da instrução if."""

car = 'bmw' #u
car == 'bmw' #v

"""
    A linha em #u define o valor de car como 'bmw' usando um único sinal de igualdade, como já vimos muitas vezes. A linha em #v verifica se o valor de car é 'bmw' usando um sinal de igualdade duplo (==). Esse operador de igualdade devolve True se os valores dos lados esquerdo e direito do operador forem iguais, e False se forem diferentes."""

print("Exemplo 1")
print(car == "bmw")
print(car == "audi")

"""
Verificando a diferença
    Se quiser determinar se dois valores não são iguais, você poderá combinar um ponto de exclamação e um sinal de igualdade (!=). O ponto de exclamação representa não, como ocorre em muitas linguagens de programação."""

print("\nExemplo 2")
moto = "suzuki"
print(moto != "yamaha")
print(moto != "suzuki")

"""
Comparações numéricas
    Você pode incluir também várias comparações matemáticas em suas instruções condicionais, por exemplo, menor que (<), menor ou igual (<=) a, maior que (>) e maior ou igual a (>=)
"""

print("\nExemplo 3")
valor = 20
print(valor < 10)
print(valor > 10)
    

"""
Diferenças entre letras maiúsculas e minúsculas ao verificar a igualdade
    Testes de igualdade diferenciam letras maiúsculas de minúsculas em Python. Por exemplo, dois valores com diferenças apenas quanto a letras maiúsculas ou minúsculas não são considerados iguais."""

print("Exemplo 4")
carro = "Audi"
print(carro == "audi")

"""
    Esse teste deve devolver True, independentemente do modo como o valor 'Audi' estiver formatado, pois o teste agora ignora as diferenças entre letras maiúsculas e minúsculas. A função lower() não altera o valor originalmente armazenado em car, portanto você pode fazer esse tipo de comparação sem afetá-lo."""

print(carro.lower() == "audi")

"""
Expressões booleanas
    À medida que aprender mais sobre programação, você ouvirá o termo expressão booleana em algum momento. Uma expressão booleana é apenas outro nome para um teste condicional. Um valor booleano é True ou False, exatamente como o valor de uma expressão condicional após ter sido avaliada.
    Valores booleanos oferecem uma maneira eficiente para monitorar o estado ou uma condição em particular que seja importante para o seu programa."""

jogardor_ativo = True
funcionario_presente = False
