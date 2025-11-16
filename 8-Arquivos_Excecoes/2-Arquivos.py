"""
Lendo um arquivo inteiro
    Para começar, vamos aprender a ler um arquivo. Primeiro crie um arquivo no diretório. Usarei de exemplo 2-Arquivos.txt 

open()
    A função open() inicialmente abri o arquivo para acessá-lo. Essa função precisa de um argumento, claramente será o nome do arquivo que você quer abrir. Python procura esse arquivo no diretório em que o programa esta executando e devolve um objeto que representa o arquivo, nesse caso o objeto será #arquivo_objeto.
    
with
    A palavra reservada #with fecha o arquivo depois que não for mais necessário acessá-lo. Observe como chamammos open() nesse programa mas não o close(). Você poderia abrir e fechar o arquivo, mas se um bug em seu programa impedir que a instrução close() seja executada, o arquivo não será fechado. Isso pode parecer trivial, mas arquivos indevidamente fechados podem provocar perda de dados ou estes podem ser corrompidos.
    Nem sempre é fácil saber exatamente quando devemos fechar um arquivo, mas com a estrutura mostrada aqui, Python descobrirá isso para você.
    
read()
    Depois que tivermos um objeto arquivo que represente 2-Arquivos.txt, usamos o método read() na segunda linha de nosso programa para ler todo o conteúdo do arquivo e armazená-lo em uma longa string em #conteudo."""

print("Exemplo 1")

with open("8-Arquivos_Excecoes/2-Exemplo_1.txt") as objeto_arquivo:
    conteudo = objeto_arquivo.read()
    print(conteudo)

"""
    A única diferença entre essa saída e o arquivo original é a linhas em branco extra no final da saída. A linha em branco aparece porque read() devolve uma string vazia quando alcança o final do arquivo. Se quiser remover essa linhas em branco extra, a função rstrip() pode ser usada na instrução print."""

print("\nExemplo 2")

with open("8-Arquivos_Excecoes/2-Exemplo_1.txt") as objeto_arquivo_2:
    conteudo_2 = objeto_arquivo_2.read()
    print(conteudo_2.rstrip())

print("Verificação se a linha em branco foi apagada")

"""
Paths de arquivo
    Às vezes, dependendo de como o seu trabalho estiver organizado, o arquivo que você quer abrir não estará no mesmo diretório que o seu arquivo de programa. Para fazer Python abrir arquivos de um diretório que não seja aquele em que seu arquivo de programa está armazenado, é preciso fornecer um path de arquivo, que diz a Python para procurar em um local específico de seu sistema, como foi feito no exemplo anterior.
    Também podemos fornecer um path absoluto, que diz exatamente em que local está o arquivo em seu computador, não importando o lugar em que o programa em execução no momento esteja armazenado. Paths absolutos geralmente são mais longos que paths relativos, portanto é conveniente armazená-los em uma variável e então passar essa variável para open()."""

print("\nExemplo 3")

path = r"C:\Users\perni\OneDrive\Documentos\Exemplo.txt"

with open(path) as objeto_arquivo_3:
    conteudo_3 = objeto_arquivo_3.read()
    print(conteudo_3.rstrip())

r"""A letra #r foi inserida para que não seja interpretado \U como um unicode, o que geraria um erro na chamada.

Lendo dados linha a linha
    Quando estiver lendo um arquivo, com frequência você vai querer analisar cada linhas do arquivo. Talvez você queira procurar uma determinada informação no arquivo ou queira modificar o texto do arquivo de alguma maneira. Para isso podemos usar um laço #for no objeto arquivo para analisar cada uma de suas linhas, uma de cada vez.
    As linhas em branco aparecem sempre que há o final de uma linha, porque há um caracteres invisível de quebra de linha em cada uma no arquivo-texto. Para evitarmos que a instrução print sempre adicione uma linha em branco, não esqueça de utilizar a função rstrip(). Experimente retirá-la para ver o que acontece."""

print("\nExemplo 4")
arquivo_nome_4 = "8-Arquivos_Excecoes/2-Exemplo_1.txt"

with open(arquivo_nome_4) as objeto_arquivo_4:
    for line in objeto_arquivo_4:
        print(line.rstrip())

"""Criando uma lista de linhas de um arquivo
    Quando usamos #with, o objeto arquivo devolvido por open() estará disponível somente no bloco #with que o contém. Se quiser preservar o acesso ao conteúdo de um arquivo fora do bloco, você pode armazenar as linhas do arquivo em uma lista dentro do bloco e então trabalhar com essa lista. Podemos processar partes do arquivo imediatamente e postergar parte do processamento de modo que seja feito mais tarde no programa."""

print("\nExemplo 5")

arquivo_nome_5 = "8-Arquivos_Excecoes/2-Exemplo_1.txt"

with open(arquivo_nome_5) as objeto_arquivo_5:
    lines = objeto_arquivo_5.readlines() #a

for line in lines: #b
    print(line.rstrip())

string_pi = "" #c

print("\nString PI")
for line in lines: #d
    string_pi = string_pi + line.strip()
    print(string_pi)

"""
    Em #a o método readlines() armazena cada linha do arquivo em uma lista. Essa lista é então armazenada em #lines, com a qual podemos continuar trabalhando depois que o bloco #with terminar.
    Em #b usamos um laço #for simples para exibir cada linha de #lines. Como cada item de #lines corresponde a uma linha do arquivo, a saída será exatamente igual ao conteúdo do arquivo.
    Em #c criamos uma variáel que será o número PI em apenas uma linha, e em #d criamos um laço #for para acrescentar cada linha a essa string. A função .strip() foi colocada para eliminar todos os espaços em branco.
    
    *Importante: Quando Python lê um arquivo-texto, todo o arquivo é interpretado como uma string. Se você ler um número e quiser trabalhar com esse valor em um contexto numérico, será necessário convertê-lo em um número inteiro usando a função int() ou para um flutuante com a função float()"""



