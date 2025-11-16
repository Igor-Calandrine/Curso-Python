"""Cidade, país: Escreva uma função que aceite dois parâmetros: o nome de uma cidade e o nome de um país. A função deve devolver uma única string no formado Cidade, País, por exemplo, Santiago, Chile. Armazene a função em um módulo chamado city_functions.py. Crie um arquivo de nome test_cities.py que teste a função que você acabou de escrever (lembre-se de que é necessário importar unittest e a função que você quer testar). Escreva um método chamado test_city_country() para conferir se a chamada à sua função com valores como 'santiago' e 'chile' resulta na string correta. Execute test_cities.py e garanta que test_city_country() passe no teste."""

import unittest
from a001 import cidade_paiz

class TestCidade_paiz (unittest.TestCase):
    def test_cidade_paiz(self):
        conteudo = cidade_paiz("belém", "brasil")
        self.assertEqual(conteudo, "Belém Brasil")


unittest.main()
