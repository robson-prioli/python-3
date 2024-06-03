try:
    print('abrir arquivo')
    8/0
except ZeroDivisionError:
    print('dividiu por zero')
else:
    print('não deu erro')
finally:
    print('fechar arquivo')