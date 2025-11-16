"""Glossário 2: Agora que você já sabe como percorrer um dicionário com um laço, limpe o código do Exercício 003, substituindo sua sequência de instruções print por um laço que percorra as chaves e os valores do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de Python ao seu glossário. Ao executar seu programa novamente, essas palavras e significados novos deverão ser automaticamente incluídos na saída"""

words = {
    "if": "se",
    "else": "então",
    "list": "lista",
    "int": "inteiro",
    "float": "flutuante",
    "str": "string",
}

for word, means in words.items():
    print(f"{word}:{means}")

words["dicionary"] = "dicionário"
words["items"] = "itens"
words["key"] = "chave" 
words["value"] = "valor"
words["print"] = "imprimir"

for word, means in sorted(words.items()):
    print(f"Plavra {word}: {means}")