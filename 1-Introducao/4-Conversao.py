"""Se por possível, pode-se converter um objeto para outro tipo imutável ou primitivo."""
print(11 + 11)
print("a" + "b")

"""Observe que o sinal '+' se comportou de maneiras diferentes dependendo do tipo de classe, isso se chama polimorfismo."""

#print("d" + 3)

"""Nesse caso temos um erro pois eles são do tipo diferentes, então iremos converter."""

print(int("30") + 90)
print(str(40) + "Ju")
print(float(30) + 90)

print(type(int("30")))
print(type(float("40")))
print(type(str(90)))