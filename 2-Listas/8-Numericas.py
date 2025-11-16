"""Criando listas numéricas

As listas são ideais para armazenar conjuntos de números, e Python oferece várias ferramentas para ajudar você a trabalhar com listas de números de forma eficiente. Depois que souber usar efetivamente essas ferramentas, seu código funcionará bem, mesmo quando suas listas tiverem milhões de itens.

Usando a função range()

A função range() de Python facilita gerar uma série de números. Por exemplo, podemos usar a função range() para exibir uma sequência de números, assim:"""

for value in range(1,5):
    print(value)

"""Nesse exemplo, range() exibe apenas os números de 1 a 4. Esse é outro resultado do comportamento deslocado de um que veremos com frequência nas linguagens de programação. A função range() faz Python começar a contar no primeiro valor que você lhe fornecer e parar quando atingir o segundo valor especificado. Como ele para nesse segundo valor, a saída não conterá o valor final, que seria 5, nesse caso."""

"""Usando range() para criar uma lista de números

Se quiser criar uma lista de números, você pode converter os resultados de range() diretamente em uma lista usando a função list(). Quando colocamos list() em torno de uma chamada à função range(), a saída será uma lista de números."""

numbers = list(range(1,5))
print(numbers)

"""Nesse exemplo, a função range() começa com o valor 3 e então soma 2 a esse valor. O valor 2 é somado repetidamente até o valor final, que é 12, ser alcançado ou ultrapassado, e o resultado a seguir é gerado:"""

numbers_2 = list(range(3,12,2))
print(numbers_2)

"""Estatísticas simples com uma lista de números

Algumas funções Python são específicas para listas de números. Por exemplo, podemos encontrar facilmente o valor mínimo, o valor máximo e a soma de uma lista de números:"""

numbers_3 = list(range(0,11))
print(numbers_3)

print(max(numbers_3))
print(min(numbers_3))
print(sum(numbers_3))