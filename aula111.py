from functools import partial


def print_iter(i):
    print(*list(i), sep='\n')
    print()


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

def mudar_preco(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novos_produtos = [
    {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
]

map_produtos = map(mudar_preco, produtos)

print_iter(produtos)
print_iter(novos_produtos)
print_iter(map_produtos)

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4, 5]
    ))
)