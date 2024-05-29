# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:

    if isinstance(item, set):
        item.add(5)
        print('set - ', item, isinstance(item, set))
    
    if isinstance(item, str):
        print('str - ', item.upper())
    
    if isinstance(item, (int, float)):
        print('num - ', item, item * 2)