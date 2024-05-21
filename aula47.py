import os

tentativas = 0
palavra_secreta = 'presente'
letras_acertadas = ''

os.system('cls')

while True:
    letra_digitada = input('Digite uma letra:').lower()
    if len(letra_digitada) > 1:
        print('apenas uma lentra')
        continue

    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    print(letras_acertadas)

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    tentativas += 1 

    print('Palavra formada: ', palavra_formada)
    print('Tentativas: ', tentativas)
    
    if palavra_secreta == palavra_formada:
        print('VOCE GANHOU !!!')
        print('Palavra secreta era: ', palavra_secreta)
        tentativas = 0
        palavra_secreta = 'presente'
        letras_acertadas = ''
        os.system('cls')