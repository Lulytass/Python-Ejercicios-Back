# 5. British Airplanes Startup 

# A British start-up specializing in the manufacturing of high-security, high-speed aircraft seeks to calculate the prices of its planes based on the following characteristics: Aircraft size, VIP seats, economy class seats, material quality, security system, and speed level.
# Currently, it offers 3 types of aircraft ready for sale.

# Wayne Rooney Plane:
# Quality AAA
# 200 economy class seats
# 70 VIP seats
# 90 square meters
# Security system AAA
# Speed level AAA

# Eric Cantona Plane:
# Quality AAA
# 150 economy class seats
# 80 VIP seats
# 110 square meters
# Security system AAA
# Speed level AA

# Bobby Charlton Plane:
# Quality AA
# 100 economy class seats
# 40 VIP seats
# 120 square meters
# Security system AA
# Speed level A

# The AAA material costs £60,000.
# The AA material costs £54,000.
# The A material costs £48,000.

# The AAA security system costs £75,000.
# The AA security system costs £68,000.
# The A security system costs £59,000.

# The AAA speed level costs £89,000.
# The AA speed level costs £78,000.
# The A speed level costs £70,000.

# In the Wayne Rooney and Eric Cantona planes, each economy class seat costs £400, and each VIP seat costs £1200.

# In the Bobby Charlton plane, each economy class seat costs £300, and each VIP seat costs £1000.

class Aviones:
    def __init__(self):
        self.aviones_caracteristicas = {
            "Wayne Rooney": {"Quality": "AAA", "economy class seats": 200, "VIP seats": 70, "square meters": 90, "Security system": "AAA", "Speed level": "AAA"},
            "Eric Cantona": {"Quality": "AAA", "economy class seats": 150, "VIP seats": 80, "square meters": 110, "Security system": "AAA", "Speed level": "AA"},
            "Bobby Charlton": {"Quality": "AA", "economy class seats": 100, "VIP seats": 40, "square meters": 120, "Security system": "AA", "Speed level": "A"},
        }
        self.precios = {
            "material": {"AAA": 60000, "AA": 54000, "A": 48000},
            "security system": {"AAA": 75000, "AA": 68000, "A": 59000},
            "speed level": {"AAA": 89000, "AA": 75000, "A": 70000},
            "square meters": {"Wayne Rooney": 1200, "Eric Cantona": 2000,"Bobby Charlton": 1500},
            "economy class seat" : {
                "Wayne Rooney": {"economy": 400, "VIP": 1200},
                "Eric Cantona": {"economy": 400, "VIP": 1200},
                "Bobby Charlton": {"economy": 300, "VIP": 1000}

            }
        }

    def calculador_precio_avion(self):
        for nombre, detalles in self.aviones_caracteristicas.items():
            precio_avion = 0
            # se calcula el precio por los asientos, segun cantidad y categoria 
            precio_avion += detalles["economy class seats"] * self.precios["economy class seat"][nombre]["economy"]
            precio_avion += detalles["VIP seats"] * self.precios["economy class seat"][nombre]["VIP"]
            # se calcula el precio segun los metros
            precio_avion += detalles["square meters"] * self.precios["square meters"][nombre]
            # calculamos precio segun calidad de materiales
            precio_avion += self.precios["material"][detalles["Quality"]]
            # calculamos precio segun sistema de seguridad
            precio_avion += self.precios["security system"][detalles["Security system"]]
            # calculamos precio segun nivel de velocidad
            precio_avion += self.precios["speed level"][detalles["Speed level"]]


            # agregamos el dato con el precio total por el avion
            detalles["precio total"] = precio_avion

    def imprimir(self):
        for index, (nombre, detalles) in enumerate(self.aviones_caracteristicas.items(), start=1):
            print(f"Avion {index}: {nombre}")
            print("Detalles:")
            for caracteristica, valor in detalles.items():
                print(f"  {caracteristica}: {valor}")
            print("\n")


prueba = Aviones()
prueba.calculador_precio_avion()
prueba.imprimir()
