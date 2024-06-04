numero = input("Digite seu numero: ")
if numero.isdigit():
    if numero % 2 == 0:
        print(f'O {numero} é par')
    if numero % 2 != 0:
        print(f'O {numero} é impar')
else:
    print("Issão não é numero inteiro!!")

