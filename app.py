from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

pizzaria = Restaurante("pizzaria", "Italiana")
pizzaria.receber_avaliacao("Lucas", 3)
pizzaria.receber_avaliacao("Lucas", 1.5)
pizzaria.receber_avaliacao("Lucas", 5)


skol = Bebida("Cerveja", 5.0, "grande")
pao = Prato("Pão", 3.99, "melhor pão da cidade")

def main():
    print(skol)
    print(pao)


if __name__ == "__main__":
    main()