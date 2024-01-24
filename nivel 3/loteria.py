# 2. Lottery System: 

#  The lottery system produces results consisting of 4 digits + 1 letter, e.g., 0345F. Develop a lottery ticket purchase system with the following features:
# Users can choose from the following tickets:
# 5678B
# 9876C
# 2345D
# 6789E
# 3456F
# 8765G
# 4321H
# 7890J
# 5432K
# 2109L
# 8765M
# 1357N
# 2468P
# 6543Q
# 7891R
# 3579S
# 9821T
# 4682U
# 5763V
# 1234A

# -Users can buy a minimum of 1 and a maximum of 2 tickets.
# -Payment is accepted in cash, and each ticket costs 1 USD.
# -After choosing tickets and quantity, the system prompts the user to pay in cash or by bank card.
# -This system only accepts 1 USD and 5 USD bills. The user must choose the bill to use for payment, and the system should return the change if applicable.
# -After payment, the ticket is issued.
# -The user returns to the main menu to play the lottery.
# -The lottery system generates 1 random ticket code.
import random
class Ticket:
    def __init__(self):
        self.tickets = ["5678B", "9876C", "2345D", "6789E", "3456F", "8765G", "4321H", "7890J", "5432K", "2109L", "8765M", "1357N", "2468P", "6543Q", "7891R", "3579S", "9821T", "4682U", "5763V", "1234A"]
        self.costo = 1
        self.billetes_permitidos = [1, 5]
        self.vendidos = []
        self.comprador = ""

    def forma_pago(self):
        print("Seleccione la forma de pago")
        print("1. Efectivo")
        print("2. Tarjeta")
        while True:
            try:
                seleccion = int(input("\nIngrese la opcion de su preferencia (1-2): "))
                if 1 <= seleccion <= 2:
                    return seleccion
                else:
                    print("----Debe ingresar un numero dentro del rango----")
            except ValueError:
                print("\nPor favor, ingrese un valor válido.")

    def cantidad_tickets(self):
        print("Cuantos tickes comprara")
        print("1")
        print("2")
        while True:
            try:
                seleccion = int(input("\nIngrese la opcion de su preferencia (1-2): "))
                if 1 <= seleccion <= 2:
                    return seleccion
                else:
                    print("----No puede comprar mas de 2 tickes ni se aceptan numeros negativos----")
            except ValueError:
                print("\nPor favor, ingrese un valor válido.")

    def pago_efectivo(self, costo_total):
        print("Tenga en cuenta que solo se aceptan billetes de 1 y 5")
        suma_pago = 0
        while True:
            print("ingrese el billete")
            print("$ 1")
            print("$ 5")
            try:
                seleccion = int(input("\nIngresar billete (1 o 5): "))

                if 1 != seleccion !=  5:
                    print("----ingrese un billete permitido----")
                    continue

                suma_pago += seleccion

                if costo_total > suma_pago:
                    print(f"\nBillete ingresado, aun faltan ${costo_total - suma_pago}")
                    continue
                elif suma_pago > costo_total:
                    print(f"\nSu cambio es de ${suma_pago - costo_total}")

                print("Muchas gracias por su compra")
                break
            except ValueError:
                print("\nPor favor, ingrese un valor válido.")

    def eleccion_ticket(self, cantidad):
        while cantidad >= 1:
            for i, ticket in enumerate(self.tickets, 1):
                print(f"{i}. {ticket}")

            try:
                eleccion = int(input(f"Seleccione la opcion de su preferencia (1 - {len(self.tickets)}): "))

                if 1 <= eleccion <= len(self.tickets):
                    codigo = self.codigo_aleatorio()
                    self.vendidos.append({
                        "comprador": self.comprador,
                        "ticket": self.tickets[eleccion-1],
                        "codigo": codigo
                    })
                    cantidad -= 1
                else:
                    print("Ingrese un numero dentro del rango")
            except ValueError:
                print("\nPor favor, ingrese un valor válido.")
    
    def codigo_aleatorio(self):
        codigo_generado = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
        return codigo_generado

    def pago_tarjeta(self, costo_total):
        while True:
            tarjeta = input("\nIngrese los 10 numero de su tarjeta: ").strip()

            if len(tarjeta) != 10:
                print("-----La contraseña debe contar con 10 numeros.-----")
            else:
                print(f"\nSe debitaron de su tarjeta ${costo_total}")
                break

    def ver_tickets_ventidos(self):
        for i, ticket in enumerate(self.vendidos, 1):
            print(f"Comprador: {ticket['comprador']} --- Ticket: {ticket['ticket']} --- Codigo: {ticket['codigo']}")


    def principal(self):
        while True:
            self.comprador = input("Ingrese a nombre de quien estara el billete: ")
            cantidad_tickets = self.cantidad_tickets()
            self.eleccion_ticket(cantidad_tickets)
            forma_pago = self.forma_pago()
            if forma_pago == 1:
                self.pago_efectivo(cantidad_tickets * self.costo)
            else:
                self.pago_tarjeta(cantidad_tickets * self.costo)
            seguir = input("Presione Y para salir del sistema, cualquier otra tecla para continuar: ").upper().strip()
            if seguir == "Y":
                self.ver_tickets_ventidos()
                break
            

tic = Ticket()
tic.principal()