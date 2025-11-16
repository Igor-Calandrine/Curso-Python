"""Verificando se é o usuário correto: A última listagem de remember_me.py supõe que o usuário já forneceu seu nome ou que o programa está executando pela primeira vez. Devemos modificá-lo para o caso de o usuário atual não ser a pessoa que usou o programa pela última vez. Antes de exibir uma mensagem  de boas-vindas de volta em greet_user(), pergunte ao usuário se seu nome está  correto. Se não estiver, chame get_new_username() para obter o nome correto."""


import json

arquivo_user = r"8-Arquivos_Excecoes\Exercicios\013a.json"

def bem_vindo(arquivo_user):
    global usuarios
    try:
        with open(arquivo_user, encoding="UTF-8") as objeto_json:
            usuarios = json.load(objeto_json)
            print(usuarios)
    except:
        print("Arquivo não encontrado, será criado")
        usuarios = []
    else:
        if len(usuarios) > 0:
            print(f"Bem vindo, usuário {usuarios[-1]}?")

            while True:
                confirmacao = input(("(S)Sim ou (N)Não: "))
                if confirmacao.upper() == "S":
                    print(f"Bem vindo novamente {usuarios[-1]}\n")
                    break
                elif confirmacao.upper() == "N":
                    usuario = input("Digite o seu nome de usuário:\n\t")
                    
                    if usuario in usuarios:
                        usuarios.remove(usuario)
                        usuarios.append(usuario)
                        print(f"Bem vindo novamente {usuario}\n")
                    else:
                        usuarios.append(usuario)
                        print(f"Bem vindo {usuario}\n")
                    break
                
                else:
                    print("Por favor digite: ")
                    continue
        else:
            usuario = input("Digite o seu nome de usuário:\n\t")
            usuarios.append(usuario)

def salvar_arquivo(arquivo_user):
    with open(arquivo_user, "w", encoding="UTF-8") as objeto_json:
        json.dump(usuarios, objeto_json, indent=2, ensure_ascii=True)
        print("Dados salvos")
    print(usuarios)

bem_vindo(arquivo_user)
salvar_arquivo(arquivo_user)
