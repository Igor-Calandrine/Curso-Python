"""Percorrendo uma lista inteira com um laço

Com frequência, você vai querer percorrer todas as entradas de uma lista, executando a mesma tarefa em cada item. Por exemplo, em um jogo, você pode mover todos os elementos da tela de acordo com a mesma distância, em uma lista de números, talvez você queira executar a mesma operação estatística em todos os elementos.
Poderíamos fazer isso recuperando cada nome da lista individualmente, mas essa abordagem poderia causar vários
problemas. Para começar, seria repetitivo fazer isso com uma lista longa de nomes. Além disso, teríamos que alterar o nosso código sempre que o tamanho da lista mudasse. Um laço for evita esses dois problemas ao permitir que Python administre essas questões internamente."""

magicians = ['alice', 'david', 'carolina']
for magician in magicians: #v
    print(magician.title()) #w

"""Em v definimos um laço for. Essa linha diz a Python para extrair um nome da lista magicians e armazená-lo na variável magician. Em w dizemos a Python para exibir o nome que acabou de ser armazenado em magician. O interpretador então repete as linhas v e w, uma vez para cada nome da lista. Ler esse código como “para todo mágico na lista de mágicos, exiba o nome do mágico” pode ajudar.

Tenha em mente também que quando escrever seus próprios laços for, você poderá escolher qualquer nome que quiser para a variável temporária que armazena cada valor da lista. No entanto, é conveniente escolher um nome significativo, que represente um único item da lista."""

"""Usando a função enumerate

A função enumerate gera uma tupla em que o primeiro valor é o índice e o segundo é o elemento da lista sendo enumerada. Ao utilizarmos x, e em for, indicamos que o primeiro valor da tupla deve ser colocado em x, e o segundo, em e. Assim, na primeira iteração teremos a tupla (0,5), onde x=0 e e=5. Isso é possível porque
Python permite o desempacotamento de valores de uma tupla, atribuindo um elemento da tupla a cada variável em for. """

numbers = [5,9,13]
for x, number in enumerate(numbers):
    print(f"{x}º - number {number}")