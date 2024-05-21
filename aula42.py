# \ usada para quebrar linha
frase = 'O Python é uma linguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'

i = 0
mais_vezes = 0
letra_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if mais_vezes < quantas_vezes_letra_apareceu:
        letra_mais_vezes = letra_atual
        mais_vezes = quantas_vezes_letra_apareceu

    print(letra_atual, quantas_vezes_letra_apareceu)
    i += 1

print(f'A {letra_mais_vezes} apareceu {mais_vezes}')
