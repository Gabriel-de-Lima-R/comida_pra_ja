from models.restaurante import Restaurante

pizzaria = Restaurante("pizzaria", "Italiana")
hamburgueria = Restaurante("Hamburgueria", "Americano")
taco_land = Restaurante("Taco Land", "Mexicano")
sujinho = Restaurante("Sujinho", "Japonês")

pizzaria.receber_avaliacao("Lucas", 3)
pizzaria.receber_avaliacao("Lucas", 1.5)
pizzaria.receber_avaliacao("Lucas", 5)
hamburgueria.receber_avaliacao("Jonas", 2)

def main():
    pizzaria.alternar_estado()
    Restaurante.listar_restaurante()

if __name__ == "__main__":
    main()