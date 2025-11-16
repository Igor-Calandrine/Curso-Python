"""
Usando um laço while com listas e dicionários
    Um laço for é eficiente para percorrer uma lista, mas você não deve modificar uma lista em um laço for, pois  Python terá problemas para manter o controle dos itens da lista. Para modificar uma lista enquanto trabalhar  com ela, utilize um laço while. Usar laços while com listas e dicionários permite coletar, armazenar e organizar muitas entradas a fim de analisá-las e apresentá-las posteriormente.
    
Transferindo itens de uma lista para outra
    Começamos com uma lista de usuários não confirmados em #u (Alice,Brian e Candace) e uma lista vazia para armazenar usuários confirmados. O laço while em #v executa enquanto a lista unconfirmed_users não estiver vazia. Nesse laço, a função pop() em #w remove os usuários não verificados, um de cada vez, do final de unconfirmed_users. Nesse caso, como Candace é o último elemento da lista unconfirmed_users, seu nome será o primeiro a ser removido, armazenado em current_user e adicionado à lista confirmed_users em x. O próximo é Brian e, depois, Alice."""

print("Exemplo 1")
unconfirmed_users = ['alice', 'brian', 'candace'] #u
confirmed_users = []
 
while unconfirmed_users: #v
    current_user = unconfirmed_users.pop() #w
 
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user) #x
 
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

"""
Removendo todas as instâncias de valores específicos de uma lista
    Começamos com uma lista contendo várias instâncias de 'cat'. Após exibir a lista, Python entra no laço while, pois encontra o valor 'cat' na lista pelo menos uma vez. Depois que entrar no laço, Python remove a primeira instância de 'cat', retorna à linha while e então entra novamente no laço quando descobre que 'cat' ainda está na lista. Cada instância de 'cat' é removida até que esse valor não esteja mais na lista, nesse momento, Python sai do laço e exibe a lista novamente."""

print("\nExemplo 2")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
 
while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

"""
Preenchendo um dicionário com dados de entrada do usuário
    Nesse laço é solicitado ao usuário  que entre com seu nome e uma montanha que gostaria de escalar #u. Essa informação é armazenada no dicionário responses #v, e uma pergunta é feita ao usuário para saber se ele quer que a enquete continue #w. Se o usuário responder yes, o programa entrará no laço while novamente. Se responder no, a flag polling_active será definida com False, o laço while para de executar e o último bloco de código em #x exibe o resultado da enquete."""

print("\nExemplo 3")
responses = {}
 
polling_active = True #Flag
 
while polling_active:
    name = input("\nWhat is your name? ") #Nome
    response = input("Which mountain would you like to climb someday? ") #montanha
    responses[name] = response #v insere no dicionário
    repeat = input("Would you like to let another person respond? (yes/no) ") #w
    
    if repeat == 'no':
        polling_active = False
        
print("\n--- Poll Results ---")
for name, response in responses.items(): #x
    print(name + " would like to climb " + response + ".")