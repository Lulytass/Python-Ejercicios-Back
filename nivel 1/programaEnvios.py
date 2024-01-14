# 4. Create an online shipping system with the following features:
# * 		The system has a login that locks after the third failed attempt.
# * 		Display a menu that allows: Sending a package, exiting the system.
# * 		To send a package, sender and recipient details are required.
# * 		The system assigns a random package number to each sent package.
# * 		The system calculates the shipping price. $2 per kg.
# * 		The user must input the total weight of their package, and the system should display the amount to pay.
# * 		The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.
import random

class Envios:
    def __init__(self):
        self.nombre_remitente = ""
        self.apellido_remitente = ""
        self.nombre_destinatario = ""
        self.nombre_destinatario = ""
        self.precio_kilo = 2
        self.attempts = 3
        self.name = ""
        self.password = ""
        self.envios = []

    def verificar(self):
        correct_name = "lucia"
        correct_password = "lucia"
        
        while self.attempts > 0:
            self.name = input("Ingrese su nombre: ").strip()
            self.password = input("Ingrese su password: ").strip()

            if not self.name or not self.password:
                print("Nombre y contraseña no pueden estar vacíos.")
                continue

            if self.name == correct_name and self.password == correct_password:
                self.menu()
                break
            else:
                self.attempts -= 1
                print(f"Credenciales incorrectas. Intentos restantes: {self.attempts}")

        if self.attempts == 0:
            print("Has alcanzado el número máximo de intentos. Se bloqueará el acceso.")
            exit()

    def costo_paquete(self):
        while True:
            peso_paquete = input("Ingrese el peso del paquete: ")
            if not peso_paquete.isdigit() or float(peso_paquete) < 0:
                print("\nDebe ingresar un numero valido")
                continue
            break
        return float(peso_paquete) * self.precio_kilo
                


    def envio(self):
        self.pedir_datos()
        precio = self.costo_paquete()
        print(f"El costo del envio es ${precio}")

        respuesta = input("Si aprueba el envio presione Y, si quiere volver al menu principal M, para salir cualquier otra letra: ")
        if respuesta == "Y":
            numero_pedido = self.numero_aleatorio()
            self.envios.append({
                                        "Remitente": self.nombre_remitente +" "+ self.apellido_remitente,
                                        "Destinatario": self.nombre_destinatario +" "+ self.apellido_destinatario,
                                        "Precio": precio,
                                        "Numero" : numero_pedido
                                    })
            print("envio cargado exitosamente")
        elif respuesta == "M":
            self.menu()
        else:
            self.mostrar_envios()
            exit()
            


    def numero_aleatorio(self):
        return random.randint(100000, 999999)  # Genera un número aleatorio de 6 dígitos

    def pedir_datos(self):
        while True:
            self.nombre_remitente = input("Ingrese el nombre del remitente: ")
            self.apellido_remitente = input("Ingrese el apellido del remitente: ")

            if not self.nombre_remitente.isalpha() or not self.apellido_remitente.isalpha():
                print("Por favor, ingrese solo letras para el nombre y apellido.")
                continue   
            
            self.nombre_destinatario = input("Ingrese el nombre del destinatario: ")
            self.apellido_destinatario = input("Ingrese el nombre del destinatario: ")
            if not self.nombre_destinatario.isalpha() or not self.apellido_destinatario.isalpha():
                print("Por favor, ingrese solo letras para el nombre y apellido.")
                continue 
            break

    def mostrar_envios(self):
        if len(self.envios) >= 0:
            print("\nEnvios cargados:")
            for pedido in self.envios:
                print(f"Remitente: {pedido['Remitente']}")
                print(f"Destinatario: {pedido['Destinatario']}")
                print(f"Precio: {pedido['Precio']}")
                print(f"Numero de envio: {pedido['Numero']}")
                print("-----------------------")
            else:
                print("No se han cargado envios")

    def menu(self):
        while True:
            print("\nSeleccione alguna de las siguientes opciones:")
            print("1. Enviar un paquete")
            print("2. Salir del sistema")

            opcion_input = input("Ingrese una opción: ")
            
            if not opcion_input.isdigit():
                print("Por favor, ingrese un número válido.")
                continue
            elif int(opcion_input) == 1:
                    self.envio()
            elif int(opcion_input) == 2:
                    self.mostrar_envios()
                    print("Saliendo del sistema...")
                    exit()
            else:
                print("Opción no válida. Intente nuevamente.")
    

prueba = Envios()
prueba.verificar()   

