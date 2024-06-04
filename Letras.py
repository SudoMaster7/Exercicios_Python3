nome = input("Digite seu nome: ")
letras_do_nome = len(nome)

if letras_do_nome <= 4:
    print(f"Olá {nome} seu nome tem {letras_do_nome} letras, ele é curto")
elif letras_do_nome <= 6:
    print(f"Olá {nome} seu nome tem {letras_do_nome} letras, ele é normal")
else:
    print(f"Olá {nome} seu nome tem {letras_do_nome} letras, ele é muito grande")
