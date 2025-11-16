import json

def abrir_json(arquivo):
    """Abre um json e salva os dicionário na variável, caso não tenho a cria"""
    global usuarios
    try:
        with open(arquivo, encoding="UTF-8") as objeto:
            usuarios = json.load(objeto)
            print(usuarios)
    except:
        print("Arquivo não encontrado, será criado")
        usuarios = {}
    else:
        contato_usuario()
    
def salvar_json(arquivo):
    with open(arquivo, "w", encoding="UTF-8") as objeto:
        json.dump(usuarios, objeto, indent=True, ensure_ascii=False)
        print("Dados salvos!")

def ler_json(arquivo):
    try:
        with open(arquivo, encoding="UTF-8") as objeto:
            conteudo = json.load(objeto)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    else:
        print(conteudo)
        
def contato_usuario():
    """Entra em contato com o usuário e atualiza o dicionário com mais dados"""
    usuario = input("Nome de usuário: ")
    if usuario in usuarios:
        print(f"Bem vindo(a) novamente {usuario}")
        print(f"Seu número favorito é {usuarios[usuario]}")
    else:
        print(f"Bem vindo(a) {usuario.strip()}")
        num_favorito = input("Digite seu número favorito: ")
        usuarios[usuario] = num_favorito

arquivo = r"8-Arquivos_Excecoes\Exercicios\011b.json"

abrir_json(arquivo)
salvar_json(arquivo)
ler_json(arquivo)