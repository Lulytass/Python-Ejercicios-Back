# 2. Amazon Software Engineer 

# Amazon has hired you as a software engineer. Your first task is to create a system that allows calculating the price of shipping based on distance. Fulfill the following requirements:
# Amazon has one branch in each state of the USA.
# Research the approximate distance between each pair of states.
# The price is $50 USD per kilometer.
# The minimum number of packages to transport is 100, and the maximum is 500.
# If the number of packages exceeds 200, a larger vehicle should be recommended, with a price of $60 USD per kilometer.
# Based on the distance, the system should calculate an estimated delivery time.

from geopy.distance import geodesic

class Distancias_estados:
    def __init__(self):
        self.estados_ubicacion = {
            "Alabama": (32.7794, 86.8287),
            "Alaska": (64.0685, 152.2782),
            "Arizona": (34.2744, 111.6602),
            "Arkansas": (34.8938, 92.4426),
            "California": (37.1841, 119.4696),
            "Colorado": (38.9972, 105.5478),
            "Connecticut": (41.6219, 72.7273),
            "Delaware": (38.9896, 75.5050),
            "District of Columbia": (38.9101, 77.0147),
            "Florida": (28.6305, 82.4497),
            "Georgia": (32.6415, 83.4426),
            "Hawaii": (20.2927, 156.3737),
            "Idaho": (44.3509, 114.6130),
            "Illinois": (40.0417, 89.1965),
            "Indiana": (39.8942, 86.2816),
            "Iowa": (42.0751, 93.4960),
            "Kansas": (38.4937, 98.3804),
            "Kentucky": (37.5347, 85.3021),
            "Louisiana": (31.0689, 91.9968),
            "Maine": (45.3695, 69.2428),
            "Maryland": (39.0550, 76.7909),
            "Massachusetts": (42.2596, 71.8083),
            "Michigan": (44.3467, 85.4102),
            "Minnesota": (46.2807, 94.3053),
            "Mississippi": (32.7364, 89.6678),
            "Missouri": (38.3566, 92.4580),
            "Montana": (47.0527, 109.6333),
            "Nebraska": (41.5378, 99.7951),
            "Nevada": (39.3289, 116.6312),
            "New Hampshire": (43.6805, 71.5811),
            "New Jersey": (40.1907, 74.6728),
            "New Mexico": (34.4071, 106.1126),
            "New York":	(42.9538, 75.5268),
            "North Carolina": (35.5557, 79.3877),
            "North Dakota": (47.4501, 100.4659),
            "Ohio": (40.2862, 82.7937),
            "Oklahoma": (35.5889, 97.4943),
            "Oregon": (43.9336, 120.5583),
            "Pennsylvania": (40.8781, 77.7996),
            "Rhode Island": (41.6762, 71.5562),
            "South Carolina": (33.9169, 80.8964),
            "South Dakota": (44.4443, 100.2263),
            "Tennessee": (35.8580, 86.3505),
            "Texas": (31.4757, 99.3312),
            "Utah": (39.3055, 111.6703),
            "Vermont": (44.0687, 72.6658),
            "Virginia": (37.5215, 78.8537),
            "Washington": (47.3826, 120.4472),
            "West Virginia": (38.6409, 80.6227),
            "Wisconsin": (44.6243, 89.9941),
            "Wyoming": (42.9957, 107.5512),
        }
    
    def calcular_distancia(self, destino, local):
        return int(geodesic(destino, local).km)
    
    def calcular_mas_cercano(self, ubicacion):
        cerca = float('inf')
        nombre_estado = ""
        for estado, coordenadas in self.estados_ubicacion.items():
            distancia = int(geodesic(ubicacion, coordenadas).km)
            if distancia < cerca and coordenadas != ubicacion:
                cerca = distancia
                nombre_estado = estado
                cordenadas_mas_cerca = coordenadas
        print(f"\nEl envio se realizara desde {nombre_estado}, ya que es la sucursal mas cercana, esta a {cerca} Km.")
        return nombre_estado, cordenadas_mas_cerca


class Usuario:
    def __init__(self):
        self.ubicacion = None
        self.estados = Distancias_estados()

    def ubicacion_usuario(self):
        opciones = list(self.estados.estados_ubicacion.keys())

        print("Seleccione su estado:")
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")

        while True:
            try:
                seleccion = int(input(f"\nIngrese una opcion entre 1 - {len(opciones)}: "))
                if 1 <= seleccion <= len(opciones):
                    print(f"Buscaremos cual es el estado mas cercano a {opciones[seleccion - 1]} para realizar el envio desde allí")
                    return opciones[seleccion - 1]
                else:
                    print("\nSelección inválida. Asegúrese de elegir una dentro del rango.")
            except ValueError:
                print("\nPor favor, ingrese un valor válido.")

    def cantidad_paquetes_usuario(self):
        print("\nEl costo por kilometro variara dependiendo de la cantidad de paquetes")
        print(f'Hasta {Calculador_envios.precio_km["vehiculoChico"]["Bultos"][1]}: ${Calculador_envios.precio_km["vehiculoChico"]["precio"]} por paquete por precio por Km')
        print(f'Entre {Calculador_envios.precio_km["vehiculoGrande"]["Bultos"]}: ${Calculador_envios.precio_km["vehiculoGrande"]["precio"]} por paquete por precio por Km')
        while True:
            try:
                cantidad = int(input(f'\nIngrese la cantidad de paquetes que enviará ({Calculador_envios.cantidad_bultos["minimo"]} - {Calculador_envios.cantidad_bultos["maximo"]}): '))
                if Calculador_envios.cantidad_bultos["minimo"] <= cantidad <= Calculador_envios.cantidad_bultos["maximo"]:
                    return cantidad
                else:
                    print("\nCantidad inválida. Asegúrese de elegir una dentro del rango.")
            except ValueError:
                print("\nPor favor, ingrese un valor válido.")

            
class Calculador_envios:
    cantidad_bultos = {
        "minimo": 100,
        "maximo": 500
    }

    precio_km = {
        "vehiculoChico": {"precio": 50, "Bultos": (1, 200)},
        "vehiculoGrande": {"precio": 60, "Bultos": (201, 500)}
    }

    def precio_cantidad(self, cantidad, distancia):
        if cantidad <= self.precio_km["vehiculoChico"]["Bultos"][1]:
            precio = distancia * cantidad * self.precio_km["vehiculoChico"]["precio"]
        else:
            precio = distancia * cantidad * self.precio_km["vehiculoGrande"]["precio"]
        return precio
    
    def estimar_tiempo_entrega(self, distancia):
        tiempo_estimado = distancia // 100
        return max(tiempo_estimado, 1)  # Al menos 1 día de entrega


# Programa principal
usuario = Usuario()
usuario.ubicacion = usuario.ubicacion_usuario()
cantidad_paquetes = usuario.cantidad_paquetes_usuario()

prueba1 = Distancias_estados()
nombre, coor = prueba1.calcular_mas_cercano(prueba1.estados_ubicacion[usuario.ubicacion])



intento1 = Calculador_envios()
tiempo_estimado = intento1.estimar_tiempo_entrega(prueba1.calcular_distancia(prueba1.estados_ubicacion[usuario.ubicacion], coor))
costo_envio = intento1.precio_cantidad(cantidad_paquetes, prueba1.calcular_distancia(prueba1.estados_ubicacion[usuario.ubicacion], coor))
print(f"El envío de {cantidad_paquetes} paquetes a {nombre} tiene un costo de: ${costo_envio} y llegara en {tiempo_estimado}")
    
  


