dinheiro = input("Digite seu aporte inicial: ")
# dinheiro = int(dinheiro)

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

# def depositando(dinheiro):
#     depositar = int(input("Digite quanto deseja depositar: "))
#     return dinheiro + depositar
#
# executando = mestre(depositando, dinheiro)
# print(executando)

if not dinheiro.isdigit():
    print("Digite um valor!!")
else:
    while True:
        dinheiro = int(dinheiro)
        opcao = int(input("\n[1] Depositar \n[2] Sacar \n[3] Relatorio \n[4] Sair \nDigite a opção: "))
        match opcao:
            case 1:
                depositar = input("Digite quanto deseja depositar: ")
                if not depositar.isdigit():
                    print("Digite um valor!!")
                else:
                    depositar = int(depositar)
                    dinheiro +=  depositar

            case 2:
                sacar = input("Digite o valor que deseja sacar: ")
                if not sacar.isdigit():
                    print("Digite um valor!!")
                else:
                    sacar = int(sacar)
                    if sacar >= dinheiro:
                        print("Valor de saque indisponivel!")
                    else:
                        dinheiro -= sacar
            case 3:
                print(dinheiro)
            case 4:
                break
            case _:
                print('Opção invalida!')
