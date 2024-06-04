print()
print('Texto explicativo')


perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qunato é 2+2?',
        'respostas': {'a': '1', 'b': '4', 'c': '3'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Qunato é 5*2?',
        'respostas': {'a': '6', 'b': '2', 'c': '10', },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Qunato é 1+2?',
        'respostas': {'a': '6', 'b': '2', 'c': '3', },
        'resposta_certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': 'Qunato é 1-1?',
        'respostas': {'a': '0', 'b': '2', 'c': '10', },
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Qunato é 8/4?',
        'respostas': {'a': '6', 'b': '2', 'c': '10', },
        'resposta_certa': 'b',
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Resposta:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input("Sua resposta: ")

    if resposta_usuario == pv['resposta_certa']:
        print("Certa resposta!!")
        respostas_certas += 1
    else:
        print('Putz você errou!!')

    print()

qnt_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qnt_perguntas * 100

if respostas_certas > 1:
    print(f'Você acertou {respostas_certas} respostas.')
else:
    print(f'Você acertou {respostas_certas} resposta.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')