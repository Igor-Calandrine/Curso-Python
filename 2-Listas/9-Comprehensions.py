"""Uma list comprehension (abrangência de lista) permite gerar essa mesma lista com apenas uma linha de código. Uma list comprehension combina o laço for e a criação de novos elementos em uma linha, e concatena cada novo elemento automaticamente. As list comprehensions nem sempre são apresentadas aos iniciantes, mas eu as
incluí aqui porque é bem provável que você as veja assim que começar a analisar códigos de outras pessoas."""

squares = [value**2 for value in range(1,11)]
print(squares)