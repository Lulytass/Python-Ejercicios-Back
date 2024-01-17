# 4. The RH Hotels chain has hired you to design the booking algorithm for their mobile application:

# Login; it should be locked after the third failed attempt.
# The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
# Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome, Milan, Paris, Marseille, Madeira, Lisbon, and Porto.
# All hotels have 24 rooms each: 6 VIP suites, 3 single rooms, 6 double rooms, 6 group rooms, and 3 luxury suites.
# The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
# Single rooms are priced at $100 per night, double rooms at $200 per night, group rooms at $350 per night, VIP suites at $450 per night, and luxury suites at $550 per night, applicable at any time of the year.
# The algorithm functions as follows: Login, choose country, choose city, choose room type, select the number of nights, collect user data (name, surname, ID/passport), 
# print the total cost, and if the user agrees, print a confirmation message for the reservation. If not, return to the main menu.
from datetime import datetime
import re

class Huesped:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.pasaporte = ""
        self.fecha_entrada = ""
        self.fecha_salida =  ""

    def __str__(self):
        return (f"\nNombre: {self.nombre}\nApellido: {self.apellido}\nPasaporte: {self.pasaporte}")
    
class Reserva:
    def __init__(self): 
        self.attempts = 3
        self.reservas = []
        self.precios = {
            "Individuales": 100,
            "Dobles": 200,
            "Grupal": 350,
            "suites VIP": 450,
            "Suites de lujo": 550
        }
        self.paises = {
            "España":{
                "Madrid":{"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}, 
                "Barcelona": {"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}, 
                "Valencia": {"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}
            }, 
            "Francia":{
                 "París": {"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}, 
                 "Marsella": {"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}
            }, 
            "Portugal":{
                  "Madeira": {"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}, 
                  "Lisboa": {"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}, 
                  "Oporto": {"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}
            }, 
            "Italia":{
                   "Roma": {"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}, 
                   "Milán": {"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}
            }, 
            "Alemania":{
                       "Munich": {"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}, 
                       "Berlín": {"suites VIP": 6 , "Individuales": 3, "Dobles": 6, "Grupal": 6, "Suites de lujo": 3}
            }
        }
    
    def login(self):
        usuario_correcto = "reserva"
        password_correcto = "reserva"

        while self.attempts > 0:
            usuario = input("Ingrese su usuario: ").strip()
            contrasena = input("Ingrese su contraseña: ").strip()

            if usuario == usuario_correcto and contrasena == password_correcto:
                self.reserva()  
                break
            else:
                self.attempts -= 1
                print(f"Credenciales incorrectas. Intentos restantes: {self.attempts}")

            if self.attempts == 0:
                print("Has alcanzado el número máximo de intentos. Se bloqueará el acceso.")

    def menu_paises(self):
        print("\nPaises donde se encuentran nuestros hoteles")
        for i, pais in enumerate(self.paises.keys(), start=1):
            print(f"{i}. {pais}")

        while True:
            try:
                opcion_pais = int(input(f"Seleccione un país (1-{len(self.paises)}): "))
                if 1 <= opcion_pais <= len(self.paises):
                    pais_seleccionado = list(self.paises.keys())[opcion_pais - 1]
                    return pais_seleccionado
                else:
                    print("Selección inválida. Asegúrese de elegir un país dentro del rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def menu_ciudades(self, pais):
        ciudades_disponibles = self.paises.get(pais, {})
        
        if not ciudades_disponibles:
            print("No hay ciudades disponibles para el país seleccionado.")
            return None

        print(f"\nCiudades Disponibles en {pais}:")
        for i, ciudad in enumerate(ciudades_disponibles.keys(), start=1):
            print(f"{i}. {ciudad}")

        while True:
            try:
                opcion_ciudad = int(input("Seleccione una ciudad (1-{0}): ".format(len(ciudades_disponibles))))
                if 1 <= opcion_ciudad <= len(ciudades_disponibles):
                    ciudad_seleccionada = list(ciudades_disponibles.keys())[opcion_ciudad - 1]
                    return ciudad_seleccionada
                else:
                    print("Selección inválida. Asegúrese de elegir una ciudad dentro del rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def menu_habitacion(self, pais, ubicacion):
        ciudades_disponibles = self.paises.get(pais, {})
        
        if not ciudades_disponibles:
            print(f"No hay información disponible para {ubicacion}.")
            return None

        habitaciones_disponibles = {habitacion: cantidad for habitacion, cantidad in ciudades_disponibles.get(ubicacion, {}).items() if cantidad > 0}

        if not habitaciones_disponibles:
            print(f"No hay habitaciones disponibles en {ubicacion}.")
            return None

        print("\nTipos de habitaciones disponibles:")
        for i, (habitacion, cantidad) in enumerate(habitaciones_disponibles.items(), start=1):
            print(f"{i}. {habitacion} ({cantidad} disponibles)")

        while True:
            try:
                opcion = int(input(f"Seleccione el tipo de habitación (1-{len(habitaciones_disponibles)}): "))
                if 1 <= opcion <= len(habitaciones_disponibles):
                    seleccionada = list(habitaciones_disponibles.keys())[opcion - 1]
                    return seleccionada
                else:
                    print("Selección inválida. Por favor, elija un tipo de habitación disponible.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def obtener_precio(self, tipo_habitacion):
        return self.precios.get(tipo_habitacion, 0)

    def validar_nombre_Apellido(self, dato):
        return bool(re.match("^[a-zA-Z ]+$", dato))

    def validar_pasaporte(self, pasaporte):
        return len(pasaporte) == 9 and pasaporte.isalnum()

    def pedir_datos(self, reserva):
        while True:
            nombre = input("\nIngrese su nombre: ").strip()
            if self.validar_nombre_Apellido(nombre):
                reserva.nombre = nombre
                break
            else:
                print("\nNombre inválido. Asegúrese de ingresar solo letras y espacios.")

        while True:
            apellido = input("\nIngrese su pellido: ").strip()
            if self.validar_nombre_Apellido(apellido):
                reserva.apellido = apellido
                break
            else:
                print("\nApellido inválido. Asegúrese de ingresar solo letras y espacios.")

        while True:
            pasaporte = input("\nIngrese su número de pasaporte: ").strip()
            if self.validar_pasaporte(pasaporte):
                reserva.pasaporte = pasaporte
                break
            else:
                print("\nNúmero de pasaporte inválido. Asegúrese de que tenga 9 caracteres alfanuméricos.")

    def pedir_fecha(self):
        while True:
            fecha = input("Ingrese la fecha (DD/MM/YYYY): ").strip()
            try:
                fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
                if fecha_dt >= datetime.now():
                    return fecha
                else:
                    print("\nLa fecha debe ser igual o posterior a la fecha actual. Intente nuevamente.")
            except ValueError:
                print("\nFormato de fecha incorrecto. Por favor, ingrese la fecha en el formato correcto (DD/MM/YYYY).")

    def pedir_fechas(self, reserva):
        print("\nDebera ingresar la fecha de entrada")
        reserva.fecha_entrada = self.pedir_fecha()
        
        while True:
            print("\nAhora debera ingresar la fecha de la salida")
            reserva.fecha_salida = self.pedir_fecha()
            fecha_entrada = datetime.strptime(reserva.fecha_entrada, "%d/%m/%Y")
            fecha_salida = datetime.strptime(reserva.fecha_salida, "%d/%m/%Y")
            
            if fecha_salida > fecha_entrada:
                break
            else:
                print("\nLa fecha de salida debe ser posterior a la fecha de entrada. Intente nuevamente.")

    def calcular_dias_estadia(self, fecha_entrada, fecha_salida):
        fecha_entrada_dt = datetime.strptime(fecha_entrada, "%d/%m/%Y")
        fecha_salida_dt = datetime.strptime(fecha_salida, "%d/%m/%Y")
        dias_estadia = (fecha_salida_dt - fecha_entrada_dt).days
        return dias_estadia
    
    def calcular_precio_estadia(self, precio_habitacion, dias):
        # Calcular el precio total de la estadía
        return precio_habitacion * dias

    def mostrar_reservas(self):
        print("\nReservas realizadas:")
        for i, reserva in enumerate(self.reservas, start=1):
            print(f"\nReserva {i}:")
            for key, value in reserva.items():
                print(f"{key}: {value}")
        
    def restar_habitacion(self, pais, ciudad, tipo_habitacion):
        if pais in self.paises and ciudad in self.paises[pais]:
            habitaciones_disponibles = self.paises[pais][ciudad]
            if tipo_habitacion in habitaciones_disponibles and habitaciones_disponibles[tipo_habitacion] > 0:
                habitaciones_disponibles[tipo_habitacion] -= 1
                print(f"\nSe ha reservado una habitación {tipo_habitacion} en {ciudad}, {pais}.")

    def reserva(self):
        while True:
            datos = Huesped()
            pais = self.menu_paises()
            ciudad = self.menu_ciudades(pais)
            tipo_habitacion = self.menu_habitacion(pais, ciudad)
            self.pedir_fechas(datos)
            precio = self.calcular_precio_estadia(self.obtener_precio(tipo_habitacion), self.calcular_dias_estadia(datos.fecha_entrada,datos.fecha_salida))
            self.pedir_datos(datos)


            reserva = {
                "Nombre": datos.nombre,
                "Apellido": datos.apellido,
                "Pasaporte": datos.pasaporte,
                "Ciudad": ciudad,
                "Tipo de Habitacion": tipo_habitacion,
                "Precio": precio
            }

            while True:
                confirmacion = input(f"\nEl costo de la estadia es: ${precio}\n¿Desea confirmar la reserva? (SI/NO): ").strip().upper()
                if confirmacion == "SI":
                    self.reservas.append(reserva)
                    self.restar_habitacion(pais, ciudad, tipo_habitacion)
                elif confirmacion == "NO":
                    print("\nReserva cancelada.")  
                else:
                    print("\nEntrada inválida. Por favor, ingrese SI o NO.")
                    continue
                volver = input("\nSi desea relizar otra reserva ingrese SI, pasara salir cualquier tecla: ").strip().upper()
                if volver == "SI":
                    break 
                else:
                    self.mostrar_reservas()
                    print("\nSaliendo del programa. ¡Gracias por visitar RH Hotels!")
                    exit() 

        
hotel = Reserva()
hotel.login()