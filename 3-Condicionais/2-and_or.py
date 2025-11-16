"""Testando várias condições
Pode ser que você queira testar várias condições ao mesmo tempo. Por exemplo, ocasionalmente, você pode precisar de duas condições True para executar uma ação. Em outros casos, poderia ficar satisfeito com apenas uma condição True. As palavras reservadas and e or podem ajudar nessas situações.

And
Para verificar se duas condições são True simultaneamente, utilize a palavra reservada and para combinar os dois testes condicionais; se cada um dos testes passar, a expressão como um todo será avaliada como True. Se um
dos testes falhar, ou ambos, a expressão será avaliada como False.

Para melhorar a legibilidade, podemos usar parênteses em torno dos testes individuais, mas eles não são obrigatórios."""

print("Exemplo 1")
age_1 = 18
age_2 = 23

print(age_1 >= 18 and age_2 >= 18)
print((age_1 >= 23) and (age_2 >= 23))

"""Or
A palavra reservada or permite verificar várias condições também, mas o teste passa se um dos testes individuais passar, ou ambos. Uma expressão or falha somente quando os dois testes individuais falharem."""

print("Exemplo 2")
print(age_1 > 20 or age_2 > 20)
print(age_1 > 30 or age_2 > 30)
