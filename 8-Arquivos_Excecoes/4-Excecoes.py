"""
Exceções
    Python usa objetos especiais chamados exceções para adiministrar erros que surgirem durante a execução de um programa. Sempre que ocorrer um erro que faça Python não ter certeza do que deve fazer em seguida, um objeto exceção será criado. Se você escrever um código que trate a exceção, o programa continuará executando. 
    Se a exceção não for tratada, o programa será interrompido e um #traceback, que inclui uma informação sobre a exceção levantada será exibida.
    As exceções são tratadas como blocos try-except. Esse bloco pede que Python faça algo, mas também lhe diz que deve ser feito se uma exceção for levantada. Ao usar blocos try-except, seus programas continuarão a executar, mesmo que algo comece a dar errado. Em vez de #tracebacks, que podem ser confusos para os usuários lerem, os usuários verão mensagens de erro simpáticas escritas por você.
    
Tratando a ZeroDivisionError
    Vamos pedir que Python divida um número por zero, assim teremos um traceback ZeroDivisionError, um objeto exceção, criado em resposta a uma situação em que ele não é capaz de fazer, o programa então é interrompido"""

print("Exemplo 1")
a = 8
b = 0
# print(a/b) #para ver o traceback retire o comentário

"""
    Vamos usar o bloco try-except agora para tratar a exceção possível de ser levantada. Dizemos a Python para tentar executar um código e lhe dizemos o que ele deve fazer caso o código resulte em um tipo de exceção. Assim o programa continuará executando e o usuário receberá uma mensagem simpática sobre o que aconteceu."""

print("\nExemplo 2")
a = 15
b = 0

try:
    print(a/b)
except:
    print("Não é possível dividir por zero")

"""
Usando exceções para evitar falhas
    Tratar erros de forma correta é iportante, em especial quando o programa tiver outras atividades para fazer depois que o erro ocorrer. Isso acontece com frequência em programas que pedem dados de entrada as usuários. Se o programa responder a entradas inválidas de modo apropriado, ele poderá pedir mais entradas válidas em vez de causar uma falha.
    Usuários que não sejam técnicos ficarão confusos com eles, e em um ambiente malicioso, invasores aprenderão mais do que você quer que eles saibam a partir de um #traceback. Por exemplo, eles saberão o nome de seu arquivo de programa e verão uma parte de seu código que não está funcionando de forma propriada. Isso pode ser o suficiente para realizar um tipo de ataque que podem usar contra o seu código."""

"""
Bloco else
    Podemos deixar esse programa mais resistente a erros colocando a linha capaz de produzir erros em um bloco try-except, assim o erro pode ocorrer apenas na linhaa que calcula a divisão. Qualquer código que dependa do sucesso do bloco try é adicionado no bloco else. """

print("\nExemplo 3")
print("Me de 2 números e eu os dividirei!")
print("Ou aperte q para encerrar o programa")

while True:
    primeiro_numero = input("Digite o primeiro número: ")

    if primeiro_numero == "q":
        break
    
    segundo_numero = input("Digite o segundo número: ")

    try:
        resultado = int(primeiro_numero)/int(segundo_numero)
    except:
        print("Não é possível dividir por zero.")
    else:
        print(f"Resultado: {resultado}")

"""Tratando a exceção FileNotFound
    Um problema comum ao trabalhar com arquivos é o tratamento de arquivos ausentes. O arquivo que você está procurando pode estar em outro lugar, o nome do arquivo pode estar escrito de forma incorreta ou o arquivo talvez simplesmente não exista. Podemos tratar todas essas situações de um modo simples com um bloco try-except.
    Vamos tentar ler um arquivo que não existe."""

print("\nExemplo 4")

arquivo_4 = "exemplo_4.txt"

# with open(arquivo_4) as objeto:
#     conteudo = objeto.read()
#     print(conteudo)

"""A última linhas do traceback informa um FileNotFoundError, essa é a exceção criada por Python quando não encontra o arquivo que está tentando abrir. A função open() gera o erro, para tratá-lo o bloco try tem início imediatamente antes da linha que contém essa função."""

print("\nExemplo 5")

arquivo_5 = "exemplo_4.txt"

try:
    with open(arquivo_5) as objeto:
        conteudo = objeto.readline()
        print(conteudo)
except:
    print(f"Arquivo {arquivo_5} não existe")

"""
Analisando textos
    Podemos analisar arquivos-texto que contenham blocos inteiros. Muitas obras clássicas de literatura estão disponíveis como arquivos-texto simples, pois estão em domínio público.
    http://gutenberg.org/
    Vamos obter um texto e tentar contar o número de palavras do texto. Usaremos o método de string split(), que cria uma lista de palavras a partir de uma string."""

print("\nExemplo 6")

titulo = "Alice no país das Maravilha"
print(titulo.split())

print("\nExemplo 7")
arquivo_7 = r".\8-Arquivos_Excecoes\\4a-alice.txt"

try:
    with open(arquivo_7, encoding="UTF-8") as objeto:
        conteudo = objeto.read()
except:
    print("Arquivo não encontrado.")
else:
    palavras_lista = conteudo.split()
    palavras_quant = len(palavras_lista)
    print(f"O livro tem {palavras_quant} palavras.")

"""
Trabalhando com vários arquivos
    Vamos acrescentar outros livros para analisar. Porém, antes disso, vamos passar a parte principal desse programa para uma função chamada contar_palavras. Após isso iremos chamar essa função colocando como parâmetro o arquivo desejado, assim você poderá abrir quantos arquivos quiser."""

print("\nExemplo 8")

def contar_palavras(arquivo):
    """Conta a quantidade de palavras de um arquivo"""
    try:
        with open(arquivo, encoding="UTF-8") as objeto:
            conteudo = objeto.read()
    except FileNotFoundError:
        msg = f"Arquivo {arquivo} não existe"
        print(msg)
    else:
        palavras_lista = conteudo.split()
        palavras_quant = len(palavras_lista)
        print(f"O livro tem {palavras_quant} palavras.")

arquivo_8 = "8-Arquivos_Excecoes/4a-alice.txt"
contar_palavras(arquivo_8)

"""
    Agora iremos acrescentar mais arquivos e um que não existe no diretório para ver como será tratado. Utilizaremos um laço #for para analizar um arquivo de cada vez dentro da lista."""

print("\nExemplo 9")

arquivos = ["8-Arquivos_Excecoes/4a-alice.txt", "8-Arquivos_Excecoes/4a-moby.txt", "8-Arquivos_Excecoes/inexistente.txt"]

for arquivo in arquivos:
    contar_palavras(arquivo)

"""
Falhando silenciosamente
    No exemplo anterior, informamos nossos usuários que um dos arquivos estava disponível. Porém, não precisamos informar todas as exceções capturadas. Ás vezes queremos que o programa falhe silenciosamente e continue como se nada tivesse acontecido. Para fazer isso, escreva um bloco try-except como seria feito normalmente, mas diga de forma explícita para não fazer nada no bloco except com #pass.
    A instrução pass também atua como um marcador, é um lembrete de que você optou por não fazer nada em um ponto específico da execução de seu programa."""

print("\nExemplo 10")

def contar_palavras_10(arquivo):
    """Conta a quantidade de palavras de um arquivo"""
    try:
        with open(arquivo, encoding="UTF-8") as objeto:
            conteudo = objeto.read()
    except FileNotFoundError:
        pass
    else:
        palavras_lista = conteudo.split()
        palavras_quant = len(palavras_lista)
        print(f"O livro tem {palavras_quant} palavras.")

arquivos = ["8-Arquivos_Excecoes/4a-alice.txt", "8-Arquivos_Excecoes/4a-moby.txt", "8-Arquivos_Excecoes/inexistente.txt"]

for arquivo in arquivos:
    contar_palavras_10(arquivo)
