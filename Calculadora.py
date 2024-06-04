def soma(n1, n2):
    return n1 + n2


def subitracao(n1, n2):
    return n1 - n2


def multiplicacao(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    if not n2 == 0:
        return n1 / n2
    else:
        return f'Não é possivel dividir por 0'


def valores():
    n1 = input('Digite o primeiro valor que deseja calcular: ')
    n2 = input('Digite o segundo valor: ')

    if not n1.isdigit() and n2.isdigit():
        print('Digite Numeros!! ')
    else:
        n1 = float(n1)
        n2 = float(n2)

        opr = input('Digite a operação que de seja fazer: [+, -, *, /]: ')
        if opr == '+':
            print(soma(n1, n2))
        elif opr == '-':
            print(subitracao(n1, n2))
        elif opr == '*':
            print(multiplicacao(n1, n2))
        elif opr == '/':
            print(divisao(n1, n2))
        else:
            print('Operação invalida!!')


while True:
    valores()
    off = input('Deseja Continuar? [s]im [n]ão: ')
    if off == 'n':
        break
