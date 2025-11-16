"""Instruções if
Quando compreender os testes condicionais, você poderá começar a escrever instruções if. Há vários tipos de instruções if, e a escolha de qual deles usar dependerá do número de condições que devem ser testadas.

Instruções if simples
Você pode colocar qualquer teste condicional na primeira linha, e praticamente qualquer ação no bloco indentado após o teste. Se o teste condicional for avaliado como True, Python executará o código após a instrução if. Se o teste for avaliado como False, Python ignorará o código depois da instrução if.
"""
print("Exemplo 1")
age = 30 

if age > 20:
    print("Ele tem mais de 20 anos")

if age > 40:
    print("Ele tem mais de 40 anos")

"""Instruções if-else
Com frequência você vai querer executar uma ação quando um teste condicional passar, e uma ação diferente em todos os demais casos. A sintaxe if-else de Python torna isso possível. Um bloco if-else é semelhante a uma instrução if simples, porém a instrução else permite definir uma ação ou um conjunto de ações executado quando o teste condicional falhar

Se o teste condicional em passar, o primeiro bloco de instruções print indentadas u será executado. Se o teste for avaliado como False, o bloco else em v será executado. Como inscrito é menor que 18 dessa vez, o teste
condicional falha e o código do bloco else é executado:"""

print("Exemplo 2")

maioridade = 18
inscrito = 15

if inscrito >= 18: #u
    print("Você pode tirar a carteira de motorista")
else: #v
    print("Você não tem idade o suficiente para tirar a carteira de motorista")

"""Sintaxe if-elif-else
Muitas vezes, você precisará testar mais de duas situações possíveis; para avaliar isso, a sintaxe if-elif-else de Python poderá ser usada. Python executa apenas um bloco em uma cadeia if-elif-else. Cada teste condicional é executado em sequência, até que um deles passe. Quando um teste passar, o código após esse teste será executado e Python ignorará o restante dos testes."""

print("Exemplo 3")

cadeira = 15
preço = 0

if (1 <= cadeira <= 10):
    preço = 100
elif (11 <= cadeira <= 20):
    preço = 150
else:
    preço = 200

print(f"Seu valor é de R${preço:.2f}")

"""Omitindo o bloco else
Python não exige um bloco else no final de uma cadeia if-elif. Às vezes, um bloco else é útil; outras vezes, é mais claro usar uma instrução elif adicional que capture a condição específica de interesse.

O bloco else é uma instrução que captura tudo. Ela corresponde a qualquer condição não atendida por um teste if ou elif específicos e isso, às vezes, pode incluir dados inválidos ou até mesmo maliciosos. Se você tiver uma condição final específica para testar, considere usar um último bloco elif e omitir o bloco else. Como resultado, você terá mais confiança de que seu código executará somente nas condições corretas.
"""