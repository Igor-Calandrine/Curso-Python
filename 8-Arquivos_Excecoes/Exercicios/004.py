"""Lista de convidados: Escreva um laço while que pergunte o nome aos usuários. Quando fornecerem seus nomes, apresente uma saudação na tela e acrescente uma linha que registre a  visita do usuário em um arquivo chamado guest_book.txt. Certifique-se de que cada entrada  esteja em uma nova linha do arquivo."""

def nome_usuario ():
    n = 0
    while True:
        print("Bem vindo ao site AAA.AAAAAA.com.br")
        usuario = input("Digite o nome de usuário,\n\tOu digite (0)zero para fechar o programa:\n\t")
        n = n + 1

        if usuario != "0":
            print(f"Seja bem vindo usuário {usuario}")

            arquivo_004 = r"8-Arquivos_Excecoes\Exercicios\004.txt"
            
            with open(arquivo_004, "a") as objeto:
                objeto.write(f"Usuário {n}: {usuario}\n")
        else:
            break

def ler_arquivo ():
    arquivo_004 = r"8-Arquivos_Excecoes\Exercicios\004.txt"
    
    with open(arquivo_004) as objeto:
        conteudo = objeto.read()
        print(conteudo)

nome_usuario()
ler_arquivo()

