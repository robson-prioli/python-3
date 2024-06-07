import os

caminho = 'aula116.txt'

with open(caminho, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

with open(caminho, 'r') as arquivo:
    print(arquivo.read())


#os.remove(caminho)
#os.unlink(caminho)
#os.rename(caminho, 'newname')