from models.cardapio.item import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return super().__str__()
    
    def aplicar_desconto(self):
        self._preco = round(self._preco - self._preco * 0.08, 2)