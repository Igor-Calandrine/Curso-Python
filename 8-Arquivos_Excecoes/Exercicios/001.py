"""Aprendendo Python: Abra um arquivo em branco em seu editor de texto e escreva  algumas  linhas que sintetizem o que você aprendeu sobre Python até agora. Comece cada linha com a  expressão Em Python podemos.... Salve o arquivo como .txt no mesmo diretório em que estão seus exercícios deste  capítulo. Exiba o conteúdo uma vez lendo o arquivo todo, uma vez percorrendo o objeto arquivo com um laço e outra armazenando as linhas em uma lista e então trabalhando com ela fora do bloco with."""

print("1 - Lendo o arquivo")

arquivo = "8-Arquivos_Excecoes\Exercicios\\001.txt"

with open(arquivo, encoding="UTF-8") as objeto_arquivo_1:
    conteudo = objeto_arquivo_1.read()
    print(conteudo.rstrip())

print("\n2 - Percorrendo o objeto")

arquivo_2 = "8-Arquivos_Excecoes\Exercicios\\001.txt"

with open(arquivo_2, encoding="UTF-8") as objeto_arquivo_2:
    for line_2 in objeto_arquivo_2:
        print(line_2.rstrip())

print("\n3 - Lendo fora do bloco")

arquivo_3 = "8-Arquivos_Excecoes\Exercicios\\001.txt"

with open(arquivo_3, encoding="UTF-8") as objeto_arquivo_3:
    read_lines = objeto_arquivo_3.readlines()

conteudo_3 = ""
for line_3 in read_lines:
    conteudo_3 = conteudo_3 + line_3.rstrip()

print(conteudo_3.strip())