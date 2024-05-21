
lista_opcao = ['i', 'a', 'l']
lista_final = []

while True:

    opcao_selecionada = input('Selecione uma opção: [i]nserir [a]pagar [l]istar:').lower()

    # verifica a opcao
    if len(opcao_selecionada) > 1:
        print('Digite somente 1 letra.')
        continue

    if opcao_selecionada not in lista_opcao:
        print('Opção invalida.')
        continue    

    if opcao_selecionada == 'i':
        inserir = input('Digite o que quer inserir na lista:')

        if not inserir:
            print('Nada foi adicionado a sua lista.')
            continue

        lista_final.append(inserir)
        continue

    if opcao_selecionada == 'a':
        delete = input('Digite o indece que quer remover da lista:')

        if delete.isdigit():
            indice_delete = int(delete)

            if indice_delete > len(lista_final):
                print('Indece invalido.')
                continue

            del lista_final[indice_delete]
            continue
        else:
            print('Somante numeros.')

    if opcao_selecionada == 'l':
        print('Lista de compras:')
        for i, valor in enumerate(lista_final):
            print(i, valor)
        continue
