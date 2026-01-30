class Restaurante:
    restaurantes = []

    #método construtor
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    #caso necessite devolver como string
    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.ativo}"

    def listar_restaurante():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}")

pizzaria = Restaurante("Pizzaria", "Italiana")
hamburgueria = Restaurante("Hamburgueria", "Americano")

Restaurante.listar_restaurante()

