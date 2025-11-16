"""Aprendendo C: Você pode usar o método replace() para substituir qualquer palavra por uma palavra diferente em uma string. Eis um exemplo rápido que mostra como substituir a palavra 'dog' por 'cat' em uma frase:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Leia cada linha do arquivo learning_python.txt que você acabou de criar e substitua a palavra Python pelo nome de outra linguagem, por exemplo, C. Mostre cada linha modificada na tela."""

arquivo = "8-Arquivos_Excecoes\Exercicios\\001.txt"

with open(arquivo, encoding="UTF-8") as objeto_arquivo:
    conteudo = objeto_arquivo.readlines()

for lines in conteudo:
    print(lines)

texto = ""
for line in conteudo:
    texto = texto + line

print()
print(texto.replace("Harry Potter", "Luke Skywalker"))
    
