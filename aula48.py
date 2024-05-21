

lista = [10, 20, 30, 40]

lista[2] = 300 # sobrecarga index
del lista[2] # deleta o segundo index
lista.append(50) # adc novo index com valor 50
lista.pop() # remove o ultimo index, da para salvar em uma variavel para ver qual foi o ultimo valor removido

lista.append(60)
ultimo_removido = lista.pop()

lista.insert(0, 'Luiz') # index e valor para ser inserido no index tipo updade