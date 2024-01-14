# 5. Develop a finance management application with the following features:
# * 		The user records their total income.
# * 		There are categories: Medical expenses, household expenses, leisure, savings, and education.
# * 		The user can list their expenses within the categories and get the total for each category.
# * 		The user can obtain the total of their expenses.
# * 		If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
# * 		If the user spends less than they earn, the system displays a congratulatory message on the screen.
# * 		If the user spends more than they earn, the system will display advice to improve the user's financial health.
class Gasto:
    def __init__(self, importe, detalle):
        self.importe = importe
        self.detalle = detalle

    def __str__(self):
        return f"Detalle: {self.detalle}, Importe: ${self.importe}"

class Gestor_gastos:
    def __init__(self):
        self.gastos_medicos = []
        self.gastos_hogar = []
        self.ocio = []
        self.ahorro = []
        self.educacion = []
        self.ingreso = 0

    def menu(self):
        while True:
            print("Cargar nuevo gasto")
            print("1. Gastos Médicos")
            print("2. Gastos del Hogar")
            print("3. Ocio")
            print("4. Ahorro")
            print("5. Educación")
            print("6. Salir")

            opcion = input("Ingrese una categoría: ")

            if not opcion:
                print("\nDebe ingresar una opción\n")
                continue
            else:
                if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 6:
                    print("\nDebe ingresar un numero del 1 al 6\n")
                    continue
                else:
                   return int(opcion) 
                
    def ingresar_ingreso(self):
        while True:
            ingreso = input("Ingrese su ingreso total: ")
            if self.verificar_datos(ingreso):
                self.ingreso = float(ingreso)
                break
                        
    def mostrar_gastos(self):
        categorias = {
            'medicos': self.gastos_medicos,
            'hogar': self.gastos_hogar,
            'ocio': self.ocio,
            'ahorro': self.ahorro,
            'educacion': self.educacion
        }

        for categoria, lista_gastos in categorias.items():
            print(f"== {categoria.capitalize()} ==")
            for gasto in lista_gastos:
                print(gasto)
            print("\n")

    def sumar_gastos(self):
        total_general = 0

        for categoria, lista_gastos in {
            'medicos': self.gastos_medicos,
            'hogar': self.gastos_hogar,
            'ocio': self.ocio,
            'ahorro': self.ahorro,
            'educacion': self.educacion
        }.items():
            total_categoria = sum(float(gasto.importe) for gasto in lista_gastos)
            total_general += total_categoria
            print(f"Total en {categoria.capitalize()}: ${total_categoria}")

        print(f"\nGasto total general: ${total_general}")

        if self.ingreso > total_general:
            print("¡Felicidades! Estás gastando menos de lo que ganas. ¡Sigue así!")
        elif self.ingreso == total_general:
            print("Estás gastando exactamente lo que ganas. Considera ajustar tus gastos.")
        else:
            print("Necesitas reducir tus gastos. Considera revisar tus gastos en la categoría donde más gastas.")


    def ingresar_gastos(self):
        print("A continuación ingresara importe y detalle del gasto")
        while True:
            opcion_seleccionada = self.menu()
            importe = input("Ingrese el importe del gasto: ")
            if not self.verificar_datos(importe):
                continue
            detalle = input("Ingrese el detalle del gasto: ")

            gasto = Gasto(importe, detalle)

            if opcion_seleccionada == 1:
                self.grabar_gasto('medicos', gasto)
            elif opcion_seleccionada == 2:
                self.grabar_gasto('hogar', gasto)
            elif opcion_seleccionada == 3:
                self.grabar_gasto('ocio', gasto)
            elif opcion_seleccionada == 4:
                self.grabar_gasto('ahorro', gasto)
            elif opcion_seleccionada == 5:
                self.grabar_gasto('educacion', gasto)
            else:
                self.mostrar_gastos()
                self.sumar_gastos()
                break
            
    def grabar_gasto(self, categoria, gasto):
        if categoria == 'medicos':
            self.gastos_medicos.append(gasto)
        elif categoria == 'hogar':
            self.gastos_hogar.append(gasto)
        elif categoria == 'ocio':
            self.ocio.append(gasto)
        elif categoria == 'ahorro':
            self.ahorro.append(gasto)
        elif categoria == 'educacion':
            self.educacion.append(gasto)

    def verificar_datos(self, importe):
        try:
            importe_gasto = float(importe)
            if importe_gasto <= 0:
                print("\nEl número ingresado debe ser positivo\n")
                return False
            return True
        except ValueError:
            print("\nIngrese un importe válido\n")
            return False
        
control_finanzas = Gestor_gastos()
control_finanzas.ingresar_gastos()