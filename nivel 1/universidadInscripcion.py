# 3. Create an university enrollment system with the following characteristics:
# * 		The system has a login with a username and password.
# * 		Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
# * 		The user must input their first name, last name, and chosen program.
# * 		Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
# # * 		If login information is incorrect three times, the system should be locked.
# * 		The user must choose a campus from three cities: London, Manchester, Liverpool.
# * 		In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
# * 		If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.
class Universidad:
    def __init__(self):
        self.contraseña = ""
        self.usuario = ""
        self.programas = {"Informática": 5, "Medicina": 5, "Marketing": 5, "Artes": 5}
        self.ciudades = {"Londres": 1 , "Manchester": 3, "Liverpool": 1}
        self.attempts = 3
        self.estudiantesInscriptos = []

    def login(self):
        usuario = "univ"
        password = "univ"

        while self.attempts > 0:
            self.usuario = input("Ingrese su usuario: ").strip()
            self.contraseña = input("Ingrese su password: ").strip()

            if not self.usuario or not self.contraseña:
                print("Nombre y contraseña no pueden estar vacíos.")
                continue

            if self.usuario == usuario and self.contraseña == password:
                self.inscripcion()
                break
            else:
                self.attempts -= 1
                print(f"Credenciales incorrectas. Intentos restantes: {self.attempts}")

        if self.attempts == 0:
            print("Has alcanzado el número máximo de intentos. Se bloqueará el acceso.")         

    def inscripcion(self):
        

        while True:

            nombre = input("Nombre del alumno: ")
            apellido = input("Apellido del alumno: ")

            print("\nProgramas:")
            print("0. Informatica")
            print("1. Medicina")
            print("2. Marketing")
            print("3. Artes")

            programaSelec = input("Seleccione el programa que desea: ")

            if programaSelec.isdigit() and 0 <= int(programaSelec) <= 3:

                if self.verificar_cupo_disponible("programa", int(programaSelec)):

                    print("\nSeleccione una ciudad:")
                    print("0. Londres")
                    print("1. Manchester")
                    print("2. Liverpool")

                    while True:  # Bucle para seleccionar una ciudad
                        ciudadSelec = input("Seleccione la ciudad que desea: ")

                        if ciudadSelec.isdigit() and 0 <= int(ciudadSelec) <= 2:
                            if self.verificar_cupo_disponible("programa", int(programaSelec)) and self.verificar_cupo_disponible("ciudad", int(ciudadSelec)):
                                nombreCiudad = list(self.ciudades.keys())
                                nombreProg = list(self.programas.keys())
                                self.estudiantesInscriptos.append({
                                    "First Name": nombre,
                                    "Last Name": apellido,
                                    "Program": nombreProg[int(programaSelec)],
                                    "Campus": nombreCiudad[int(ciudadSelec)]
                                })
                                break  # Salir del bucle una vez que se haya inscrito correctamente
                            else:
                                continue  # Si no hay cupos, sigue pidiendo seleccionar una ciudad
                        else:
                            print("Selección de ciudad no válida. Intente de nuevo.")
                else:
                    print("Selección de programa no válida. Intente de nuevo.")

                respuesta = input("¿Desea inscribir a otro estudiante? (Y/N): ")
                if respuesta.upper() != "Y":
                    break
        #Mostramos cada uno de los inscriptos             
        print("\nEstudiantes Inscritos:")
        for estudiante in self.estudiantesInscriptos:
            print(f"Nombre: {estudiante['First Name']} {estudiante['Last Name']}")
            print(f"Programa: {estudiante['Program']}")
            print(f"Campus: {estudiante['Campus']}")
            print("-----------------------")                    
                

    #funcion para validar los valores de las listas programas / ciudades
    def verificar_cupo_disponible(self, tipo, numero):
        if tipo == 'programa':
            programas = list(self.programas.keys())
            if 0 <= numero < len(programas):
                programa_seleccionado = programas[numero]
                if self.programas[programa_seleccionado] > 0:
                    self.programas[programa_seleccionado] -= 1
                    return True
                else:
                    print(f"Lo sentimos, no hay cupos disponibles para {programa_seleccionado}.")
                    return False
            else:
                print("Número de programa no válido.")
                return False
        elif tipo == 'ciudad':
            ciudades = list(self.ciudades.keys())
            if 0 <= numero < len(ciudades):
                ciudad_seleccionada = ciudades[numero]
                if self.ciudades[ciudad_seleccionada] > 0:
                    self.ciudades[ciudad_seleccionada] -= 1
                    return True
                else:
                    print(f"Lo sentimos, no hay cupos disponibles para la ciudad de {ciudad_seleccionada}.")
                    return False
            else:
                print("Número de ciudad no válido.")
                return False
        else:
            print("Tipo no válido. Debe ser 'programa' o 'ciudad'.")
            return False
                

universidad = Universidad()
universidad.login()