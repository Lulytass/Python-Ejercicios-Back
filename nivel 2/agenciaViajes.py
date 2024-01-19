# 2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

# Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
# Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
# Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
# Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
# Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

# Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
# 12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

# Clue: You could consider the user's budget


class Usuario:
    def __init__(self):
        self.preferencia_epoca = None
        self.presupuesto = None
        self.preferencia_actividades = None

    def validar_entrada(self, valor, opciones):
        return any(opcion.lower() in valor.lower() for opcion in opciones)

    def pedir_temporada(self):
        while True:
            temporada = input("¿En qué temporada quieres viajar? (Invierno, Verano, Primavera, Otoño): ").capitalize()
            if self.validar_entrada(temporada, ["Invierno", "Verano", "Primavera", "Otoño"]):
                self.preferencia_epoca = temporada
                return True
            else:
                print("Por favor, ingresa una temporada válida.")

    def pedir_presupuesto(self):
        while True:
            try:
                presupuesto = int(input("¿Cuál es tu presupuesto para el viaje?: $"))
                if presupuesto > 0:
                    self.presupuesto = presupuesto
                    return True
                else:
                    print("Por favor, ingresa un presupuesto válido.")
            except ValueError:
                print("Por favor, ingresa un valor numérico.")

    def pedir_actividad(self):
        while True:
            actividad = input("¿Qué actividad te llama más la atención hacer? (Esqui, Alpes Suizos, Senderismo, Deportes Extremos, Actividades de Playa, Recorrido Cultural e Historico): ").capitalize()
            if self.validar_entrada(actividad, ["Esqui"," Alpes Suizos", "Senderismo","Deportes Extremos", "Actividades de Playa", "Recorrido Cultural e Historico"]):
                self.preferencia_actividades = actividad
                return True
            else:
                print("Por favor, ingresa una actividad válida de la lista proporcionada.")

class Agencia:
    def __init__(self):
        self.destinos = {
            "Invierno": {
                "Andorra": ["Esqui"],
                "Suiza": ["Alpes Suizos"]
            },
            "Verano": {
                "España": ["Senderismo", "Deportes Extremos"],
                "Portugal": ["Actividades de Playa"]
            },
            "Primavera": {
                "Francia": ["Deportes Extremos"],
                "Italia": ["Recorrido Cultural e Historico"]
            },
            "Otoño": {
                "Bélgica": ["Senderismo", "Deportes Extremos"],
                "Austria": ["Recorrido Cultural e Historico"]
            },
        }
        self.precios = {
            "Invierno": 100,
            "Otoño": 200,
            "Primavera": 300,
            "Verano": 400
        }

    def determinar_destino(self, temporada, presupuesto, actividad):
        destinos_temporada = self.destinos.get(temporada, {})
        destinos_posibles_temporada = []
        destinos_preferido = []

        for pais, actividades_disponibles in destinos_temporada.items():
            precio = self.precios.get(temporada, 0)
            
            if actividad in actividades_disponibles and precio <= presupuesto:
                destinos_preferido.append(
                    {
                        "Pais": pais,
                        "Temporada": temporada,
                        "Actividad": actividades_disponibles,
                        "Precio": precio
                    }
                )
            elif precio <= presupuesto:
                destinos_posibles_temporada.append(
                    {
                        "Temporada": temporada,
                        "Pais": pais,
                        "Actividad": actividades_disponibles,
                        "Precio": precio
                    }
                )

        mensaje_destino = ""

        if destinos_preferido:
            print(f"\n-----Destinos coincidentes dentro de un presupuesto de ${presupuesto}-----")
            for i, datos in enumerate(destinos_preferido, start=1):
                mensaje_destino += f"\nTemporada: {datos['Temporada']}\nPais: {datos['Pais']}\nPrecio: ${datos['Precio']}\nActividades: {', '.join(datos['Actividad'])}."
        elif destinos_posibles_temporada:
            print(f"\n-----Destinos en {temporada} dentro de un presupuesto de ${presupuesto}-----")
            for i, datos in enumerate(destinos_posibles_temporada, start=1):
                mensaje_destino += f"\nPais: {datos['Pais']}\nPrecio: ${datos['Precio']}\nActividades: {', '.join(datos['Actividad'])}."

        if not destinos_preferido:
            # Buscar destinos en otras temporadas con la actividad deseada
            destinos_en_otras_temporadas = []

            for otra_temporada, destinos_otra_temporada in self.destinos.items():
                if otra_temporada != temporada:
                    for pais_otra_temporada, actividades_otra_temporada in destinos_otra_temporada.items():
                        precio_otra_temporada = self.precios.get(otra_temporada, 0)
                        if precio_otra_temporada <= presupuesto and actividad in actividades_otra_temporada:
                            destinos_en_otras_temporadas.append(
                                {
                                    "Pais": pais_otra_temporada,
                                    "Temporada": otra_temporada,
                                    "Actividad": actividades_otra_temporada,
                                    "Precio": precio_otra_temporada
                                }
                            )

            if destinos_en_otras_temporadas:
                for i, datos in enumerate(destinos_en_otras_temporadas, start=1):
                    mensaje_destino += f"\nNo hay destinos disponibles para {actividad} en {temporada} dentro de tu presupuesto. Sin embargo, puedes considerar {datos['Pais']} en {datos['Temporada']}. Precio: ${datos['Precio']}. Podrás disfrutar de las siguientes actividades: {', '.join(datos['Actividad'])}."
            else:
                mensaje_destino = f"\nNo hay destinos disponibles para {actividad} en {temporada} dentro de tu presupuesto."

        return mensaje_destino


def main():
    print("Bienvenido a la agencia de viajes")

    usuario = Usuario()

    if usuario.pedir_temporada() and usuario.pedir_presupuesto() and usuario.pedir_actividad():
        agencia = Agencia()
        destino_recomendado = agencia.determinar_destino(usuario.preferencia_epoca, usuario.presupuesto, usuario.preferencia_actividades)
        print(destino_recomendado)

if __name__ == "__main__":
    main()