"""População:  Modifique sua função para que ela exija um terceiro parâmetro,  population. Agora ela  deve devolver uma única string no formato Cidade, País – população xxx, por exemplo, Santiago, Chile – população 5000000. Execute test_cities.py novamente. Certifique-se de que test_city_country() falhe dessa vez. Modifique a função para que o parâmetro population seja opcional. Execute
"""
import unittest
from a002 import cidade_paiz

class TestCidade_paiz(unittest.TestCase):
    def test_cidade_paiz(self):
        conteudo = cidade_paiz("belém", "brasil", 12000)
        self.assertEqual(conteudo, "Belém: Brasil - popUlação: 12000")

unittest.main()

