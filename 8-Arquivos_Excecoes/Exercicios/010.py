"""Palavras comuns: Acesse o Projeto Gutenberg (http://gutenberg.org/ ) e encontre alguns textos que você gostaria de analisar. Faça download dos arquivos-texto dessas obras ou copie o texto puro de seu navegador para um arquivo-texto em seu computador. Você pode usar o método count() para descobrir quantas vezes uma palavra ou expressão aparece em uma string. Observe que converter a string para letras minúsculas usando lower() faz com
que todas as formas da palavra que você está procurando sejam capturadas, independentemente do modo como elas estiverem grafadas. Escreva um programa que leia os arquivos que você  encontrou no Projeto Gutenberg e determine quantas vezes a palavra 'the' aparece em cada texto."""

arquivo = r"8-Arquivos_Excecoes\Exercicios\010.txt"
arquivo_a = r"8-Arquivos_Excecoes\Exercicios\010b.txt"

print("Teste com read()")

with open(arquivo, "w", encoding="UTF-8") as objeto:
    conteudo_r = objeto.write("Arquivo novo")

with open(arquivo, "r", encoding="UTF-8") as objeto:
    conteudo_r = objeto.read()
    print(conteudo_r)

with open (arquivo_a, "r", encoding="UTF-8") as objeto:
    conteudo_a = objeto.read()
    print(f"\nConteúdo arquivo 2:" )
    print(f"{conteudo_a}")

with open(arquivo, "a", encoding="UTF-8") as objeto:
    conteudo_r = objeto.write(f"\n{conteudo_a}")

with open(arquivo, "r", encoding="UTF-8") as objeto:
    conteudo_r = objeto.read()
    print(f"\nConteúdo total")
    print(conteudo_r)

# Exercício

arquivo_ex = r"8-Arquivos_Excecoes\Exercicios\010a.txt"

print("\nContagem de palavras")
with open(arquivo_ex, "r", encoding="UTF-8") as objeto:
    conteudo_ex = objeto.read()
    palavra = "past"
    quantidade = conteudo_ex.count(palavra)
    print(f"A palavra '{palavra}' foi encontrada {quantidade} vezes.")
    



# with open(arquivo, encoding="UTF-8") as objeto:
#     conteudo = objeto.read()
#     quantidade = conteudo.count("the")
#     print(quantidade)





