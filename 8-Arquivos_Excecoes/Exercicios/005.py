"""Enquete sobre programação: Escreva um laço while que pergunte às pessoas por que elas gostam de programação. Sempre que alguém fornecer um motivo, acrescente-o em um arquivo que armazene todas as respostas."""

def motivo_programar():
    while True:
        print("Escreva porque você gosta tanto de programação ou digite (0) para encerrar:")
        motivo = input("-->")

        if motivo != "0":
            arquivo = r"8-Arquivos_Excecoes\Exercicios\005.txt"

            with open(arquivo, "a", encoding="UTF-8") as objeto:
                objeto.write(f"\t{motivo}\n")
        else:
            break

def ler_arquivo():
    arquivo = r"8-Arquivos_Excecoes\Exercicios\005.txt"

    with open(arquivo) as objeto:
        conteudo = objeto.read()
        print(conteudo.rstrip())

motivo_programar()
ler_arquivo()