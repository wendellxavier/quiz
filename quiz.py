print('======== Quiz de pergutas =======')
perguntas = {
    'Pergunta 1': {
        'Pergunta' : ' Quanto é 7 + 7 ?',
        'respostas': {
            'a': '19',
            'b': '14',
            'c': '16',
            'd': '17'
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2':{
        'Pergunta' : ' Quanto é 6 * 8 ?',
        'respostas': {
            'a': '20',
            'b': '34',
            'c': '48',
            'd': '52'
        },
        'resposta_certa': 'c'
        },
    'Pergunta 3':{
    'Pergunta' : ' Quanto é 6 / 30 ?',
    'respostas': {
        'a': '0,1',
        'b': '0,4',
        'c': '0,5',
        'd': '0,2'
    },
    'resposta_certa': 'd'
    },
    'Pergunta 4': {
        'Pergunta' : ' Quanto é 9 * 8 ?',
        'respostas': {
            'a': '72',
            'b': '80',
            'c': '94',
            'd': '97'
        },
        'resposta_certa': 'a',
    },
    'Pergunta 5':{
        'Pergunta' : ' Quanto é 7 * 9 ?',
        'respostas': {
            'a': '60',
            'b': '56',
            'c': '63',
            'd': '52'
        },
        'resposta_certa': 'c'
        },
    'Pergunta 6':{
    'Pergunta' : ' Quanto é 78 - 26 ?',
    'respostas': {
        'a': '41',
        'b': '31',
        'c': '52',
        'd': '42'
    },
    'resposta_certa': 'c'
    },
    
}

resposta_certas = 0

for chave_p, chave_r in perguntas.items():
    print()
    print(f'{chave_p}:{chave_r["Pergunta"]}')

    print('Escolha opção abaixo')
    for rk, rv in chave_r['respostas'].items():
        print(f'[{rk}]: {rv}')


    respota_usuario = input('Sua resposta: ')

    if respota_usuario == chave_r['resposta_certa']:
        print('Você acertou')
        resposta_certas += 1
    else:
        print('Respota errada')

    print()

qtd_perguntas = len(perguntas)
porcentagem = resposta_certas / qtd_perguntas * 100
porcentagem_arredondada = round(porcentagem, 1)
print(f'Você acertou {resposta_certas} questões')
print(f'Você respondeu {qtd_perguntas} questões, sua porcentagem de acerto é {porcentagem_arredondada} %')

    
if porcentagem < 49:
    print('Voce reprovou')
else:
    print('Voce foi aprovado')