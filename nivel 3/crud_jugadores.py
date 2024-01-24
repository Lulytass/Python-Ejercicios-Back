# 3. Manchester United FC Player Management System:

# As a developer for Manchester United FC, the executive management has tasked you with creating a CRUD system for the current players, including the following information: Jersey number, position, age, height, and other statistical data. Additionally, integrate the system from the previous level where it was possible to compare two players and visualize their characteristics. You may find player information by searching on the internet.

# Features:

# Create:
# Add new players to the system with their respective details.
# Read:
# View the complete list of current players with their jersey number, position, age, height, and other statistical information.
# Update:
# Modify player information as needed, such as position, age, or height.
# Delete:
# Remove players from the system if they are no longer part of the team.
# Compare Players:
# Utilize the comparison feature to analyze and contrast the characteristics of two players.
# Visualize Characteristics:
# Display the statistical and physical attributes of each player for a comprehensive overview.

class Crud_equipo():
    def __init__(self):
        self.jugadores = {
            "8": {
                'nombre': 'Bruno Fernandes', 'posicion': 'Centro Campista', 'edad': 29,
              'altura': 1.79, 'goles': 5, 'puntos asistencia': 9
            },
            "11": {
                'nombre': 'Rasmus Hojlund', 'posicion': 'Delantero', 'edad': 20, 'altura': 1.91,
               'goles': 12, 'puntos asistencia': 2 
            },
            "5": {
                'nombre': 'Harry Maguire', 'posicion': 'Defensa', 'edad': 30, 'altura': 1.94,
              'goles': 1, 'puntos asistencia': 1
            },
            "17": {
                'nombre': 'Alejandro Garnacho', 'posicion': 'Centro Campista', 'edad': 19,
               'altura': 1.80, 'goles': 8, 'puntos asistencia': 8 
            },
            "7": {
                'nombre': 'Mason Mount', 'numero camiseta': 7, 'posicion': 'Centro Campista', 'edad': 25, 'altura': 1.81,
              'goles': 2, 'puntos asistencia': 4
            },
        }
        self.menu = {
            "Ver jugadores": "jugadores",
            "Comparar dos jugadores": "comparar",
            "Visualizar características": "caracteristicas",
            "Crear registro": "crear",
            "Dar de baja jugador": "baja",
            "Editar jugador": "editar",
            "Salir del sistema": "cerrar"
        }

    def mostrar_menu(self):
        print("----Bienvenido----\n")
        for i, opciones in enumerate(self.menu.keys(), start=1):
            print(f"{i}. {opciones}")

    def obtener_opcion(self, estruc, mensaje, retorno_clave=False):
        while True:
            try:
                opcion = int(input(f"\n{mensaje} (1-{len(estruc)}): "))
                if 1 <= opcion <= len(estruc):
                    if retorno_clave:
                        str_opcion = list(estruc.values())[opcion - 1]
                        return str_opcion
                    else:
                        return opcion
                else:
                    print("\nSelección inválida. Asegúrese de elegir una dentro del rango.")
            except ValueError:
                print("\nPor favor, ingrese un número válido.")

    def mostrar_jugadores(self):
        print("----Jugadores Disponibles----\n")
        for i, datos in enumerate(self.jugadores.values(), start=1):
            print(f"{i}. {datos['nombre']}")

    def seleccionar_jugadores(self, estruc):
        opcion1 = self.obtener_opcion(estruc, "Seleccione el primer jugador", False)
        opcion2 = self.obtener_opcion(estruc, "Seleccione el segundo jugador", False)

        return opcion1, opcion2

    def mostrar_jugador(self, jugador):
        camiseta = list(self.jugadores.keys())[jugador - 1]
        jugador_seleccionado = list(self.jugadores.values())[jugador - 1]
        print(f"\nCamiseta Numero: {camiseta}\nPosición: {jugador_seleccionado['posicion']}\nNombre: {jugador_seleccionado['nombre']}\nGoles: {jugador_seleccionado['goles']}\nAsistencias: {jugador_seleccionado['puntos asistencia']}\nEdad: {jugador_seleccionado['edad']}\nAltura: {jugador_seleccionado['altura']}")
   
    def crear_registro(self):
        print("----Crear Nuevo Jugador----\n")
        while True:
            try:
                nombre = input("Nombre del jugador: ")
                posicion = input("Posición: ")
                edad = int(input("Edad: "))
                altura = float(input("Altura: "))
                goles = int(input("Goles: "))
                asistencias = int(input("Asistencias: "))
                numero_camiseta = int(input("Camiseta: "))
                # crea un numero de camiseta unico
                if str(numero_camiseta) in self.jugadores.keys():
                    input("Ese numero de camiseta ya esta en uso")
                    continue
                else:
                    nuevo_jugador = {
                        'nombre': nombre,
                        'posicion': posicion,
                        'edad': edad,
                        'altura': altura,
                        'goles': goles,
                        'puntos asistencia': asistencias,
                        'numero camiseta': numero_camiseta
                    }

                    self.jugadores[str(numero_camiseta)] = nuevo_jugador
                    print(f"\n¡Jugador {nombre} agregado al sistema con éxito!\n")
                    break
            except ValueError:
                print("\nPor favor, ingrese un número válido.")

    def actualizar_jugador(self):
        self.mostrar_jugadores()
        jugador_a_actualizar = self.obtener_opcion(self.jugadores.keys(), "Seleccione el jugador que desea actualizar", False)

        if 1 <= jugador_a_actualizar <= len(self.jugadores):
            clave_jugador = list(self.jugadores.keys())[jugador_a_actualizar - 1]
            jugador_actualizado = self.jugadores[clave_jugador]

            print(f"\n----Actualizar Jugador {clave_jugador}----")
            print("Deje en blanco si no desea realizar cambios.")

            nombre = input(f"Nombre actual ({jugador_actualizado['nombre']}): ") or jugador_actualizado['nombre']
            posicion = input(f"Posición actual ({jugador_actualizado['posicion']}): ") or jugador_actualizado['posicion']
            edad = input(f"Edad actual ({jugador_actualizado['edad']}): ") or jugador_actualizado['edad']
            altura = input(f"Altura actual ({jugador_actualizado['altura']}): ") or jugador_actualizado['altura']
            goles = input(f"Goles actual ({jugador_actualizado['goles']}): ") or jugador_actualizado['goles']
            asistencias = input(f"Asistencias actual ({jugador_actualizado['puntos asistencia']}): ") or jugador_actualizado['puntos asistencia']

            self.jugadores[clave_jugador] = {
                'nombre': nombre,
                'posicion': posicion,
                'edad': int(edad),
                'altura': float(altura),
                'goles': int(goles),
                'puntos asistencia': int(asistencias)
            }

            print(f"\n¡Jugador {nombre} actualizado con éxito!\n")
        else:
            print("\nSelección inválida. Asegúrese de elegir una dentro del rango.")

    def dar_de_baja_jugador(self):
        self.mostrar_jugadores()
        jugador_a_eliminar = self.obtener_opcion(self.jugadores.keys(), "Seleccione el jugador que desea dar de baja", False)

        if 1 <= jugador_a_eliminar <= len(self.jugadores):
            clave_jugador = list(self.jugadores.keys())[jugador_a_eliminar - 1]
            jugador_eliminado = self.jugadores.pop(clave_jugador)
            print(f"\n¡Jugador {jugador_eliminado['nombre']} dado de baja con éxito!\n")
        else:
            print("\nSelección inválida. Asegúrese de elegir una dentro del rango.")

    def programa_principal(self):
        while True:
            self.mostrar_menu()
            opcion_menu = self.obtener_opcion(self.menu, "Seleccione una de las opciones",True)
            if opcion_menu == "jugadores":
                self.mostrar_jugadores()
                opcion_jugador = self.obtener_opcion(self.menu, "Seleccione un jugador",False)
                self.mostrar_jugador(opcion_jugador)                
            elif opcion_menu == "comparar":
                self.mostrar_jugadores()
                opcion1, opcion2 = self.seleccionar_jugadores(self.jugadores)
                print("\nCaracterísticas del primer jugador\n")
                self.mostrar_jugador(opcion1)
                print("\nCaracterísticas del segundo jugador\n")
                self.mostrar_jugador(opcion2)
            elif opcion_menu == "caracteristicas":
                self.mostrar_jugadores()
                opcion_jugador = self.obtener_opcion(self.menu, "Seleccione un jugador",False)
                self.mostrar_jugador(opcion_jugador) 
            elif opcion_menu == "crear":
                self.crear_registro()
            elif opcion_menu == "editar":
                self.actualizar_jugador()
            elif opcion_menu == "baja":
                self.dar_de_baja_jugador()
            else:
                break



prueba = Crud_equipo()
prueba.programa_principal()
