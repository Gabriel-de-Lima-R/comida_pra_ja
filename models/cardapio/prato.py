from models.cardapio.item import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
    
    def __str__(self):
        return super().__str__()
    
    def aplicar_desconto(self):
        self._preco = round(self._preco - self._preco * 0.05, 2)
