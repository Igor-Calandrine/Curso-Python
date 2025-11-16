"""Introdução -
    Neste capítulo aprenderemos a aceitar dados de entrada do usuário para que seu programa possa então trabalhar com eles. Quando seu programa precisar de um nome, você poderá solicitá-lo ao usuário. 
    Também veremos como manter os programas executando pelo tempo que  os  usuários  quiserem,  de  modo  que  eles  possam  fornecer  quantas informações forem , e em seguida seu programa poderá trabalhar com essas informações. Usaremos o laço while de Python para manter os programas executando enquanto determinadas condições permanecerem verdadeiras.

Como a função input() trabalha
    A  função  input() faz  uma pausa em seu programa e espera o usuário fornecer um texto. Depois que Python recebe a entrada do usuário, esse dado é armazenado em uma variável para que você possa trabalhar com ele de forma conveniente.
    Acrescente um espaço no final de seus prompts (depois dos dois-pontos no  exemplo  anterior) para separar o  prompt da resposta do usuário e deixar claro em que lugar o usuário deve fornecer seu texto. """

print("Exemplo 1")
palavra = input("Digite uma palavra: ")
print(palavra)

"""
input() multilinha
   Esse exemplo mostra uma maneira de criar uma string multilinha. A primeira linha armazena a parte inicial da mensagem na variável prompt. Na segunda linha, o operador += acrescenta a nova string no final da string que estava armazenada em prompt."""

print("\nExemplo 2")
prompt = "Por favor, para melhor segurança precisamos de validar seus dados."
prompt += "\nDigite seu CPF: "

cpf = input(prompt)

"""
Usando int() para aceitar entradas numéricas
    Se  usarmos a função  input(), Python interpretará tudo que o usuário fornecer como uma string, portanto se tentar usar a entrada como um número, você obterá um erro. Podemos resolver esse problema usando a função int(), que diz a Python para tratar a entrada como um valor numérico. A função int() converte a representação em string de um número em uma representação numérica.
    Assim também podemos usar float() para determinar a entrada de números não inteiros."""

print("\nExemplo 3")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Acesso liberado")
else:
    print("Acesso negado")

print("\nExemplo 4")

preço = float(input("Digite o valor do item.\n\t"))

venda = preço + preço*0.2
print(f"Venda: {venda}" )