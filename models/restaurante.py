class Restaurante:
    restaurantes = []

    #método construtor
    #self refere-se ao objeto
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False #ao colocar _ antes do nome da propriedade, declaramos pro sistema que ela é protegida e em tese, não se deve mexer
        Restaurante.restaurantes.append(self)
    
    #caso necessite devolver como string
    def __str__(self):
        return f"{self.nome.center(20)} | {self.categoria.center(20)} | {self.ativo.center(20)}"

    @classmethod
    def listar_restaurante(cls): #cls refere-se a classe
        print(f"{"Nome do Restaurante".center(20)} | {"Categoria".center(20)} | {"Status".center(20)}")
        print("-" * 66)
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.center(20)} | {restaurante._categoria.center(20)} | {restaurante.ativo.center(20)}")

    @property
    def ativo(self):
        return "Ativado" if self._ativo else "Desativado"

    def alternar_estado(self):
        self._ativo = not self._ativo



pizzaria = Restaurante("Pizzaria", "Italiana")
hamburgueria = Restaurante("Hamburgueria", "Americano")

pizzaria.alternar_estado()

Restaurante.listar_restaurante()

