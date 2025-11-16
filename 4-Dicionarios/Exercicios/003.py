"""Glossário: Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo de glossário.
• Pense em cinco palavras relacionadas à programação que você conheceu nos capítulos  anteriores.  Use  essas  palavras  como  chaves  em  seu  glossário armazene seus significados como valores.
•  Mostre  cada  palavra  e  seu  significado  em  uma  saída  formatada  de  modo elegante.  Você  pode  exibir  a  palavra  seguida  de  dois-pontos  e  depois  o  seu significado, ou apresentar a palavra em uma linha e então exibir seu significado indentado em  uma  segunda linha.  Utilize  o caractere  de quebra  de  linha  (\n) para  inserir  uma  linha  em  branco  entre  cada  par  palavra-significado  em  sua saída."""

word = {
    "if": "se",
    "else": "então",
    "list": "lista",
    "int": "inteiro",
    "float": "flutuante",
    "str": "string",
}

print(f"O significado de if é:\n    {word["if"]}\n")
print(f"O significado de else é:\n    {word["else"]}\n")
print(f"O significado de list é:\n    {word["list"]}\n")
print(f"O significado de int é:\n    {word["int"]}\n")
print(f"O significado de float é:\n    {word["float"]}\n")
print(f"O significado de str é:\n    {word["str"]}\n")