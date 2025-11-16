"""Gatos e cachorros: Crie dois arquivos, cats.txt e dogs.txt. Armazene pelo menos  três  nomes de gatos no primeiro arquivo e três nomes de cachorro no segundo arquivo. Escreva um  programa que tente ler esses arquivos e mostre o conteúdo do arquivo na tela. Coloque seu código em um bloco try-except para capturar o erro FileNotFound e apresente uma mensagem  simpática caso o arquivo não esteja presente. Mova um dos arquivos para um local diferente de seu sistema e garanta que o código no bloco except seja executado de forma apropriada."""

arquivo_list = [r"8-Arquivos_Excecoes\Exercicios\008.txt", r"8-Arquivos_Excecoes\Exercicios\008.txt", r"8-Arquivos_Excecoes\Exercicios\099.txt"]

def ler_conteudo(arquivo):
    try:
        with open(arquivo, encoding="UTF-8") as objeto:
            conteudo = objeto.read()
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado")
    else:
        print(conteudo)

for arquivo in arquivo_list:
    ler_conteudo(arquivo)
    print()
