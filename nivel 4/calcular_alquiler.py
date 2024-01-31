# 3. Real State Rent System 


# A real estate agency has 5 homes for rent. The homes are characterized by their size, number of bedrooms, number of bathrooms, and location. The rental price of a home is calculated based on these factors.
# Features:

# First home: 200 square meters, 3 bedrooms, 2 bathrooms
# Second home: 150 square meters, 2 bedrooms, 2 bathrooms
# Third home: 100 square meters, 2 bedrooms, 1 bathroom
# Fourth home: 100 square meters, 1 bedroom, 2 bathrooms
# Fifth home: 80 square meters, 1 bedroom, 1 bathroom
# The program must quote the price of the home according to: square meters, number of bedrooms, and number of bathrooms. Each bedroom adds $40, and each bathroom adds $30. Each square meter has a cost of $90.

class Inmobiliaria:
    def __init__(self):
        self.casas = {
            "First home": {"square meters": 200, "bedrooms": 3, "bathrooms": 2},
            "Second home": {"square meters": 150, "bedrooms": 2, "bathrooms": 2},
            "Third home": {"square meters": 100, "bedrooms": 2, "bathrooms": 1},
            "Fourth home": {"square meters": 100, "bedrooms": 1, "bathrooms": 2},
            "Fifth home": {"square meters": 80, "bedrooms": 1, "bathrooms": 1}
        }

        self.precios = {"square meters": 90, "bedrooms": 40, "bathrooms": 30}

    def calcular_valor(self):
        for nombre, detalles in self.casas.items():
            precio_casa = 0
            precio_casa += detalles["square meters"] * self.precios["square meters"]
            precio_casa += detalles["bedrooms"] * self.precios["bedrooms"]
            precio_casa += detalles["bathrooms"] * self.precios["bathrooms"]

            detalles["precio total"] = precio_casa

    def imprimir(self):
        for index, (nombre, detalles) in enumerate(self.casas.items(), start=1):
            print(f"Casa {index}: {nombre}")
            print("Detalles:")
            for caracteristica, valor in detalles.items():
                print(f"  {caracteristica}: {valor}")
            print("\n")


prueba = Inmobiliaria()
prueba.calcular_valor()
prueba.imprimir()
