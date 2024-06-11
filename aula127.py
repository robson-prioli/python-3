import json

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def salvar(self, dados):
        if self.nome is not None and self.idade is not None:
            
            with open('aula127.json', 'w', encoding='utf8') as arquivo:
                print(f'dados: {dados}')
                json.dump(dados, arquivo, indent=2)
            
            print(f'Os dados de pessoa foram salvos.')
            return
        
        print(f'Não há dados para serem salvos.')
    

    def carregar(self):
        with open('aula127.json', 'r', encoding='utf8') as arquivo:
            pessoa = json.load(arquivo)
            self.nome = pessoa['nome']
            self.idade = pessoa['idade']

        print(f'Dados carregados com sucesso.')
        


p1 = Pessoa('Lucas', 25)
print(vars(p1))
p1.salvar(p1.__dict__)

p1.carregar()


