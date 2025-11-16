"""
Escrevendo dados em um arquivo
    Uma das maneiras mais simples de salvar dados é escrê-los em um arquivo. Quando um texto e escrito em um arquivo, o resultado estará disponível depois que você fechar o terminal que contém a saída do seu programa. Além disso, podemos escrever programas que leiam o texto de volta para a memória e trabalhar com esses dados novamente.
    
Escrevendo dados em um arquivo vazio
    Para escrever um texto em um arquivo, chame open() com um segundo argumento que diga a Python que você quer escrever dados no arquivo.
    
    #w, diz a Python que queremos abrir o arquivo em #modo de escrita, assim também temos: 
    #r, como modo de leitura
    #a, como modo de concatenação
    #r+, como modo de que permita ler e escrever no arquivo 
    
    """

print("Exemplo 1")

arquivo = "8-Arquivos_Excecoes/3-Exemplo_1.txt"

with open(arquivo) as objeto:
    conteudo = objeto.read()
    print(conteudo)

with open(arquivo, "w") as objeto_arquivo: #a
    objeto_arquivo.write("Eu amo trabalhar!") #b

with open(arquivo) as objeto:
    conteudo = objeto.read()
    print(conteudo)

"""Abaixo temos o exemplo de um arquivo foi criado para exemplificar, apague o arquivo caso já esteja criado."""

print("\nExemplo 2")

arquivo_2 = "8-Arquivos_Excecoes/novo_arquivo.txt"

with open(arquivo_2, "w") as objeto_arquivo_2: 
    objeto_arquivo_2.write("Arquivo criado para exemplos") 

with open(arquivo_2) as objeto_arquivo_2:
    conteudo = objeto_arquivo_2.read()
    print(conteudo)

"""
    Se o argumento de modo for omitido, por padrão Python abrirá o arquivo em modo somente de leitura.
    A função open() cria automaticamente o arquivo no qual você vai escrever caso ele ainda não exista. Tome cuidado ao abrir um arquivo em modo de escrita ("w") porque se o arquivo já existir, Python o apagará antes de devolver o objeto arquivo. 
    Experimente alterar a frase em #b para ver o arquivo sendo alterado.
    
    *Python escreve apenas strings em um arquivo-texto. Sequiser armazenar dados numéricos em um arquivo-texto, será necessário converter os dados em um formato de strings antes usando a função str()
    
Escrevendo várias linhas
    A função write() não acrescenta nenhuma quebra de linha ao texto que você escrever. Portanto, se escrever mais de uma linha sem incluir caracteres de quebra de linhas, seu arquivo poderá não ter a aparência desejada. É necessário a inclusão de quebras de linhas na sua instrução para aparecer da forma desejada, também podemos utilizar tabulações como já fizemos durante o curso."""

print("\nExemplo 3")

arquivo_3 = "8-Arquivos_Excecoes/3-Exemplo_1.txt"

with open(arquivo_3, "w") as objeto:
    objeto.write("Primeira frase.")
    objeto.write("Segunda frase.")

with open(arquivo_3) as objeto:
    conteudo = objeto.read()
    print(conteudo)

print("\nAgora com a quebras de linha incluída")

with open(arquivo_3, "w") as objeto:
    objeto.write("Primeira frase.\n")
    objeto.write("Segunda frase.\n")

with open(arquivo_3) as objeto:
    conteudo = objeto.read()
    print(conteudo.rstrip())

"""
Concatenando dados em um arquivo
    Se quiser acrescentar conteúdos em um arquivo em vez de sobrescrever o conteúdo existente, você pode abrir o arquivo em #modo de concatenação. Nesse modo Python não apagará o arquivo antes de devolver o objeto arquivo. Qualquer linhas que você escrever no arquivo será adicionada no final. Se o arquivo não existe, ele criará um novo para você.
    Vamos utilizar como exemplo o anterior para concaternar com novas frases."""

print("\nExemplo 4")
with open(arquivo_3, "a") as objeto:
    objeto.write("Terceira frase\n")
    objeto.write("Quarta frase\n")

with open(arquivo_3) as objeto:
    conteudo = objeto.read()
    print(conteudo)



    
