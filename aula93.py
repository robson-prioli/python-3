try:
    a = 18
    b = 2
    c = a / b
    print('Olá'[10])
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido.')
except (SyntaxError, TypeError, IndexError) as error:
    print(f'msg: {error}, class: {error.__class__.__name__}')
except Exception:
    print('Erro desconhecido.')

print('continuou..')