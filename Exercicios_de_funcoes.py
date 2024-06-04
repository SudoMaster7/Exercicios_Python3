def ola(saudacao, nome):
    print(f'{saudacao} {nome}')


def soma(n1, n2, n3):
    print(f'{n1} + {n2} + {n3} = {int(n1) + int(n2) + int(n3)}')


def porcentagem(n1, n2):
    if not n1.isdigit() and n2.isdigit():
        return "Digite numeros!! "
    else:
        porcent = float(n1) * (float(n2)/100)
        return float(n1) + float(porcent)



def fizz_buzz(num):
    if not num.isdigit():
        return "Digite um NUMERO!! "
    num = int(num)
    if num % 5 == 0 and num % 3 == 0:
        return 'FizzBuzz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 3 == 0:
        return 'Fizz'
    return num

ola(input("Digite a saudacao: "), input("Digite seu nome: "))

soma(input("Digite o 1° da soma: "), input("Digite o 2° da soma: "), input("Digite o 3° da soma: "))

n1 = input("Digite um numero para encontar o aumento percentual: ")
n2 = input("Digite sua porcentagem: ")

print(f'O aumento percentual de {n2}% de {n1} é : {porcentagem(n1, n2)}')

num = input('Digite um numero para saber o FizzBuzz: ')
print(fizz_buzz(num))


