

def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6


g1 = gen2(gen1)
for numero in g1:
    print(numero)