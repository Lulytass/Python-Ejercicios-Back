# 5. Turkish Airlines has just launched an offer to travel among the following destinations: Turkey, Greece, Lebanon, Spain, and Portugal. Develop an algorithm with the following characteristics:
# It must have a login and validate the data; after the third failed attempt, it should be locked.
# The user must choose the origin country and the destination country, the flight date, and the condition: Economy or First Class.
# The user must choose if they want to check an additional piece of luggage into the hold.
# Hand luggage is free of charge.
# The user must purchase both the outbound and return tickets.
# The user can choose their preferred meal: Regular, Vegetarian, Kosher.
# The program must collect the following data: Name, country of origin, passport, and destination country.
# Upon completing the process, the system will display everything the user has previously chosen along with their information. 
# The system will provide the option to confirm the reservation or cancel it. If the user chooses YES, a confirmation message will appear. If not, it will return to the main menu.
from datetime import datetime
import re
class Pasaje:
    def __init__(self):
        self.nombre = ""
        self.origen = ""
        self.destino = ""
        self.pasaporte = ""
        self.comida = ""
        self.fecha_ida = ""
        self.fecha_vuelta = ""
        self.condicion = ""
        self.equipaje_bodega = 0

    def __str__(self):
        return (f"\nNombre: {self.nombre}\nPasaporte: {self.pasaporte}\nOrigen: {self.origen}\nDestino: {self.destino}\nFecha Salida: {self.fecha_ida}\nFecha Vuelta: {self.fecha_vuelta}\nClase: {self.condicion}\nComida de preferencia durante el vuelo: {self.comida}\nEquipaje en bodega: {self.equipaje_bodega}")

class Vuelo:
    def __init__(self):
        self.attempts = 3

    def opciones_paises(self, pasaje):
        destinos = ["Turquía", "Grecia", "Líbano", "España", "Portugal"]

        print("\nDestinos Disponibles:\n")
        for i, destino in enumerate(destinos, start=1):
            print(f"{i}. {destino}")

        while True:
            try:
                opcion_origen = int(input("Seleccione el país de origen (1-5): "))
                opcion_destino = int(input("Seleccione el país de destino (1-5): "))
                if 1 <= opcion_origen <= 5 and 1 <= opcion_destino <= 5 and opcion_origen != opcion_destino:
                    pasaje.origen = destinos[opcion_origen - 1]
                    pasaje.destino = destinos[opcion_destino - 1]
                    break
                else:
                    print("\nSelección inválida. Asegúrese de elegir destinos diferentes y dentro del rango.")
            except ValueError:
                print("\nPor favor, ingrese un número válido.")

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

    def pedir_clase(self, pasaje):
        categorias = ["Turista", "Primera Clase"]

        print("\nCategorias Disponibles:")
        for i, categoria in enumerate(categorias, start=1):
            print(f"{i}. {categoria}")

        while True:
            try:
                opcion_categoria = int(input("Seleccione La categoria (1-2): "))
                if 1 <= opcion_categoria <= 2:
                    pasaje.condicion = categorias[opcion_categoria - 1]
                    break
                else:
                    print("\nSelección inválida. Asegúrese de elegir una categoria dentro del rango.")
            except ValueError:
                print("\nPor favor, ingrese un número válido.")

    def seleccion_comida(self, pasaje):
        comidas = ["Regular", "Vegetariana", "Kosher"]

        print("\nSeleccione el tipo de comida:")
        for i, comida in enumerate(comidas, start=1):
            print(f"{i}. {comida}")

        while True:
            try:
                opcion_comida = int(input("Seleccione La Comida (1-3): "))
                if 1 <= opcion_comida <= 3:
                    pasaje.comida = comidas[opcion_comida - 1]
                    break
                else:
                    print("Selección inválida. Asegúrese de elegir una comida dentro del rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def pedir_fechas(self, pasaje):
        print("\nDebera ingresar los datos del pasaje de ida")
        pasaje.fecha_ida = self.pedir_fecha()
        
        while True:
            print("\nAhora debera ingresar los datos del pasaje de vuelta")
            pasaje.fecha_vuelta = self.pedir_fecha()
            fecha_salida = datetime.strptime(pasaje.fecha_ida, "%d/%m/%Y")
            fecha_vuelta = datetime.strptime(pasaje.fecha_vuelta, "%d/%m/%Y")
            
            if fecha_vuelta > fecha_salida:
                break
            else:
                print("\nLa fecha de vuelta debe ser posterior a la fecha de salida. Intente nuevamente.")


    def equipaje(self,pasaje):
            print("\nEl equipaje que se despacha tiene un costo adicional y no se pueden despachar mas de 10 valijas")
            confirmar = input("Desea despachar equipaje? (SI/NO): ").strip().upper()
            if confirmar == "SI":
                while True:
                    try:
                        cantidad = int(input("\nCuantas piezas de equipaje desea despachar: "))
                        if 1 <= cantidad <= 10:
                            pasaje.equipaje_bodega = cantidad
                            break
                        else:
                            print("\nSelección inválida. Asegúrese de elegir una cantidad dentro del rango.")
                    except ValueError:
                        print("\nPor favor, ingrese un número válido.")
                
    def validar_nombre(self, nombre):
        return bool(re.match("^[a-zA-Z ]+$", nombre))

    def validar_pasaporte(self, pasaporte):
        return len(pasaporte) == 9 and pasaporte.isalnum()

    def pedir_nombre_y_pasaporte(self, pasaje):
        while True:
            nombre = input("\nIngrese su nombre: ").strip()
            if self.validar_nombre(nombre):
                pasaje.nombre = nombre
                break
            else:
                print("\nNombre inválido. Asegúrese de ingresar solo letras y espacios.")

        while True:
            pasaporte = input("\nIngrese su número de pasaporte: ").strip()
            if self.validar_pasaporte(pasaporte):
                pasaje.pasaporte = pasaporte
                break
            else:
                print("\nNúmero de pasaporte inválido. Asegúrese de que tenga 9 caracteres alfanuméricos.")

    def realizar_reserva(self):
        while True:
            pasaje = Pasaje()
            self.opciones_paises(pasaje)
            self.pedir_fechas(pasaje)
            self.pedir_clase(pasaje)
            self.seleccion_comida(pasaje)
            self.equipaje(pasaje)
            self.pedir_nombre_y_pasaporte(pasaje)

            print("\nResumen de la Reserva:\n")
            print(str(pasaje))
            print("----------------------------")

            confirmar = input("\n¿Desea confirmar la reserva? (SI/NO): ").strip().upper()
            if confirmar == "SI":
                print("=======¡Reserva confirmada! ¡Buen viaje!=======\n")
            else:
                print("Reserva cancelada.")

            continuar = input("¿Desea realizar otra reserva? (SI/NO): ").strip().upper()
            if continuar != "SI":
                print("Saliendo del programa.")
                break

            
        

    def login(self):
        usuario_correcto = "vuelo"
        password_correcto = "vuelo"

        while self.attempts > 0:
            usuario = input("Ingrese su usuario: ").strip()
            contrasena = input("Ingrese su contraseña: ").strip()

            if usuario == usuario_correcto and contrasena == password_correcto:
                self.realizar_reserva()  
                break
            else:
                self.attempts -= 1
                print(f"Credenciales incorrectas. Intentos restantes: {self.attempts}")

            if self.attempts == 0:
                print("Has alcanzado el número máximo de intentos. Se bloqueará el acceso.")



vuelo_instance = Vuelo()
vuelo_instance.login()