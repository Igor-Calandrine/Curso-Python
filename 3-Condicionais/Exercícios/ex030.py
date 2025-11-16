""" Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo o nome 'admin'. Suponha que você esteja escrevendo um código que exibirá uma saudação a cada usuário depois que eles fizerem login em um site. Percorra a lista com um laço e mostre uma saudação para cada usuário:
• Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo, Olá admin, gostaria de ver um relatório de status?
• Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por fazer login novamente.
• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns usuários!"""

users1 = ["igor", "bianca", "yuri", "mário", "cristina","admin"]
users = []
adms = ["igor", "admin"]
password = "123"
adm_here = False

login_user = input("Digite seu loggin: ")
login_pass = input("Digite sua senha: ")

login_user_lower = login_user.lower()

if users:
    if len(login_user) > 0:
        if login_user_lower in users and login_pass == password:
        
            for adm in adms:
                if adm == login_user_lower:
                    adm_here = True
            if adm_here == True:
                print(f"Bem vindo admin {login_user.title()}, gostaria de um relatório?")
            else:
                print(f"Bem vindo novamente {login_user.title()}")
            
        else:
            print("Usuário e senha inválidos")
    else:
        print("Digite um usuário") 
else:
    print("Não há usuários no momento")




