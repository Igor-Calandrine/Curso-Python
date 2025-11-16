"""10.9 – Gatos e cachorros silenciosos: Modifique o seu bloco except do Exercício
10.8 para falhar silenciosamente caso um dos arquivos esteja ausente"""

arquivo_list = [r"8-Arquivos_Excecoes\Exercicios\008.txt", r"8-Arquivos_Excecoes\Exercicios\008.txt", r"8-Arquivos_Excecoes\Exercicios\099.txt"]

def ler_conteudo(arquivo):
    try:
        with open(arquivo, encoding="UTF-8") as objeto:
            conteudo = objeto.read()
    except FileNotFoundError:
        pass
    else:
        print(conteudo)

for n ,arquivo in enumerate(arquivo_list, 1):
    print(f"{n}º Arquivo")
    ler_conteudo(arquivo.strip())
    print()