
def multipleArgs(*args):

    total = 1
    for num in args:
        total *= num

    return total 

def isPar(num):
    return 'ímpar' if num % 2 > 0 else 'par'


print(multipleArgs(2, 4, 6))
print(isPar(2))