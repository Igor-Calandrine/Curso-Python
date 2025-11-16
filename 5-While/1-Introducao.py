"""
Introdução aos laços while
    O laço for toma uma coleção de itens e executa um bloco de código uma vez para cada item da coleção. Em  comparação, o laço while executa durante o tempo em que, ou enquanto,  uma  determinada  condição  for verdadeira.
    Na primeira linha começamos a contar de 1 ao definir o valor de numero_atual com 1. O laço while é então configurado para continuar executando enquanto o valor de numero_atual for menor ou igual a 5. O código no laço exibe o valor numero_atual e então soma 1 a esse valor com numero_atual += 1."""

print("Exemplo 1")
numero_atual = 1
while numero_atual <= 5:
    print(numero_atual)
    numero_atual += 1

"""
Deixando o usuário decidir quando quer sair
    Na primeira vez que o programa executar e Python alcançar a instrução while, ele deverá comparar o valor de message com 'quit', mas o usuário ainda não forneceu nenhuma entrada. Se Python não tiver nada para comparar, ele não será capaz de continuar executando o programa. Para  resolver  esse problema,  garantimos  que  message  receba  um  valor inicial. Embora seja apenas uma string vazia, ela fará sentido para Python e permitirá que a comparação que faz o laço while funcionar seja feita. Esse laço while w executa enquanto o valor de message não for 'quit'."""

print("\nExemplo 2")
prompt = "Escreva alguma coisa para eu reornar a você."
prompt += "\n\tou digite 'quit' para encerrar: "

palavra = ""

while palavra != "quit":
    palavra = input(prompt)
    
    if palavra != "quit":
        print(palavra)

"""
Usando uma flag
    Para  um  programa  que  deva  executar  somente  enquanto  muitas condições forem verdadeiras, podemos definir uma variável que determina se o programa como um todo deve estar ativo. Essa variável, chamada de flag,  atua  como  um  sinal  para  o  programa.  Podemos  escrever  nossos programas de modo que executem enquanto a flag estiver definida com True e parem de executar quando qualquer um dos vários eventos definir o valor  da  flag  com  False.  Como  resultado,  nossa  instrução  while  geral precisa  verificar  apenas  uma  condição:  se  a  flag,  no  momento,  é  True. Então  todos  os  nossos  demais  testes podem estar bem organizados no restante do programa."""

print("\nExemplo 3")
prompt = "Escreva alguma coisa para eu retornar a você."
prompt += "\n\tou digite 'quit' para encerrar: "

palavra = ""
ativo = True
while ativo == True:
    palavra = input(prompt)
    
    if palavra != "quit":
        print(palavra)
    else:
        ativo = False

"""
Usando break para sair de um laço
    Para sair de um laço while de imediato, sem executar qualquer código restante no laço, independentemente do resultado de qualquer teste condicional, utilize a instrução break. A instrução break direciona o fluxo de seu programa, podemos usá-la para controlar quais linhas de código são ou não são executadas, de modo que o programa execute apenas o código que você quiser, quando você quiser. Um laço que comece com while True executará indefinidamente, a menos que alcance uma instrução break. """

print("\nExxemplo 4")
prompt = "Digite a cidade que você mais gostou de visitar."
prompt += "\n\t ou digite 'quit' para encerrar: "

cidade = ""
while True:
    cidade = input(prompt)
    
    if cidade != "quit":
        print(f"Cidade preferida: {cidade}")
    else:
        print("Programa encerrado.")
        break

"""
Usando continue em um laço
    Em vez de sair totalmente de um laço sem executar o restante de seu código, podemos usar a instrução continue para retornar ao início, com base no resultado de um teste condicional. Por exemplo, considere um laço que  conte de 1 a 10, mas apresente apenas os números ímpares desse intervalo. A instrução continue diz a Python para ignorar o restante do laço e voltar ao início. Se o número atual não for divisível por 2, o restante do laço será executado e Python exibirá o número atual"""

current_number = 0
while current_number < 10:
    current_number += 1
    
    if current_number % 2 == 0:
        continue
    
    print(current_number)

"""
Evitando loops infinitos
    Todo programador escreve ocasionalmente um loop infinito (ou laço infinito) com while por acidente, em especial quando os laços do programa tiverem condições de saída sutis. Se seu programa ficar preso em um loop infinito, tecle CTRL-C ou simplesmente feche a janela do terminal que está exibindo a saída de seu programa. Para evitar escrever loops infinitos, teste todos os laços while e certifique-se  de  que  eles  serão encerrados  conforme  esperado. Se quiser que seu programa termine quando o usuário fornecer determinado  valor de entrada, execute o programa e forneça esse valor.
    IMPORTANTE: UM LAÇO INFINITO PODE DANIFICAR SEU PROCESSADOR"""





