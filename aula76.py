import copy

pessoa = {}

pessoa['nome'] = 'Robson'

if pessoa.get('sobrenome') is None:
    print('Chave n existe')


pessoa = {
    'nome': 'Robson',
    'sobrenome': 'Miranda'
}

print(len(pessoa))
print(tuple(pessoa.keys()))
print(list(pessoa.keys()))

print(list(pessoa.values()))


d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = d1.copy() # copy rasa, ou seja, n copia o l1, aponta para o mesmo

d2 = copy.deepcopy(d1) # copia pronfuda