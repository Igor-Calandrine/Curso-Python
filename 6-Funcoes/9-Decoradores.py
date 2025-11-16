"""
Python Decoradores
    Um decorador em Python é um recurso que permite modificar ou estender o comportamento de uma função, método ou classe sem alterar o seu código-fonte diretamente. Ela é um função que recebe outra função como argumento e reorna uma nova função.
    
    Resumindo, uma decorador "envolve" outra função, adicionando camadas extras de comportamento a ela.
    
    Um decorador é baseado em funções de ordem superior, ou seja, funções que recebem outras funções como parÂmetros ou retornam funções. No exemplo abaixo veremos uma função dentro de outra função."""

print("Exemplo 1")

def decorador(funcao): #a
    
    def nova_funcao(): #b
        print("Antes da função original")
        funcao() #a
        print("Depois da função original")
    
    return nova_funcao

def diga_oi(): #c
    print("Oi!")

funcao_decorada = decorador(diga_oi)
funcao_decorada()

#a,
"""Fizemos uma função que tem apenas um argumento mas que ele será uma outra função"""
#b;
"""Temos uma função dentro que será responsável por armazenar o parâmetro da função superior"""
#c,
"""Criamos a função que definirá o que acontecerá no parâmetro da função #decorador, lembrando que ela esta dentro de #nova_funcao

    Agora aplicaremos o Python decoradores para fornecer uma forma sintática mais simples. O código acima agora será escrito com o decorador primeiro acompanhado de @ na frente e acima da função. Vejamos o exemplo abaixo :"""

print("\nExemplo 2")

@decorador
def diga_boa():
    return "Boa!!"

print(diga_boa())


"""Isso é o mesmo que:"""

"""Não gostei desse recurso, desisti
"""

    
    

