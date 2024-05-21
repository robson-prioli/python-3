nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2)

nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1)

_, nome2, *resto = ['Maria', 'Helena', 'Luiz']
print(nome2)