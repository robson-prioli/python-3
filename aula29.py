
numero_str = input('Vou dobrar o numero que vc digitar:')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
except:
    print('Isso n é um numero')
