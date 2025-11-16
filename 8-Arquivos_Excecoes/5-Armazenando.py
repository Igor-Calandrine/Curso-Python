"""
Armazenando Dados
    Qualquer que seja o foco de seu programa, vicê armazenará as informações fornecidas pelos usuários em estruturas de dados como listas e dicionários. Quando usuários fecham um programa, quase sempre você vai querer salvar as informações que eles fornecem. Uma maneira simples de fazer isso envolve armazenar seus dados usando o mósulo #json
    
    O módulo #json permite descarregar estruras de dados Python seimples em um arquivo e carregar os dados desse arquivo na próxima vez que o programa executar. Também podemos usar para com compartilhar dados entre diferentes programas Python.
    
    O formato de dados #json não é específico de Python, portanto podemos compartilhar dados armazenados com pessoas que trabalhaam com várias outras linguagens de programação. [E um formato útil e portável, além de ser fácil de aprender.

Usando json.dump() e json.load()
    Vamos escrever um pequeno programa que armazene um conjunto de números e outro que leia esses números de volta para a mamória. O primeiro programa usará json.sum() e o segundo json.load()
    
    Inicialmente importamos o módulo #json e criamos uma lista de números com a aqual trabalharemos."""

print("Exemplo 1")

import json
numeros = [2, 3, 5, 6, 8, 10]

arquivo_nome = r"8-Arquivos_Excecoes\5a-numeros.json" #a

with open (arquivo_nome, "w") as objeto: #b
    json.dump(numeros, objeto) #c

"""
    Em #a, escolhemos o nome de um arquivo em que armazenaremos a lista de números. É comum usar a extensão de arquivo #json para indicar que os dados do arquivo estão armazenados nesse formato.
    Em #b, abrimos o arquivo para escrita, o que permite escrever os dados.
    Em #c, usamos a função para armazenar a lista no arquivo.
    Para melhor visualização, delete o arquivo e depois olhe o seu conteúdo.
    
    Agora iremos colocar a lista na memória afim de ler"""

print("\nExemplo 2")

with open(arquivo_nome, encoding="UTF-8") as objeto:
    conteudo = json.load(objeto) #d

print(conteudo)

"""
    Em #d usamos a função para carregar as informações armazenadas e as guardamos na variável. Por fim, exibimos a lista de números.
    
Refatoração
    Com frequência você chegará a um ponto em que seu código funcionará, mas reconhecerá que ele poderia ser melhorado se fosse dividido em uma série de funções com tarefas específicas. Esse processo se chama #refatoração. Ela deixa seu código mais limpo, mais fácil de compreender e de entender."""

    