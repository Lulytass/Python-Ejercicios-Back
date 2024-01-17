# 1. Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their fastest player, player with the most goals, assists, passing accuracy, and defensive involvements.
# The system should also allow comparison between two players. Use the following player profiles:

# Bruno Fernandes: 5 goals, 6 points in speed, 9 points in assists, 10 points in passing accuracy, 3 defensive involvements. Corresponds to jersey number 8.
# Rasmus Hojlund: 12 goals, 8 points in speed, 2 points in assists, 6 points in passing accuracy, 2 defensive involvements. Corresponds to jersey number 11.
# Harry Maguire: 1 goal, 5 points in speed, 1 point in assists, 7 points in passing accuracy, 9 defensive involvements. Corresponds to jersey number 5.
# Alejandro Garnacho: 8 goals, 7 points in speed, 8 points in assists, 6 points in passing accuracy, 0 defensive involvements. Corresponds to jersey number 17.
# Mason Mount: 2 goals, 6 points in speed, 4 points in assists, 8 points in passing accuracy, 1 defensive involvement. Corresponds to jersey number 7.
# The program functions as follows: The coach accesses the system and encounters a menu with the following options:

# Player Review: By entering the player's jersey number, they can access the player's characteristics.
# Compare two players: The system prompts for two jersey numbers and displays the data of both players on screen.
# Identify the fastest player: Displays the player with the most points in speed.
# Identify the top goal scorer: Displays the player with the most points in goals.
# Identify the player with the most assists: Displays the player with the most points in assists.
# Identify the player with the highest passing accuracy: Displays the player with the most points in passing accuracy.
# Identify the player with the most defensive involvements: Displays the player with the most points in defensive involvements.
# The system should also allow returning to the main menu.

class Jugadores:
    def __init__(self):
        self.jugadores = {
            "8": {
                "nombre": "Bruno Fernandes", "goles": 5, "velocidad": 6, "asistencias": 9, "precisión de pase": 10, "participaciones defensivas": 3 
            },
            "11": {
                "nombre": "Rasmus Hojlund", "goles": 12, "velocidad": 8, "asistencias": 2, "precisión de pase": 6, "participaciones defensivas": 2 
            },
            "5": {
                "nombre": "Harry Maguire", "goles": 1, "velocidad": 5, "asistencias": 1, "precisión de pase": 7, "participaciones defensivas": 9 
            },
            "17": {
                "nombre": "Alejandro Garnacho", "goles": 8, "velocidad": 7, "asistencias": 8, "precisión de pase": 6, "participaciones defensivas": 0 
            },
            "7": {
                "nombre": "Mason Mount", "goles": 2, "velocidad": 6, "asistencias": 4, "precisión de pase": 8, "participaciones defensivas": 1
            },
        }
        self.menu = {
            "Máximo goleador": "goles",
            "Jugador más rápido": "velocidad",
            "Revisión del jugador": "ver jugador",
            "Comparar dos jugadores": "comparar",
            "Jugador con más asistencias": "asistencias",
            "Jugador con mayor precisión de pase": "precisión de pase",
            "Jugador con más implicaciones defensivas": "participaciones defensivas",
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

    def maximos(self, busqueda):
        max_valor = 0
        jugador_max_valor = None

        for datos in self.jugadores.values():
            valor = datos[busqueda]
            if valor > max_valor:
                max_valor = valor
                jugador_max_valor = datos["nombre"]

        if max_valor > 0:
            print(f"Nombre: {jugador_max_valor}\n{busqueda}: {max_valor}.")
        else:
            print("Todos los jugadores se encuentran en 0 en dicho aspecto.")

    def mostrar_jugadores(self):
        print("----Jugadores Disponibles----\n")
        for i, datos in enumerate(self.jugadores.values(), start=1):
            print(f"{i}. {datos['nombre']}")

    def seleccionar_jugadores(self, estruc):
        opcion1 = self.obtener_opcion(estruc, "Seleccione el primer jugador", False)
        opcion2 = self.obtener_opcion(estruc, "Seleccione el segundo jugador", False)

        return opcion1, opcion2

    def mostrar_jugador(self, jugador):
        jugador_seleccionado = list(self.jugadores.values())[jugador - 1]
        print(f"\nNombre: {jugador_seleccionado['nombre']}\nGoles: {jugador_seleccionado['goles']}\nVelocidad: {jugador_seleccionado['velocidad']}\nAsistencias: {jugador_seleccionado['asistencias']}\nPrecisión de pase: {jugador_seleccionado['precisión de pase']}\nParticipaciones defensivas: {jugador_seleccionado['participaciones defensivas']}")

    def programa_principal(self):
        while True:
            self.mostrar_menu()
            opcion_menu = self.obtener_opcion(self.menu, "Seleccione una de las opciones",True)
            
            if opcion_menu in ["goles", "velocidad", "asistencias", "precisión de pase", "participaciones defensivas"]:
                self.maximos(opcion_menu)
            elif opcion_menu == "ver jugador":
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
            else:
                break


prueba = Jugadores()
prueba.programa_principal()

  
        
           
                

