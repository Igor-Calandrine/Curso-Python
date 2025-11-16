""""
A função imprime da tela os argumentos
"""
print(34, 78)

""" É possível alterar o separador com: """
print(34, 78, sep="-")
print(45, 98, 67, sep=" @@ ")

"""Também podemos alterar o final. Por padrão é \n, ou seja, uma quebra de linha"""
print(34, 78, sep="-", end=" ** ")
print(45, 98, 67, sep=" == ")

"""Para que textos (Strings) sejam mostrados na tela é necessário que eles estejam entra aspas, simples ou duplas."""
print("Amanhã eu acordo cedo")
print("O queijo esta na geladeira")

"""Pode-se usar aspas detro de uma String, mas é necessário que eles sejam anternadas a entrada."""
print("Amanhã irei 'domir' tarde")
print('Quando', 'você', 'irá', 'á', '"escola"?')
