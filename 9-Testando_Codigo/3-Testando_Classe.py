"""
Testando uma classe
    Você usará classes em muitos de deus próprios programas, portante é conveniente ser capaz de provar que suas classes funcionem corretamente. Se os testes para uma classe com a qual você estiver trabalahdno passarem, você poderá estar confiante de que as melhorias que fizer nesse classe não causarão falhas por acidente no comportamento atual.
    
Uma variedade de métodos de asserção
    A tabela abaixo descreve seis métodos de asserção comumente usados. Você pode usar esses métodos somente em uma classe que herde de #unitest.TestCase, portante vamos observar como um desses métodos podem ser usados no contexto dos testes de uma classe.
    
    
       Método                        Uso
    |-------------------------------------------------------------------|
    |assertEqual(a, b)             Verifica se a ==b                    |
    |assertNotEqual(a, b)          Verifica se a != b                   |
    |assrtTrue(x)                  Verifica se x é True                 |
    |assertFalse(x)                Verifica se x é False                |
    |assertIn(item, lista)         Verifica se item está na lista       |
    |assertNotItem(item, lista)    Verifica se item não está na lista   |
    |-------------------------------------------------------------------|
    
    
    Testar uma classe é semelhante a testar uma função, portante há algumas diferenças. Vamos escrever uma classe para ser testada"""  

print("Exemplo 1")  

class PesquisaAnonima():
    """Coleta respostas anônima para uma pergunta da pesquisa"""
    
    def __init__(self, questao):
        """Armazena pergunta e se prepara para armazenar respostas"""
        self.questao = questao
        self.nova_resposta = ""
        self.respostas = []

    def mostrar_questao(self):
        """Mostra a pergunta da pesquisa"""
        print("Digite 'q' para sair da enquete")
        self.nova_resposta = input(self.questao)

    def armazenar_resposta(self):
        """Armazena uma única resposta"""
        self.respostas.append(self.nova_resposta)

    def mostrar_resultados(self):
        """Mostra todas as respostas dadas"""
        print("Resposta do questionário:")
        
        for x, resposta in enumerate(self.respostas, 1):
            print(f"{x} - {resposta}")

questao_1 = "Qual a sua cor preferida?\n\t"

anonimo_1 = PesquisaAnonima(questao_1)

while True:
    anonimo_1.mostrar_questao()

    if anonimo_1.nova_resposta == "q":
        break
    else:
        anonimo_1.armazenar_resposta()

print("Obrigado por participarem da enquete!")
anonimo_1.mostrar_resultados()

"""
    Essa classe funciona  para uma pesquisa anônima simples. No entanto, vamos super que queremos aperfeiçoar esse módulo em que se encontra. Poderíamos permitir que cada usuário forneça mais de uma resposta. Poderíamos escrever uma método para listar apenas as respostas únicas e informar quantas vezes cada resposta foi dada. Também poderíamos escrever outra classe para administrar pesquisas não anônimas.
    
    O comportamento atual da classe correria risco de ser afetado com a implementação de mudanças como essas. Por exemplo, é possível que, na tentativa de permitir que cada usuário forneça várias respostas, poderíamos acedentalmente mudar o modo como as respostas únicas são tratadas. Para garantir que não causaremos problemas no comportamento existente à medida que desenvolvemos esse módulo, podemos escrever testes para a classe.
    
    Vamos agora escrever um testa para a classe acima, usaremos o método assertIn() para conferir se a resposta está na lista de respostas depois que ela for armazenada."""

import unittest

print("\nExemplo 2")

class TestPesquisaAnonima(unittest.TestCase):
    """Teste para a classe TestPesquisaAnonima"""

    def test_resposta_unica(self):
        """Testa se há resposta armazenada"""
        anonimo_test = PesquisaAnonima("Qual a sua cor preferida?")
        anonimo_test.nova_resposta = "Azul"
        anonimo_test.armazenar_resposta()
        
        self.assertIn("Azul", anonimo_test.respostas)
        self.assertEqual(len(anonimo_test.respostas), 1)

# unittest.main()

print("\nEemplo 3")

class TestPesquisaAnonima2(unittest.TestCase):
    def teste_resposta_lista(self):
        """Testa se pega todos elementos da lista"""
        anonimo_test2 = PesquisaAnonima("Qual a sua cor preferida?")
        respostas = ["Azul", "Verde", "Laranja"]

        for resposta in respostas:
            anonimo_test2.nova_resposta = resposta
            anonimo_test2.armazenar_resposta()

        self.assertIn("Laranja", anonimo_test2.respostas)
        self.assertIn("Vermelho", anonimo_test2.respostas)
            
unittest.main()


