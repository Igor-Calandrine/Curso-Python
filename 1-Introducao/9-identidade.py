# id = identidade
# O Python aloca a identidade de variáveis de nomes diferentes mas de mesmo valor no meso ID

a1 = "A"
a2 = "A"
a3 = "B"


print(id(a1))
print(id(a2))
print(id(a3))

#is ou is not 
# São usados para comparar identidade de objetos, não o conteúdo.
# None é um valor especial que representa a ausência de um valor ou um valor nulo. Ele não é o mesmo que 0, uma string vazia (""), ou uma lista vazia ([]). None é um tipo de dado único, e existe apenas um objeto None no Python.

# Pense nele como um "nada" intencional.

a5 = True
b5 = False
c5 = None

print(f"Checando se as variáveis tem a mesma identidade: {a1 is a2}")

print(a5 is True)
print(b5 is False)
print(c5 is None)

print(a5 is not True)
print(b5 is not False)
print(c5 is not None)