secreta = 'bola'
digitadas = []
chance = 3

while True:
    if chance <= 0:
        print("Você perdeu!!\n")
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print("Digite apenas uma letra!!")
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'Parabéns a letra {letra} esta correta!\n')
    else:
        print(f'A letra {letra} não esta na palavra\n')
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreta:
        print(f"Parabéns você ganhou a palavra era {secreto_temporario}!!!\n")
        break
    else:
        print(f'A palavra secreta está assim {secreto_temporario}\n')
    if letra not in secreta:
        chance -= 1
    print(f'Você ainda tem {chance} chances.')