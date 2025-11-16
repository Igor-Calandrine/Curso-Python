"""
Testando uma função
    Para aprender a testar, precisamos de um código para testes. Eis uma função simples que aceita um primeiro nome e um sobrenome e devolve um nome completo formatado de modo elegante."""

print("Exemplo 1")

def nome_elegante(primeiro_nome, ultimo_nome):
    # primeiro_nome = input("Digite seu primeiro nome: ")
    # ultimo_nome = input("Digite se último nome: ")
    nome_completo = f"{primeiro_nome} {ultimo_nome}"
    return nome_completo.title()

"""
Teste de unidade e casos o de teste
    O módulo #unittest da biblioteca-padrão de Python oferece as ferramentas para testar seu código. 
    
    Um teste de unidade verifica se um aspecto específico do comportamento de uma função esta correto. 
    
    Um caso de teste é uma coleção de testes de unidade que, em conjunto, prova que uma função se comporta como deveria em todas as situações que você espera que ela trate. Um bom caso de teste considera todos os tipo possíveis de entradas que uma função poderia receber e inclui testes para representar cada uma dessas situações. 
    
    Um caso de teste com cobertura completa é composta de uma variedade de testes de unidade que inclui todas as possíveis maneiras de usar uma função. Atingir a cobertura completa em um projeto de grande porte pode ser desanimador. Em geral é suficiente escrever testes para os comportamentos críticos de seu código e então visar uma cobertura completa somente se o projeto começar a ter uso disseminado.
    
Um teste que passa
    A sintaxe para criar um caso de teste exige uma pouco de prática. Para escrever um caso de teste para uma função, importe o módulo #unittest e a função que você quer testar. Em seguida crie uma classe que herde de #unittest.TestCase e escreva uma série de métodos para testar diferentes aspectos do comportamento de sua função."""

import unittest

class TesteCasoNome(unittest.TestCase): #a
    """Teste para nome_elegante"""

    def test_nome_elegante(self): #b
        nome_completo = nome_elegante("janes", "joplin")
        self.assertEqual(nome_completo, "Janes Joplin") #c

unittest #se adicionar .main() ele fechará o programa

#a
"""Criamos um classe que conterá uma série de testes de unidade para a função. Você pode dar o nome que quiser para a classe, mas é melhor nomeá-la com palavras relacioadas à função que você está prestes a testar com Teste na frente. Essa classe deve herdar da classe unittest.TEstCase para que Python saiba executar os testes que você escrever."""
#b
"""Chamamos esse método porque estamos verificando se os nomes que têm apenas o primeiro nome e o sobrenome são formatados corretamente. Qualquer método que comece com test_ será executado de modo automático quando o programa for executado."""
#c
"""Usamos um dos recusos mais úteis de #unittest: um método de asserção. Os métodos de asserção verificam se um resultado recebido é igual ao resultado que você esperava receber com #AssertEqual().

Um teste que falha
    Vamos modificar a função para que trate de nomes do meio, mas faremos isso de modo que a função gere um erro para nomes que tenham apenas um primeiro nome e um sobrenome.
    
    Na saída tem um #E, que nos informa que um teste de unindade do caso de teste resultou em erro. A sefuir vemos que causou um erro. Em seguida vemos no traceback pasdrão que afunção não funciona, pois um argumento posicional obrigatório está ausente. """

print("\nExemplo 2")

def nome_elegante_2(primeiro_nome, meio_nome ,ultimo_nome):
    # primeiro_nome = input("Digite seu primeiro nome: ")
    # ultimo_nome = input("Digite se último nome: ")
    nome_completo = f"{primeiro_nome} {meio_nome} {ultimo_nome}"
    return nome_completo.title()

class TestCasoNome2(unittest.TestCase):
    """Teste para nome elegante"""
    def test_nome_elegante_2(self):
        nome_completo_2 = nome_elegante_2("igor", "araújo")
        self.assertEqual(nome_completo_2,"Igor Araújo")

unittest.main()

