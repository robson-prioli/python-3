def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'bom dia', 'luiz')
print(v)