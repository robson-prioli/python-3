
def isInteger(n):
    tipo = type(n)

    if not isinstance(n, (int)):
        raise TypeError(
            f'{n} deve ser int, '
            f'{tipo.__name__} enviado.'
        )


print(isInteger(1.2))
print(123)
raise ValueError('Error')
print(456)