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