import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterable = iter(iterable)

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000)) # n esta na memoria, n tem indice; n sabe o tamanho

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))