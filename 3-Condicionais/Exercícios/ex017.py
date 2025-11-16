# Verificar se a idade é entre 13 e 17 (adolescente).

idade = input("Digite sua idade:\n")

if bool(idade) == True:
    idade_int = int(idade)

    if 13 <= idade_int <= 17:
        print(f"Sua idade de {idade_int} anos é de um adolescente")
    else:
        print(f"Sua idade de {idade_int} anos não é de um adolescente")

else:
    print("Não há idade digitada")