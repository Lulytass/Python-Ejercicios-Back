# 4. Old Trafford Stadium

# The executive management of Manchester United FC aims to implement a ticket sales system for the team's matches at Old Trafford Stadium. Develop a ticket purchase system with the following features:

# Membership Discount:
# Users with a Manchester United membership card receive a 15% discount on their total purchase.
# Seating Capacity and Distribution:
# The total seating capacity at Old Trafford is 74,310.
# 5% for VIP boxes, 15% for VIP seats, and 80% for general seating.
# Seat Selection:
# Seats are identified by a ticket number from 1 to 74,310.
# Users can choose their seats.
# The first seats correspond to VIP boxes, the next to the VIP area, and the rest to general seating (considering the percentages).
# Ticket Purchase Limits:
# Users with a membership card can buy up to 10 tickets, while non-members can purchase up to 3 tickets.
# Seat Availability Validation:
# The system must validate if a seat has already been sold to another user and offer a nearby seat if necessary.
# Seat Costs:
# VIP boxes: £1000 per seat.
# VIP seats: £500 per seat.
# General seating: £90 per seat.
# System Workflow:
# Login.
# Confirm membership status.
# Select seats.
# Make payment.
# Generate and issue tickets.
# Remaining Seat Display:
# The system should display the number of available seats after each purchase.

class Asientos:
    def __init__(self):
        self.total_asientos = 74310
        self.precios_asientos = {'vip box': 1000, 'vip': 500, 'general': 90}
        self.asientos = {'vip box': list(range(1, 3716)), 'vip': list(range(3716, 14863)), 'general': list(range(14863, 74311))}

    def comprobar_existencia(self, claseAsiento, numeroAsiento):
        return numeroAsiento in self.asientos[claseAsiento]
    
    def tipos_asientos(self):
        claves = list(self.asientos.keys())
        for i, (tipo, asiento) in enumerate(self.asientos.items(), start=1):
            print(f"{i}. {tipo}: del asiento {asiento[0]} al {asiento[len(asiento)-1]}")
        while True:
            try:
                seleccion = int(input(f"Seleccione un tipo de asiento (1-{len(self.asientos.items())}): "))
                if 1 <= seleccion <= len(self.asientos.items()):
                    return claves[seleccion-1]
                else:
                    print("\nSelección inválida. Asegúrese de elegir una dentro del rango.")
            except ValueError:
                print("\nPor favor, ingrese un valor válido.")

    def elegir_numero(self, clave):
        while True:
            try: 
                eleccion = int(input(f"Seleccione un asiento del {self.asientos[clave][0]} al {self.asientos[clave][len(self.asientos[clave])-1]}: "))
                if self.asientos[clave][0] <= eleccion <= self.asientos[clave][len(self.asientos[clave])-1]:
                    return eleccion
                else:
                    print("Ingrese un numero dentro del rango señalado")
            except ValueError:
                print("\nPor favor, ingrese un valor válido.")

    def ocupar_asiento(self, clase, asiento): 
        try:
            self.asientos[clase].remove(asiento)
            print("El asiento se reservo correctamente")
            self.total_asientos -= 1
            return True
        except ValueError:
            print("No se pudo realizar la reserva")
            return False

    def descuento_miembro(self, miembro, clase):
        if miembro == True:
            precio = self.precios_asientos[clase] * 0,15
            print(self.precios_asientos[clase])
            print("El precio de las entradas cuentan con un 15% de descuento por ser socio del club")
        else:
            precio = self.precios_asientos[clase]
        return precio
    
    def asiento_cercano(self, clase, asiento):
        # Buscar hacia adelante
        for i in range(asiento, self.asientos[clase][-1] + 1):
            if self.comprobar_existencia(clase, i):
                return i

        # Buscar hacia atrás
        for i in range(asiento - 1, self.asientos[clase][0] - 1, -1):
            if self.comprobar_existencia(clase, i):
                return i

        # Si no se encuentra ningún asiento disponible en la misma clase
        return None


class Usuario:
    def __init__(self):
        self.usuarios = {}
        self.attempts = 3
        self.Usuario_membership = False

    def pedir_datos_nuevo_usuario(self, es_miembro):
        # Solicitar nombre de usuario
        while True:
            nombre = input("Ingrese un nombre de usuario: ").strip()

            # Verificar si el usuario ya existe
            if nombre in self.usuarios:
                print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
                continue
            else:
                break

        # Solicitar contraseña
        while True:
            contrasenia = input("Ingrese una contraseña (mínimo 6 caracteres): ").strip()

            # Validar longitud de contraseña
            if len(contrasenia) < 6:
                print("La contraseña debe tener al menos 6 caracteres.")
            else:
                break  # Salir del bucle si la contraseña es válida

        # Agregar usuario al diccionario
        self.usuarios[nombre] = {
            "contrasenia": contrasenia,
            "miembro": es_miembro
        }
        print("La cuanta fue creada exitosamente.")
        

    def crear_usuario(self):
        while True:
            respuesta = input("¿Es miembro? (Y/N): ").strip().upper()

            if respuesta == "Y":
                es_miembro = True
                break
            elif respuesta == "N":
                es_miembro = False
                break
            else:
                print("Respuesta inválida. Por favor, ingrese 'Y' para Sí o 'N' para No.")

        self.pedir_datos_nuevo_usuario(es_miembro)

    def login(self):
        while self.attempts > 0:
            nombre = input("Ingrese su nombre de usuario: ").strip()
            if nombre in self.usuarios:
                while True:
                    contrasenia = input("Ingrese su contraseña: ").strip()
                    if self.usuarios[nombre]["contrasenia"] == contrasenia:
                        return True, self.usuarios[nombre]["miembro"]
                    else:
                        print("Contraseña incorrecta. Inténtelo nuevamente.")
                        self.attempts -= 1
                        print(f"Contraseña incorrecta. Intentos restantes: {self.attempts}")
                        if self.attempts == 0:
                            print("Cuenta bloqueada. Por favor, contacte al soporte.")
                            return False
            else:
                print("No existe un usuario con ese nombre.")
                return False

    def menu_inicio(self):
        print("------Bienvenido------")
        print("1. Crear Usuario")
        print("2. Ingresar")

    def leer_opcion(self):
        
        while True:
            self.menu_inicio()
            try:
                opcion = int(input("Ingrese una opcion (1-2): "))
                if 1 <= opcion <= 2:
                    if opcion == 1:
                        self.crear_usuario()
                    elif opcion == 2:
                        return self.login()      
                else:
                    print("Ingrese una opcion dentro del rango correcto")
            except ValueError:
                print("\nPor favor, ingrese un valor válido.")


class Estadio:
    def __init__(self):
        self.entradas = Asientos()
        self.usuario = Usuario()
        self.entradas_vendidas = []

    def menu(self):
        print("1. Comprar entradas")
        print("2. Salir")

    def leer_opcion(self):
        while True:
            self.menu()
            try:
                opcion = int(input("Ingrese una opcion (1-2): "))
                if 1 <= opcion <= 2:
                    if opcion == 1:
                        return True
                    elif opcion == 2:
                        return False   
                else:
                    print("Ingrese una opcion dentro del rango correcto")
            except ValueError:
                print("\nPor favor, ingrese un valor válido.")


    def programa_principal(self):
        asientos_disponibles = 3
        login, miembro = self.usuario.leer_opcion()
        if miembro == True:
            asientos_disponibles = 10
        while asientos_disponibles > 0 and login:
            if self.leer_opcion():
                clave = self.entradas.tipos_asientos()
                valor = self.entradas.elegir_numero(clave)
                if self.entradas.comprobar_existencia(clave, valor):
                    precio = self.entradas.descuento_miembro(miembro, clave)
                    print(f"El precio por {clave} nro. {valor} es {precio}")
                    respuesta = input("Ingrese Y para confirmar o cual otra tecla para cancelar: ").strip().upper()
                    if respuesta == "Y":
                        self.entradas.ocupar_asiento(clave, valor)
                        self.entradas_vendidas.append({
                            "clase": clave,
                            "asiento": valor,
                            "precio": precio
                        })
                        asientos_disponibles -= 1
            else:
                break
        if asientos_disponibles < 1:
            print("Llego al limite de entradas que puede adquirir")
        print("-----Detalle de compra-----")
        for i, datos in enumerate(self.entradas_vendidas, start=1):
            print(f"{i}. Ubicación: {datos['clase']} Asiento: {datos['asiento']} Precio {datos['precio']}")
        
    



                
est = Estadio()
est.programa_principal()


# ent = Asientos()
# ent.elegir_numero("vip")
# ent.ocupar_asiento("vip", 3800)
# ent.mostrar_tipos_asientos()

# # Uso de la clase Usuario
                
# usuario = Usuario()
# sesion_iniciada, miembro = usuario.leer_opcion()
# print(sesion_iniciada)
# print(miembro)
