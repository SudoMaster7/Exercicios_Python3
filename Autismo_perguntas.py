import os

print()
print('Texto explicativo')


perguntas = {
    'Pergunta 1': {
        'pergunta': 'O que é o autismo?',
        'respostas': {'a': 'Uma doença contagiosa.', 'b': 'Um transtorno do desenvolvimento neurológico.', 'c': 'Uma alergia alimentar.'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quais são alguns sinais comuns de autismo em crianças?',
        'respostas': {'a': 'Dificuldade em fazer amigos.', 'b': 'Habilidade excepcional em matemática.', 'c': 'Aversão a cores vivas.', },
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Qual é uma característica comum do autismo?',
        'respostas': {'a': 'Hiperatividade extrema.', 'b': 'Dificuldade com a comunicação social.', 'c': 'Medo de água.', },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Como podemos apoiar pessoas com autismo?',
        'respostas': {'a': 'Ignorando suas necessidades.', 'b': 'Sendo pacientes e compreensivos.', 'c': 'Fazendo piadas sobre o autismo.', },
        'resposta_certa': 'b',
    },
    'Pergunta 5': {
        'pergunta': 'O que significa “estimulação sensorial” no contexto do autismo?',
        'respostas': {'a': 'Uma técnica de meditação.', 'b': 'A sensação de tontura.', 'c': 'A resposta do cérebro a estímulos sensoriais como luz, som e toque.', },
        'resposta_certa': 'c',
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
        os.system('color 0A')
        print("Certa resposta!!")
        respostas_certas += 1
    else:
        os.system('color 04')
        print('Putz você errou!!')

    print()

qnt_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qnt_perguntas * 100

os.system('color 07')
if respostas_certas > 1:
    print(f'Você acertou {respostas_certas} respostas.')
else:
    print(f'Você acertou {respostas_certas} resposta.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')