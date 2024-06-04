from itertools import zip_longest

def zipper(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))

    return [
        (lista1[i], lista2[i]) for i in range(intervalo)
    ]
    

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1, l2))
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='Sem cidade')))


lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x,y in zip(lista_a, lista_b)]
print(lista_soma)