# 3. 

# The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

# It must have a login and validate the data; after the third failed attempt, it should be locked.
# The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
# There are 3 doctors for each specialty.
# The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
# The maximum limit for appointments, in general, is 3.
# Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
# Display available specialists.
# The user can choose their preferred specialist.
# The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.
class Hospital:
    def __init__(self):
        self.attempts = 3
        self.especialidad_seleccionada = None
        self.medico_seleccionado = None
        self.turno_seleccionado = None
        self.horario_elegido = None
        self.citas = []
        self.numero_citas_realizadas = 0
        self.max_citas = 3
        self.especialidades_reservadas = []
        self.especialidades = {
    "Medicina General": {
        "gen1": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "gen2": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "gen3": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        }
    },
    "Atención de Emergencias": {
        "em1": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "em2": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "em3": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        }
    },
    "Análisis Clínicos": {
        "cli1": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "cli2": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "cli3": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        }
    },
    "Cardiología": {
        "car1": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "car2": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "car3": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        }
    },
    "Neurología": {
        "neu1": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "neu2": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "neu3": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        }
    },
    "Nutrición": {
        "nut1": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "nut2": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "nut3": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        }
    },
    "Fisioterapia": {
        "fis1": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "fis2": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "fis3": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        }
    },
    "Traumatología": {
        "tra1": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "tra2": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "tra3": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        }
    },
    "Medicina Interna": {
        "int1": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "int2": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        },
        "int3": {
            "Mañana": ["08", "08.30", "09", "09.30", "10", "10.30", "11"],
            "Tarde": ["13", "13.30", "14", "14.30", "15", "15.30", "16"]
        }
    }
}
       

    def login(self):
        usuario_correcto = "hospi"
        password_correcto = "hospi"

        while self.attempts > 0:
            usuario = input("Ingrese su usuario: ").strip()
            contrasena = input("Ingrese su contraseña: ").strip()

            if usuario == usuario_correcto and contrasena == password_correcto:
                return True
            else:
                self.attempts -= 1
                print(f"Credenciales incorrectas. Intentos restantes: {self.attempts}")

            if self.attempts == 0:
                print("Has alcanzado el número máximo de intentos. Se bloqueará el acceso.")
                return False

    def mostrar_opciones(self, opciones, texto):
        print(f"{texto}")
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")

    def obtener_opcion(self, opciones, texto):
        while True:
            try:
                if isinstance(opciones, list):
                    self.mostrar_opciones(opciones, texto)
                    seleccion = int(input(f"Seleccione una opcion (1-{len(opciones)}): "))
                    print(seleccion)
                    if 1 <= seleccion <= len(opciones):
                        return opciones[seleccion - 1]
                    else:
                        print("\nSelección inválida. Asegúrese de elegir una dentro del rango.")
                elif isinstance(opciones, dict):
                    self.mostrar_opciones(opciones.keys(), texto)
                    seleccion = input("Seleccione una opción: ")
                    if seleccion in opciones:
                        return opciones[seleccion]
                    else:
                        print("\nSelección inválida. Asegúrese de elegir una opción válida.")
                else:
                    print("\nTipo de opciones no admitido.")
                    break  # Esto evita el bucle infinito
            except ValueError:
                print("\nPor favor, ingrese un valor válido.")

    def mostrar_turno(self, turnos_disponibles):
        if isinstance(turnos_disponibles, dict):
            print("\nTurnos Disponibles:")
            for i, (turno, horarios) in enumerate(turnos_disponibles.items(), start=1):
                print(f"{i}. {turno}")
        elif isinstance(turnos_disponibles, list):
            print("\nHorarios Disponibles:")
            for i, turno in enumerate(turnos_disponibles, start=1):
                print(f"{i}. {turno}")
        else:
            print("\nTipo de turnos no admitido.")

    def reservar_cita(self, medico, turno):
        cita = f"{self.especialidad_seleccionada} - {medico} - {turno}"
        self.citas.append(cita)
        print(f"Cita reservada: {cita}")

    def mostrar_seleccion(self):
        print("\nResumen de selecciones:")
        print(f"1. Especialidad: {self.especialidad_seleccionada}")
        print(f"2. Médico: {self.medico_seleccionado}")
        print(f"3. Turno: {self.turno_seleccionado}")
        print(f"3. Turno: {self.horario_elegido}")

    def programa_principal(self):
        if self.login():
            while self.numero_citas_realizadas < self.max_citas:
                # Mostrar opciones y obtener selecciones
                opciones_especialidades = list(self.especialidades.keys())
                self.especialidad_seleccionada = self.obtener_opcion(opciones_especialidades, "Especialidades Disponibles")

                medicos_disponibles = self.especialidades[self.especialidad_seleccionada]
                print(self.especialidades_reservadas)
                # Verificar si la especialidad ya ha sido reservada
                if self.especialidad_seleccionada in self.especialidades_reservadas:
                    print("Ya ha reservado una cita para esta especialidad. Seleccione otra especialidad.")
                    continue

                medicos_disponibles = self.especialidades[self.especialidad_seleccionada]
                opciones_medicos = list(medicos_disponibles.keys())
                self.medico_seleccionado = self.obtener_opcion(opciones_medicos, "Médicos Disponibles")

                # Ahora que tenemos el médico seleccionado, podemos obtener los turnos disponibles
                turnos_disponibles = medicos_disponibles[self.medico_seleccionado]

                # # Mostrar turnos disponibles y obtener selección de turno
                # self.mostrar_turno(turnos_disponibles)

                # Obtener la selección de Mañana o Tarde
                opciones_turno = list(turnos_disponibles.keys())
                self.turno_seleccionado = self.obtener_opcion(opciones_turno, "Seleccione Mañana o Tarde")

                # Mostrar los horarios disponibles según la elección de Mañana o Tarde
                horarios_disponibles = turnos_disponibles[self.turno_seleccionado]

                # Obtener la selección de horario
                self.horario_elegido = self.obtener_opcion(horarios_disponibles, "Seleccione un horario")

                # Mostrar resumen de selecciones
                self.mostrar_seleccion()

                # Confirmar la reserva de la cita
                confirmacion = input("\n¿Desea confirmar la reserva de la cita? (S): ").strip().upper()
                if confirmacion == "S":
                    self.reservar_cita(self.medico_seleccionado, f"{self.turno_seleccionado} - {self.horario_elegido}")
                    self.numero_citas_realizadas += 1
                    self.especialidades_reservadas.append(self.especialidad_seleccionada)
                else:
                    print("Reserva de cita cancelada.")

                # Preguntar si desea reservar otra cita
                reservar_otra = input("\n¿Desea reservar otra cita? (S/N): ").strip().upper()
                if reservar_otra != "S":
                    print(f"Citas reservadas: {self.citas}") 
                    print(f"Gracias por usar el sistema. Ha realizado {self.numero_citas_realizadas} citas.")
                    break
            
                if self.numero_citas_realizadas == 3:
                    print(f"Ha llegado al limite de citas reservadas")
                    print(f"Saliendo del sistema")
                    break

prueba = Hospital()
prueba.programa_principal()