# 1. Create an online banking system with the following features:

# * Users must be able to log in with a username and password.
# * If the user enters the wrong credentials three times, the system must lock them out.
# * The initial balance in the bank account is $2000.
# * The system must allow users to deposit, withdraw, view, and transfer money.
# * The system must display a menu for users to perform transactions.
class Banco:
    def __init__(self):
        self.name = ""
        self.password = ""
        self.balance = 2000
        self.attempts = 3

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

    def menu(self):
        while True:
            print("\nSeleccione alguna de las siguientes opciones:")
            print("1. Deposito")
            print("2. Retiro")
            print("3. Ver")
            print("4. Transferir")
            print("5. Cambios de moneda")
            print("6. Salir")

            opcion_input = input("Ingrese una opción: ")
            
            if not opcion_input.isdigit():
                print("Por favor, ingrese un número válido.")
                continue

            opcion = int(opcion_input)

            match opcion:
                case 1:
                    while True:
                        deposito_input = input("Ingrese monto a depositar: ")
                        if deposito_input.isdigit() and int(deposito_input) > 0:
                            deposito = int(deposito_input)
                            self.balance += deposito
                            print("Deposito realizado exitosamente.")
                            break
                        else:
                            print("Por favor, ingrese un monto válido.")
                case 2:
                    while True:
                        retiro_input = input("Ingrese monto a retirar: ")
                        if retiro_input.isdigit() and int(retiro_input) > 0:
                            retiro = int(retiro_input)
                            if retiro <= self.balance:
                                self.balance -= retiro
                                print("Retiro realizado exitosamente.")
                                break
                            else:
                                print("No tiene suficientes fondos para retirar esa cantidad.")
                        else:
                            print("Por favor, ingrese un monto válido.")
                case 3:
                    print("Su balance actual es: ", self.balance)
                case 4:
                    while True:
                        transferir_input = input("Ingrese monto a transferir: ")
                        if transferir_input.isdigit() and int(transferir_input) > 0:
                            transferir = int(transferir_input)
                            self.balance -= transferir
                            print("Transferencia realizada exitosamente.")
                            break
                        else:
                            print("Por favor, ingrese un monto válido.")
                case 5:
                    cambio = CurrencyConverter(self)
                    cambio.menuMonedas()
                case 6:
                    break
                case _:
                    print("Opción no válida. Intente nuevamente.")

# 2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
# * 		The user must choose their initial currency and the currency they want to exchange to.
# * 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
# * 		If the user decides to withdraw the funds, the system will charge a 1% commission.
# * 		Set a minimum and maximum amount for each currency, it can be of your choice.
# * 		The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.


class CurrencyConverter(Banco):
    def __init__(self, banco_instance):
        self.banco = banco_instance
        self.userCurrency = ""
        self.exchangeCurrency = ""
        self.converted_amount = 0
        self.currency = {
            "CLP": 0.1,
            "ARS": 0.2,
            "USD": 1.0,
            "EUR": 1.3,
            "TRY": 0.03,
            "GBP": 1.5
        }
        self.limits = {
            "CLP": (10, 100000),
            "ARS": (10, 100000),
            "USD": (10, 100000),
            "EUR": (10, 100000),
            "TRY": (10, 100000),
            "GBP": (10, 100000)
        }

    def menuMonedas(self):
        while True:
            print("\nCon qué moneda operará:")
            print("0. CLP")
            print("1. ARS")
            print("2. USD")
            print("3. EUR")
            print("4. TRY")
            print("5. GBP")

            monedaInicial = input("Seleccione la moneda inicial: ")
            monedaCambio = input("Seleccione la moneda a la que cambiará su dinero: ")
            if monedaInicial.isdigit() and 0 <= int(monedaInicial) <= 5 and monedaCambio.isdigit() and 0 <= int(monedaCambio) <= 5:
                self.userCurrency = list(self.currency.keys())[int(monedaInicial)]
                self.exchangeCurrency = list(self.currency.keys())[int(monedaCambio)]
            
                self.converted_amount = float(input(f"Ingrese el monto en {self.userCurrency} que desea cambiar: "))

                if self.converted_amount < self.limits[self.userCurrency][0] or self.converted_amount > self.limits[self.userCurrency][1]:
                    print(f"El monto ingresado no está dentro de los límites permitidos para {self.userCurrency}.")
                    continue
                elif self.converted_amount > self.banco.balance:
                    print(f"No cuenta con el saldo necesario para realizar la operacion")
                    continue
                
                self.cambio()
                self.retiro()

                continuar = input("Si desea realizar otro proceso de cambio presione Y u otro caracter para volver al menu principal: ")
                if continuar != "Y":
                    return
            else:
                print(f"La opcion ingresada no es valida")
                continue

    def retiro(self):
        while True:
            respuesta = input("Desea retirar su dinero? Y/N: ")
            
            if respuesta == "Y":
                commission_rate = 0.01
                commission_amount = self.converted_amount * commission_rate
                
                print(f"Comisión por retiro ({commission_rate*100}%): ${commission_amount}")
                print(f"Total retirado: {self.exchangeCurrency} {self.converted_amount}")
                print(f"Saldo restante: ${self.banco.balance}")
                
                break
            elif respuesta == "N":
                self.menuMonedas() 
                break
            else:
                print("Ingreso una opcion invalida, reintentelo")
                continue

    def cambio(self):
        print(f"El dinero de su cuenta se pasará a {self.exchangeCurrency}")
        
        conversion_rate = self.currency[self.exchangeCurrency]
        self.banco.balance -=  self.converted_amount
        self.converted_amount *=  conversion_rate
        
        print(f"El cambio fue realizado con exito:  {self.exchangeCurrency}{self.converted_amount}")


mi_banco = Banco()
mi_banco.verificar()




    




