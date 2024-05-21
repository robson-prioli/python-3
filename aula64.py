import random

for _ in range(100):
    novedigitos = ''
    for i in range(9):
        novedigitos += str(random.randint(0, 9)) 

    digito1 = 0
    contador = 10
    for digito in novedigitos:
        digito1  += int(digito) * contador
        contador -= 1

    digito1 = (digito1 * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0

    dezdigitos = novedigitos + str(digito1) 

    digito2 = 0
    contador = 11
    for digito in dezdigitos:
        digito2  += int(digito) * contador
        contador -= 1

    digito2 = (digito2 * 10) % 11
    digito2 = digito2 if digito2 <= 9 else 0

    cpf_valido = dezdigitos + str(digito2)

    print(cpf_valido)