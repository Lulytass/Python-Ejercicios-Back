# 4. United Direct: The Manchester United's Shop



# United Direct, the official store of Manchester United FC, has hired you as a developer for their online store. The manager wishes to launch a new line of products with different discounts.

# Develop the shopping cart of this application considering the following features:

# The jerseys are classified by: Men, Women, and Children.
# Sizes range from XS to 3XL.
# All men's and women's jerseys are priced at £100 if they are short-sleeved.
# Long-sleeved jerseys cost £120.
# Short-sleeved children's jerseys are priced at £70.
# Long-sleeved children's jerseys are priced at £90.
# If you are a club member, you get a 20% discount on the total purchase.
# The user can buy as many jerseys as they want.
# If the buyer wishes to personalize their jersey with a player's number, there is an additional charge of £25.
# The stock is as follows:

# FOR MEN:

# First kit short-sleeved jersey: 100 units
# First kit long-sleeved jersey: 90 units
# Second kit short-sleeved jersey: 80 units
# Second kit long-sleeved jersey: 80 units
# Third kit short-sleeved jersey: 85 units
# Third kit long-sleeved jersey: 50 units
# FOR WOMEN:

# First kit short-sleeved jersey: 105 units
# First kit long-sleeved jersey: 92 units
# Second kit short-sleeved jersey: 81 units
# Second kit long-sleeved jersey: 81 units
# Third kit short-sleeved jersey: 85 units
# Third kit long-sleeved jersey: 51 units
# FOR CHILDREN:

# First kit short-sleeved jersey: 200 units
# First kit long-sleeved jersey: 100 units
# Second kit short-sleeved jersey: 85 units
# Second kit long-sleeved jersey: 85 units
# Third kit short-sleeved jersey: 90 units
# Third kit long-sleeved jersey: 62 units

# IMPORTANT: You decide how many sizes are available for each available shirt size.

class Tienda:
    def __init__(self):
        self.inventario = Inventario()
        self.carrito = Carrito()

    def iniciar_compra(self):
        while True:
            es_socio = input("¿Es usted socio del club? (s/n): ").lower()
            if es_socio in ['s', 'n']:
                es_socio = es_socio == 's'
                break
            else:
                print("Por favor, ingrese una opción válida (s/n).")
        total_final = 0    
        while True:
            self.mostrar_menu()
            seleccion_categoria = input("Seleccione una categoría (1-3) o 0 para finalizar: ")

            if seleccion_categoria == '0':
                break

            if seleccion_categoria not in ['1', '2', '3']:
                print("Por favor, seleccione una opción válida.")
                continue

            categoria = self.obtener_categoria(int(seleccion_categoria))

            kit_seleccionado, tipo_manga, talla_seleccionada = self.seleccionar_producto(categoria)

            cantidad = self.obtener_cantidad(self.inventario.obtener_stock(categoria, tipo_manga, kit_seleccionado, talla_seleccionada))

            if not self.validar_stock(categoria, tipo_manga, kit_seleccionado, talla_seleccionada, cantidad):
                continue

            while True:
                personalizar = input("¿Desea personalizar con el número de un jugador? (s/n): ").lower()
                if personalizar in ['s', 'n']:
                    break
                else:
                    print("Por favor, ingrese una opción válida (s/n).")

            subtotal = self.calcular_subtotal(tipo_manga, cantidad, personalizar)
            descuento = self.obtener_descuento(es_socio)
            total = self.calcular_precio_total(subtotal, descuento)
            total_final += total
            self.actualizar_inventario(categoria, tipo_manga, kit_seleccionado, talla_seleccionada, cantidad)
            self.actualizar_carrito(categoria, tipo_manga, kit_seleccionado, talla_seleccionada, cantidad)

            self.mostrar_resumen(subtotal, descuento, total)

            agregar_mas = input("¿Desea agregar más camisetas al carrito? (s/n): ").lower()

            if agregar_mas != 's':
                break

        print("\nGracias por su compra!")
        self.mostrar_resumen_total()
        print(f"El total de la compra es de: {total_final}")

    def mostrar_menu(self):
        print("\nMenú de selección:")
        print("1. Hombres")
        print("2. Mujeres")
        print("3. Niños")
        print("0. Finalizar compra")

    def obtener_categoria(self, seleccion):
        categorias = ['hombres', 'mujeres', 'niños']
        return categorias[seleccion - 1]

    def seleccionar_producto(self, categoria):
        tipo_manga = self.obtener_tipo_manga()
        kits_disponibles = list(self.inventario.obtener_kits(categoria, tipo_manga))
        seleccion_kit = self.obtener_seleccion("kit", kits_disponibles, categoria, tipo_manga)

        tallas_disponibles = list(self.inventario.obtener_tallas(categoria, tipo_manga, seleccion_kit))
        seleccion_talla = self.obtener_seleccion("talla", tallas_disponibles, categoria, tipo_manga, seleccion_kit)

        return seleccion_kit, tipo_manga, seleccion_talla

    def convertir_opcion(self, tipo, opcion):
        if tipo == 'kit':
            return f"Kit {opcion.replace('_', ' ').capitalize()}"
        elif tipo == 'talla':
            return f"Talla {opcion.replace('_', ' ').capitalize()}"
        else:
            return opcion.replace('_', ' ').capitalize()

    def obtener_seleccion(self, tipo, opciones, categoria=None, tipo_manga=None, kit=None):
        while True:
            print(f"\nSeleccione un {tipo}:")
            for i, opcion in enumerate(opciones, start=1):
                if categoria is not None and tipo_manga is not None and kit is not None:
                    print(f"{i}. {self.convertir_opcion(tipo, opcion)} (Disponible: {self.inventario.obtener_stock(categoria, tipo_manga, kit, opcion)})")
                else:
                    print(f"{i}. {self.convertir_opcion(tipo, opcion)}")
            
            seleccion = input(f"Seleccione un {tipo} (1-{len(opciones)}): ")

            if seleccion not in map(str, range(1, len(opciones) + 1)):
                print("Por favor, seleccione una opción válida.")
                continue

            return opciones[int(seleccion) - 1]

    def obtener_tipo_manga(self):
        while True:
            print("\nSeleccione el tipo de manga:")
            print("1. Manga corta")
            print("2. Manga larga")

            seleccion_manga = input("Seleccione el tipo de manga (1-2): ")

            if seleccion_manga not in ['1', '2']:
                print("Por favor, seleccione una opción válida.")
                continue

            return 'corta' if seleccion_manga == '1' else 'larga'

    def obtener_cantidad(self, stock_disponible):
        while True:
            print(f"\nIngrese la cantidad de camisetas que desea comprar (Disponible: {stock_disponible}):")
            cantidad = input("Cantidad: ")

            if not cantidad.isdigit() or int(cantidad) <= 0 or int(cantidad) > stock_disponible:
                print("Por favor, ingrese una cantidad válida y dentro del stock disponible.")
                continue

            return int(cantidad)

    def validar_stock(self, categoria, tipo_manga, kit, talla, cantidad):
        if cantidad > self.inventario.obtener_stock(categoria, tipo_manga, kit, talla):
            print("No hay suficientes unidades disponibles.")
            return False

        return True

    def calcular_subtotal(self, tipo_manga, cantidad, personalizar):
        return (
            cantidad * self.inventario.obtener_precio_manga(tipo_manga) +
            self.inventario.obtener_precio_personalizacion(personalizar, cantidad)
        )

    def obtener_descuento(self, es_socio):
        return self.inventario.obtener_descuento(es_socio)

    def calcular_precio_total(self, subtotal, descuento):
        return subtotal * (1 - descuento)

    def actualizar_inventario(self, categoria, tipo_manga, kit, talla, cantidad):
        self.inventario.actualizar_stock(categoria, tipo_manga, kit, talla, cantidad)

    def actualizar_carrito(self, categoria, tipo_manga, kit, talla, cantidad):
        self.carrito.actualizar_carrito(categoria, tipo_manga, kit, talla, cantidad)

    def mostrar_resumen(self, subtotal, descuento, total):
        print(f"\nSubtotal: £{subtotal}")
        print(f"Descuento: £{descuento * 100}%")
        print(f"Total: £{total}")

    def mostrar_resumen_total(self):
        self.carrito.mostrar_carrito()


class Inventario:
    def __init__(self):
        self.inventario = {
            'hombres': {
                'corta': {
                    'first_kit': {'XS': 10, 'S': 10, 'M': 30, 'L': 20, 'XL': 10, '2XL': 10, '3XL': 10},
                    'second_kit': {'XS': 10, 'S': 10, 'M': 20, 'L': 10, 'XL': 10, '2XL': 10, '3XL': 10},
                    'third_kit': {'XS': 10, 'S': 10, 'M': 20, 'L': 15, 'XL': 10, '2XL': 10, '3XL': 10},
                },
                'larga': {
                    'first_kit': {'XS': 10, 'S': 10, 'M': 20, 'L': 20, 'XL': 10, '2XL': 10, '3XL': 10},
                    'second_kit': {'XS': 10, 'S': 10, 'M': 20, 'L': 10, 'XL': 10, '2XL': 10, '3XL': 10},
                    'third_kit': {'XS': 5, 'S': 5, 'M': 10, 'L': 10, 'XL': 5, '2XL': 10, '3XL': 5},
                },
            },
            'mujeres': {
                'corta': {
                    'first_kit': {'XS': 10, 'S': 10, 'M': 30, 'L': 20, 'XL': 15, '2XL': 10, '3XL': 10},
                    'second_kit': {'XS': 10, 'S': 10, 'M': 20, 'L': 11, 'XL': 10, '2XL': 10, '3XL': 10},
                    'third_kit': {'XS': 10, 'S': 10, 'M': 20, 'L': 12, 'XL': 13, '2XL': 10, '3XL': 10},
                },
                'larga': {
                    'first_kit': {'XS': 10, 'S': 10, 'M': 20, 'L': 12, 'XL': 10, '2XL': 10, '3XL': 10},
                    'second_kit': {'XS': 10, 'S': 10, 'M': 20, 'L': 11, 'XL': 10, '2XL': 10, '3XL': 10},
                    'third_kit': {'XS': 5, 'S': 5, 'M': 10, 'L': 11, 'XL': 5, '2XL': 10, '3XL': 5},
                },
            },
            'niños': {
                'corta': {
                    'first_kit': {'XS': 20, 'S': 30, 'M': 30, 'L': 30, 'XL': 30, '2XL': 30, '3XL': 30},
                    'second_kit': {'XS': 10, 'S': 10, 'M': 20, 'L': 12, 'XL': 13, '2XL': 10, '3XL': 10},
                    'third_kit': {'XS': 10, 'S': 10, 'M': 20, 'L': 10, 'XL': 20, '2XL': 10, '3XL': 10},
                },
                'larga': {
                    'first_kit': {'XS': 10, 'S': 10, 'M': 30, 'L': 20, 'XL': 10, '2XL': 10, '3XL': 10},
                    'second_kit': {'XS': 10, 'S': 10, 'M': 20, 'L': 12, 'XL': 13, '2XL': 10, '3XL': 10},
                    'third_kit': {'XS': 10, 'S': 10, 'M': 10, 'L': 10, 'XL': 10, '2XL': 5, '3XL': 7},
                },
            },
        }

    def obtener_kits(self, categoria,manga):
        return list(self.inventario[categoria][manga].keys())

    def obtener_tallas(self, categoria, tipo_manga, kit):
        if (
            categoria in self.inventario
            and tipo_manga in self.inventario[categoria]
            and kit in self.inventario[categoria][tipo_manga]
        ):
            return list(self.inventario[categoria][tipo_manga][kit].keys())
        else:
            return []

    def obtener_precio_manga(self, tipo_manga):
        return 100 if tipo_manga == 'corta' else 120

    def obtener_precio_personalizacion(self, personalizar, cantidad):
        return 25 * cantidad if personalizar == 's' else 0

    def obtener_descuento(self, es_socio):
        return 0.2 if es_socio else 0.0

    def obtener_stock(self, categoria, tipo_manga, kit, talla):
        return self.inventario[categoria][tipo_manga][kit][talla]

    def actualizar_stock(self, categoria, tipo_manga, kit, talla, cantidad):
        self.inventario[categoria][tipo_manga][kit][talla] -= cantidad



class Carrito:
    def __init__(self):
        self.carrito = {
            'hombres': {'corta': {}, 'larga': {}},
            'mujeres': {'corta': {}, 'larga': {}},
            'niños': {'corta': {}, 'larga': {}},
        }

    def actualizar_carrito(self, categoria, tipo_manga, kit, talla, cantidad):
        if talla not in self.carrito[categoria][tipo_manga]:
            self.carrito[categoria][tipo_manga][talla] = {}

        if kit not in self.carrito[categoria][tipo_manga][talla]:
            self.carrito[categoria][tipo_manga][talla][kit] = {}

        if talla not in self.carrito[categoria][tipo_manga][talla][kit]:
            self.carrito[categoria][tipo_manga][talla][kit][talla] = 0

        self.carrito[categoria][tipo_manga][talla][kit][talla] += cantidad

    def mostrar_carrito(self):
        print("\nResumen del carrito:")
        for categoria, mangas in self.carrito.items():
            for tipo_manga, kits in mangas.items():
                for talla, kits_talla in kits.items():
                    for kit, cantidades in kits_talla.items():
                        for talla, cantidad in cantidades.items():
                            print(
                                f"{cantidad} camisetas {categoria.capitalize()}, "
                                f"manga {tipo_manga}, talla {talla.replace('_', ' ').capitalize()}, "
                                f"{kit}"
                            )

# Iniciar la tienda y realizar la compra
tienda = Tienda()
tienda.iniciar_compra()

