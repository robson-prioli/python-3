"""
"""

CPF = '746.824.890-70'


cpf_split = CPF.split('-')[0].replace('.', '')

valor_final = 0
valores_multicapor = [10, 9, 8, 7, 6, 5, 4, 3, 2]
digitos = []

# primeiro digito
for i, valor in enumerate(cpf_split):
    valor_final += int(valor) * valores_multicapor[i]

    if i == 8:
       valor_final *= 10
       digitos.append(0 if valor_final % 11 > 9 else valor_final % 11) 


valor_final = 0
valores_multicapor = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
cpf_split =  cpf_split + '' + str(digitos[0])
# segundo digito
for i, valor in enumerate(cpf_split):
    valor_final += int(valor) * valores_multicapor[i]

    if i == 9:
       valor_final *= 10
       digitos.append(0 if valor_final % 11 > 9 else valor_final % 11) 

print(digitos)