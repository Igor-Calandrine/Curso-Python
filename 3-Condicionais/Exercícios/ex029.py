""" Fruta favorita: Faça uma lista de suas frutas favoritas e, então, escreva uma série de instruções if independentes que verifiquem se determinadas frutas estão em sua lista.
• Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.
• Escreva cinco instruções if. Cada instrução deve verificar se uma determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir uma frase, por exemplo, Você realmente gosta de bananas!"""

favorite_fruits = ["banana", "cupuaçu", "bacuri", "maça", "abacaxi"]

store_fruits = ["pera", "banana", "kwi", "morango", "maça"]

fruit = "banana"

for store_fruit in store_fruits:
    if store_fruit in favorite_fruits:
        print(f"Você realmente gosta de {store_fruit}")
    else:
        print(f"{store_fruit.title()} não é uma das suas favoritas")


