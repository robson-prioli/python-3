import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


while True:
    for pergunta in perguntas:
        print(f'Pergunta: {pergunta['Pergunta']}\n')

        print(f'Opções:\n')
        for i, value in enumerate(pergunta['Opções']):
            print(f'{i+1}) {value}')  

        resposta = input(f'Esolha uma opção:')


        try:
            resposta = int(resposta) 
        except:
            print('vc opitou por n jogar.')

        if resposta == 0 or resposta > 4:
            continue

        respostas = list(pergunta['Opções'])
        if respostas[int(resposta) - 1] == pergunta['Resposta']:
            print('Uau! vc é ferra nisso!\n\n')
        else:
            print('vc errou!\n\n')
        os.system('cls')