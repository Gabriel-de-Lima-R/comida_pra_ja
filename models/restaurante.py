from models.avaliacao import Avaliacao
from models.cardapio.item import ItemCardapio

class Restaurante:
    restaurantes = []

    #método construtor
    #self refere-se ao objeto
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False #ao colocar _ antes do nome da propriedade, declaramos pro sistema que ela é protegida e em tese, não se deve mexer
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    #caso necessite devolver como string
    def __str__(self):
        return f"{self.nome.center(20)} | {self.categoria.center(20)} | {self.ativo.center(20)}"

    @classmethod
    def listar_restaurante(cls): #cls refere-se a classe
        print(f"{"Nome do Restaurante".center(20)} | {"Categoria".center(20)} | {"Avaliação".center(20)} | {"Status".center(20)}")
        print("-" * 89)
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.center(20)} | {restaurante._categoria.center(20)} | {str(restaurante.media_avaliacao).center(20)} | {restaurante.ativo.center(20)}")

    @property
    def ativo(self):
        return "Ativado" if self._ativo else "Desativado"

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            nova_avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(nova_avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return "-"
        
        somas_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(somas_notas / quantidade_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
        else:
            print("Precisa ser um item válido para adicionar ao cardápio, se não existir, crie um novo item!")

    @property
    def mostre_cardapio(self):
        print(f"Cardápio do restaurante {self._nome}:")
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, "_descricao"):
                msg = f"{i}. Nome: {item._nome} | Preço ${item._preco} | Descrição: {item._descricao}"
            else:
                msg = f"{i}. Nome: {item._nome} | Preço ${item._preco} | Tamanho: {item._tamanho}"
            print(msg)
