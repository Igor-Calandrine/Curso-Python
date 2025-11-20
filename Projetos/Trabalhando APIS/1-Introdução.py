"""
Usando uma API web
    Uma API web é uma parte de um site projetada para interagir com programas que usam URLs bem específicos a fim de requisitar determinadas informações. Esse tipo de requisição é conhecido como, chamada de API. Os dados solicitados serão desvolvidos em um formato facilmente processável, por exemplo, JSON ou CSV. 
    
    ?A maioria das aplicações que dependem de fontes de dados exeternos, como aquelas que se integram a sites de mídias sociais, contam com chamadas de API.
    
Requisitando dados usando uma chamada de API
    A API do GitHub permite requisitar várias informações por meioo de chamadas de API. Para ver como é a aparência de uma chamada de API, digite o seguinte na barra de endereço de seu navegador e tecle ENTER:

*    https://api.github.com/search/repositories?q=language:python&sort=stars

    Essa chamda devolve o número de projetos Python hospedados no GitHub no momento, bme como informações sobre os repositórios Python mais populares. Vamos analisar a chamada:
    
    *https://api.github.com/
    Direciona a requisição para a parte do site do GitHub que respode a chamadas de API. 

    *search/repositories
    Diz à API para conduzir uma pesquisa em todos os repositórios do GitHub.
    
    *?
    Indica que estamos prestes a passar um argumento

    *q=
    quer dizer "query" e o sinal = no permite começar a especificá-la.

    *language:python
    sinalizamos que queremos informações somente sobre os repositórios que tenham Python como linguagem principal.

    *&sorts=start
    Ordena os projetos de acordo com o número de estrelas que receberam

    Ao observá-la podemos notar que esse URL não tem como propósito ser usada por seres humanos. O trecho a seguir mostra as primeiras linhas da resposta.

    {
        "total_count": 713062,
        "incomplete_results": false,
        "items": [
        {
            "id": 3544424,
            "name": "httpie",
            "full_name": "jkbrzt/httpie",
            --trecho omitido--


    Se o GitHub não tivesse sido capaz de processar totalmente a requisição da API, ele teria devolvido true em "incomplete_results".

Instalando o pacote request
    O pacote requests permite que um programa Python solicite facilmente informações a um site e analise a resposta devolvida. Para instalar esse pacote, execute:

    $ pip install --user requests

Processando uma resposta de API
    Agora começaremos a escrever um programa para fazer uma chamada de API e processar o resultado identidicando os projetos Python com mais estrelas no GitHub."""

print("Exemplo 1")

import requests

#Faz uma chamada de API
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

resposta = requests.get(url) #a
print(f"Status code: {resposta.status_code}") #a

#Armazena a resposta da API em uma variável
resposta_dict = resposta.json() #b

#Processa o resultado
print(resposta_dict.keys()) #c

"""
    #a,
    Chamamos get() e passamos a URL e armazenamos o objeto com a resposta na variável. O objeto com a resposta tem um atributo chamada #status_code, que nos informa se a requisição foi bem sucedida (código 200).

    #b,
    A API devolve as informações em formato JSON, portanto usamos o método json() para convertê-las em um dicionário Python. Armazenamos o dicionário resultante em #resposta_dict

    #c, 
    Chamos print para exibir penas as chaves desse dicionário

Trabalhando com o dicionário
    Agora que temos a informação da chamada de API na forma de um dicionário, podemos trabalhar com os dados armazenados nele. Vamos gerar um saída que sentetize as informações. Essa é uma boa maneira de garantir que recebemos as informações esperadas e começar a analisar os dados em que estamos interessados:"""

print("\nExemplo 2")

print(f"Total repositórios: {resposta_dict["total_count"]}") #d
print(f"Resultados incompletos: {resposta_dict["incomplete_results"]}") #d
print(f"Quantidade de itens: {len(resposta_dict["items"])}") #d

#Salva a lista de dicionários e abre o item dentro da lista de dicionários
items_dicts = resposta_dict["items"] #e Dicionário Items
item_dicts = items_dicts[0] #e

#Imprime só as informações dentro do dicionário escolhido
print(f"Keys: {len(item_dicts)}") #f
print("\nChaves do dicionário:") #f
print(item_dicts.keys()) #f

"""
#d, 
Exploramos as informações contidas nessas chaves do dicionário, porém não vai ser possível fazer o mesmo com items, pois é uma lista de dicionários com muitas informações que irão poluir a tela. Devemos então filtrar as informações.

#e,
Salvamos a lista de dicionários na variável #items_dicts, e então abrimos o primeiro item dessa lista

#f,
Agora com acesso ai dicionário da lista desejado, podemos obter informações sobre ele.

Agora vamos extrair os valores de agumas das chaves em #item_dicts"""

print("\nInformações slecionadas sobre o respositório:")
print(f"Nome: {item_dicts["full_name"]}")
print(f"Repositório: {item_dicts["html_url"]}")
print(f"Owner: {item_dicts["owner"]["login"]}")
print(f"Stars: {item_dicts["stargazers_count"]}")
print(f"Watchers: {item_dicts["watchers_count"]}")

"""
Trabalhando com todos os repositórios
    Quando quisermos criar uma visualização para todos os respositporios devemos utilizar um laço for, pois trát-se de uma lista de dicionários. Vamos reduzir as informações para poluir menos a tela.
    ?lembrando que a lista de dicionários esta na variável items_dicts
"""

print("\nExemplo 3")

for item in items_dicts:
    print(f"\nNome: {item["full_name"]}")
    print(f"Stars: {item["stargazers_count"]}")
    print(f"Watchers: {item["watchers_count"]}")

"""
Monitorando os limites da taxa de uso da API
    A maioria das APIs tem uma taxa de uso limitada, o que significa que há um limite para quantas requisições podemos fazer em determinado período de tempo. Para ver se estamos nos aproximando dos limites do GitHub, forneça o endereço:
    
*   https://api.github.com/rate_limit

    A informação que estamos interessados é o limite da taxa de uso da API, e vemos que o limite é de dez requisições por minuto e que temos oito requisições restantes para o minuto atual. Se atingir sua quota, você obterá uma resposta breve que permitirá saber que o limite da API foi atingido. Se alcançar o limite, basta esperar até que sua quota seja reiniciada.
    
Visualizando os repositórios usando Pygal
    Agora que temos alguns interessantes, vamos criar uma visualizaçao que mostre a popularidade relativa dos projetos Python no GitHub. Criaremos um gráfico de barras interativas: a altura de cada barra representará o número de estrelas que o projeto recebeu. Clicar em uma barra levará você para a página nicial do projeto GitHub."""

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

nomes, stars = [], [] #g

for item in items_dicts:
    nomes.append(item["name"]) #g
    stars.append(item["stargazers_count"]) #g

#Cria a visualização
meu_estilo = LS("#3030E2", base_style=LCS) #h
chart = pygal.Bar(style=meu_estilo, x_label_rotation=90, show_legend=False) #h
chart.title = "Projetos mais estrelados no GitHub" #h
chart.x_labels = nomes
chart.add("", stars)
chart.render_to_file("Projetos\Trabalhando APIS\python_repos.svg")


"""
#g,
Criamos duas listas vazias para armazenar os dados que incluiremos no gráfico. Precisaremos do nome de cada projeto para rotular as barras e do número de estrelas para determinar a altura delas. No laço, incluimos nessas listas o nome de cada projeto e o número de estrelas

#h,
Definimos um estilo usando a classa LightenStyle como LS, depois utilizamos Bar() para criar um gráfico de barras seimples e lhe passamos #meu_estilo, definimos a totação do nome em 45 graus e ocultamos a legenda, e então fornecemos um nome(título) ao gráfico.

Aperfeiçoando os gráficos do Pygal
    Vamos melhorar a estilização de nosso gráfico. Faremos algumas personalizações diferentes, para isso iremos pssar #config como primeiro argumento, e todas as nossas definições de configuração serão enviadas em um só argumento."""

#Cria a visualização 2
# ---- Config Personalizada ----
config = pygal.Config()
config.x_label_rotation = 70 
config.show_legend = False
config.title_font_size = 30
config.label_font_size = 24
config.x_labels_major_label_font_size = 18
config.truncate_label = 15 #reduz nomes
config.show_y_guides = False #Mostrar linha horizontal da escala y
config.width = 1200 #Define a largura horizontal

chart= pygal.Bar(config, style=meu_estilo)
chart.title = "Projetos mais estrelados no GitHub - Conf Personalizada"
chart.x_labels = nomes
chart.add(f"Respositório x Stars", stars)
chart.render_to_file("Projetos\Trabalhando APIS\python_repos_2.svg")

"""Acrescentando dicas de contexto personalizadas
    No Pygal, ao passar o cursos sobre uma barra individual faz com que as informações representadas pela barra sejam exibidas. Elas são comumente chamadas de dicas de contexto (tooltips) e, nesse caso, mostram o número de estrelas que um projeto tem. Criaremos uma dia de contexto personalizada que mostra também a descrição de cada projeto."""

meu_estilo_2 = LS("#3030E2", base_style=LCS)
chart_2 = pygal.Bar(style=meu_estilo, x_label_rotation=90, show_legend=False)
chart_2.title = "Python Projetos"
chart_2.x_labels = ["httpie", "django", "flask"] 

plot_dctis = [
    {"value": 16101, "label": "Descrição httpie"},
    {"value": 15028, "label": "Descrição Django"},
    {"value": 14798, "label": "Descrição Flask"}
]

chart_2.add("", plot_dctis)
chart_2.render_to_file("Projetos\Trabalhando APIS\python_projetos.svg")

"""
Adicionando links que podem ser clicados em nosso gráfico
    P Pygal também permite usar barra do gráfico com um link para um site. Para acrescentar essa funcionalidade, basta adicionar um linha em nosso nódigo, tirando proveito do dicionário que criamos para da projeto."""

names_3, plot_dctis_3 = [], [] #i

for item in items_dicts:
    names_3.append(item["name"])

    plot_dcti_3 = { #j
        "value": item["stargazers_count"], 
        "label": item["description"],
        "xlink": item["html_url"] 
        }
    
    plot_dctis_3.append(plot_dcti_3) #j
    
meu_estilo_3 = LS("#AFE230", base_style=LCS)
chart_3= pygal.Bar(config, style=meu_estilo)
chart_3.title = "Projetos mais estrelados no GitHub - Links"
chart_3.x_labels = names_3

chart_3.add("", plot_dctis_3)
chart_3.render_to_file("Projetos\Trabalhando APIS\python_repos_link.svg")

"""
#i,
Primeiramente criamos duas listas para conter as informações que serão usada quando plotar o gráfico, assim como foi feito no primeiro exemplo

#j,
A segunda lista será ums série de informações, por isso foi construido um dicionário para cada informação que será colocada no gráfico 
?As chaves são as mesma da variáveis que o Paygal irá reconhecer para gerar o gráfico, disso vem a necessidade de utilizar exatamente os mesmos nomes
Colocamos então esse dionário dentro da lista para ser acessada em #chart_3.add()

Agora você tem uma visualização informativa e interativa dos dados obtidos por meio de uma API.

"""


