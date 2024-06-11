class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('João', 31)


print(p1.__dict__)
print(vars(p1))

dados = p1.__dict__
p2 = Pessoa(**dados)

print()
print(p2.__dict__)
print(vars(p2))

p1.__dict__['sobrenome'] = 'Silva'
print()

print(p1.__dict__)
print(vars(p1))

p1.__dict__['sobrenome'] = 'Silva'
