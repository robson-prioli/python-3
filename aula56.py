frase = 'Olha só que, coisa interessante'
lista_frases = frase.split(',')

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip()) # rstrip - remove os espaco da direita | lstrip - remove os espaco da esquerda | strip - remove dos dois lados

print(lista_frases)