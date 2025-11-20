"""
A API de HAcker News
    Para explorar o iso de chamadas API em outros sites daremos uma olhada em Hacker News
    
*   http://news.ycombinator.com/

    No site as pessoas compartilhamd artigos sobre programaçao e tecnoogia, e se envolvem em discussões estusiasmadas sobre esses artigos. A API do Hacker News oferece acesso a dados sobre todos os artigos submetidos e os comentários do site, disponíveis sem a necessidade de se registrar parar obter uma chave.
    
    A chamda a seguir devolve informações sobre os principais artigos do momento:
    
*   https://hacker-news.firebaseio.com/v0/item/9884165.json

    A resposta é um dicionário com informações sobre o artigo cujo ID é 9884165. Vamos fazer uma chamda que devolva os IDs dos principais artigos do momento e então analisaremos cada um desses artigos.
    
?Neste aquivivo irei primeiro salvar a API em um arquivo e depois trabalhar em cima dele em JSON e não usarei itemgetter"""

import requests
import json
from operator import itemgetter

#Faz a chamada API \ Armazena a resposta \ Oferece Estatus
url = "https://hacker-news.firebaseio.com/v0/item/9884165.json"
resposta = requests.get(url)
print(f"Estatus: {resposta.status_code}")

resposta_json = resposta.json()

#Salva a API em JSON
path = r"Projetos\Trabalhando APIS\resposta.json"
with open(path, "w", encoding="UTF-8") as objeto:
    json.dump(resposta_json, objeto, ensure_ascii=False, indent=4)

#Cria a lista de Kids          
resposta_kids = []

with open(path, "r", encoding="UTF-8") as objeto:
    r_json = json.load(objeto)

for item in r_json["kids"][:5]:
    resposta_kids.append(item)

print("\nID ------------- ")
for x, item in enumerate(resposta_kids, 1):
    print(f"{x}º ID - {item}")

#Faz a chamada API \ Armazena a resposta \ Oferece Estatus \ Inseri o Dicionário da lista
kids_dicionario = []
print("\n Estatus de cada ID na API -------------")

for item in resposta_kids:
    url = f"https://hacker-news.firebaseio.com/v0/item/{item}.json"
    resposta_kids = requests.get(url)
    print(f"Estatus: {resposta_kids.status_code}")

    resposta_kids_json = resposta_kids.json()

    #// print(resposta_kids_json)

    #Cria o dicionário apartir de Kids
    item_kids_dicionario = {
        "Autor": resposta_kids_json["by"],
        "ID": resposta_kids_json["id"],
        "Comentários": resposta_kids_json["parent"],
        "Link": f"https://news.ycombinator.com/item?id={resposta_kids_json["id"]}"
    }

    kids_dicionario.append(item_kids_dicionario)

#Ordena a lista pela chave Autor
kids_dicionario = sorted(kids_dicionario, key=lambda x: x["Autor"])

path_2 = r"Projetos\Trabalhando APIS\resposta_kids.json"
with open(path_2, "w", encoding="UTF-8") as objeto:
    json.dump(kids_dicionario, objeto, ensure_ascii=False, indent=4)

with open(path_2, "r", encoding="UTF-8") as objeto:
    r_kids= json.load(objeto)

for x, item in enumerate(r_kids, 1):
    print(f"\n{x}º - Item")
    for key, value in item.items():
        print(f"{key} - {value}")
    


