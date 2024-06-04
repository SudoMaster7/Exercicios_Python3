while True:

    cpf = input("Digite um cpf: ")
    novo_cpf = cpf[:9]
    total = 0

    reverso = 10
    for i in range(19):
        if i > 8:
            i -= 9

        total += int(novo_cpf[i]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    if cpf == novo_cpf:
        print(f'CPF {cpf} é valido')
        off = input("Deseja continuar [s]im [n]ão: ")
        if off == 'n':
            break
    else:
        print(f'CPF {cpf} é invalido')
        off = input("Deseja continuar [s]im [n]ão: ")
        if off == 'n':
            break
