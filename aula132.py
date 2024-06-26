class Caneta:
    def __init__(self, cor):
        self.cor = cor #private or protected

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        if valor == 'Verde':
            raise ValueError('Cor invalida')
        
        self._cor = valor

caneta = Caneta('Azul')
caneta.cor = 'Pink'
print(caneta.cor)