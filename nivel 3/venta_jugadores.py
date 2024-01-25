# 5. Manchester United FC Talent Acquisition System:

# The Manchester United FC is in search of new talents to enhance its player roster. The head coach aims to recruit two forwards, two midfielders, a right-back, a defender, and a goalkeeper. To achieve this, the club needs to sell some players to fund these new signings. Develop a system to assist the head coach in choosing which players can be sold based on their market price, salary, position, and performance within the club.

# Current Squad:

# Goalkeepers:

# André Onana - Price: £25,000,000 - Salary: £15,000,000 - Performance: Good
# Altay Bayindir - Price: £5,000,000 - Salary: £5,000,000 - Performance: Normal
# Tom Heaton - Price: £5,000,000 - Salary: £2,000,000 - Performance: Normal
# Defenders:

# Victor Lindelof - Price: £10,000,000 - Salary: £7,000,000 - Performance: Normal
# Harry Maguire - Price: £15,000,000 - Salary: £10,000,000 - Performance: Good
# Raphael Varane - Price: £15,000,000 - Salary: £10,000,000 - Performance: Good
# Lisandro Martínez - Price: £15,000,000 - Salary: £8,000,000 - Performance: Good
# Jonny Evans - Price: £7,000,000 - Salary: £4,000,000 - Performance: Good
# Willy Kambwala - Price: £4,000,000 - Salary: £1,000,000 - Performance: Normal
# Rhys Bennett - Price: £4,000,000 - Salary: £2,000,000 - Performance: Normal
# Right Side:

# Diogo Dalot - Price: £40,000,000 - Salary: £10,000,000 - Performance: Good
# Aaron Wan Bissaka - Price: £30,000,000 - Salary: £9,000,000 - Performance: Normal
# Left Side:

# Luke Shaw - Price: £40,000,000 - Salary: £16,000,000 - Performance: Good
# Sergio Reguilón - Price: £20,000,000 - Salary: £8,000,000 - Performance: Normal
# Tyrell Malacia - Price: £16,000,000 - Salary: £7,000,000 - Performance: Normal
# Midfielders:

# Sofyan Amrabat - Price: £25,000,000 - Salary: £9,000,000 - Performance: Normal
# Mason Mount - Price: £25,000,000 - Salary: £12,000,000 - Performance: Normal
# Carlos Casemiro - Price: £25,000,000 - Salary: £15,000,000 - Performance: Good
# Bruno Fernandes - Price: £50,000,000 - Salary: £11,000,000 - Performance: Good
# Christian Eriksen - Price: £25,000,000 - Salary: £8,000,000 - Performance: Normal
# Scott McTominay - Price: £40,000,000 - Salary: £8,000,000 - Performance: Good
# Hannibal Mejbri - Price: £12,000,000 - Salary: £2,000,000 - Performance: Good
# Kobbie Mainoo - Price: £12,000,000 - Salary: £2,000,000 - Performance: Good
# Daniel Gore - Price: £9,000,000 - Salary: £2,000,000 - Performance: Normal
# Strikers:

# Alejandro Garnacho - Price: £12,000,000 - Salary: £10,000,000 - Performance: Good
# Rasmus Hojlund - Price: £20,000,000 - Salary: £7,000,000 - Performance: Good
# Marcus Rashford - Price: £25,000,000 - Salary: £10,000,000 - Performance: Good
# Antony - Price: £25,000,000 - Salary: £10,000,000 - Performance: Normal
# Anthony Martial - Price: £18,000,000 - Salary: £4,000,000 - Performance: Normal
# Facundo Pellistri - Price: £18,000,000 - Salary: £6,000,000 - Performance: Good

# Market Players:

# Goalkeepers:

# Andriy Lunin - Price: £30,000,000 - Salary: £10,000,000 - Performance: Good
# Dominic Livakovic - Price: £15,000,000 - Salary: £9,000,000 - Performance: Good
# Rui Patricio - Price: £10,000,000 - Salary: £7,000,000 - Performance: Normal
# Yassine Bounou - Price: £14,000,000 - Salary: £9,000,000 - Performance: Normal
# Midfielders:

# Enzo Fernández - Price: £35,000,000 - Salary: £15,000,000 - Performance: Good
# Jamal Musiala - Price: £30,000,000 - Salary: £10,000,000 - Performance: Good
# Arda Guler - Price: £18,000,000 - Salary: £9,000,000 - Performance: Normal
# Right Side:

# Achraf Hakimi - Price: £20,000,000 - Salary: £15,000,000 - Performance: Good
# Jeremie Frimpong - Price: £12,000,000 - Salary: £8,000,000 - Performance: Good
# Ronald Araujo - Price: £15,000,000 - Salary: £10,000,000 - Performance: Good
# Strikers:

# Victor Osimhen - Price: £30,000,000 - Salary: £12,000,000 - Performance: Good
# Harry Kane - Price: £40,000,000 - Salary: £15,000,000 - Performance: Good
# Karim Benzema - Price: £20,000,000 - Salary: £20,000,000 - Performance: Normal

class Sistema_Venta:
    def __init__(self):
        self.goalkeppers = [
            {
                'name': 'André Onana',
                'Price': 25000000,
                'Salary': 15000000,
                'Performance': 'Good',
            },
            {
                'name': 'Altay Bayindir',
                'Price': 5000000,
                'Salary': 5000000,
                'Performance': 'Normal',
            },
            {
                'name': 'Tom Heaton',
                'Price': 5000000,
                'Salary': 2000000,
                'Performance': 'Normal',
            },
        ]

        self.defenders = [
            {
                'name': 'Victor Lindelof',
                'Price': 10000000,
                'Salary': 7000000,
                'Performance': 'Normal',
            },
            {
                'name': 'Harry Maguire',
                'Price': 15000000,
                'Salary': 10000000,
                'Performance': 'Good',
            },
            {
                'name': 'Raphael Varane',
                'Price': 15000000,
                'Salary': 10000000,
                'Performance': 'Good',
            },
            {
                'name': 'Lisandro Martínez',
                'Price': 15000000,
                'Salary': 8000000,
                'Performance': 'Good',
            },
            { 
                'name': 'Jonny Evans', 
                'Price': 7000000, 
                'Salary': 4000000, 
                'Performance': 'Good' 
            },
            {
                'name': 'Willy Kambwala',
                'Price': 4000000,
                'Salary': 1000000,
                'Performance': 'Normal',
            },
            {
                'name': 'Rhys Bennett',
                'Price': 4000000,
                'Salary': 2000000,
                'Performance': 'Normal',
            },
        ]
        self.rightside = [
            {
                'name': 'Diogo Dalot',
                'Price': 40000000,
                'Salary': 10000000,
                'Performance': 'Good',
            },
            {
                'name': 'Aaron Wan Bissaka',
                'Price': 30000000,
                'Salary': 9000000,
                'Performance': 'Normal',
            },
        ]
        self.leftside = [
            { 
                'name': 'Luke Shaw', 
                'Price': 40000000, 
                'Salary': 16000000, 
                'Performance': 'Good' 
            },
            {
                'name': 'Sergio Reguilón',
                'Price': 20000000,
                'Salary': 8000000,
                'Performance': 'Normal',
            },
            {
                'name': 'Tyrell Malacia',
                'Price': 16000000,
                'Salary': 7000000,
                'Performance': 'Normal',
            },
        ]
        self.midfielders = [
            {
                'name': 'Sofyan Amrabat',
                'Price': 25000000,
                'Salary': 9000000,
                'Performance': 'Normal',
            },
            {
                'name': 'Mason Mount',
                'Price': 25000000,
                'Salary': 12000000,
                'Performance': 'Normal',
            },
            {
                'name': 'Carlos Casemiro',
                'Price': 25000000,
                'Salary': 15000000,
                'Performance': 'Good',
            },
            {
                'name': 'Bruno Fernandes',
                'Price': 50000000,
                'Salary': 11000000,
                'Performance': 'Good',
            },
            {
                'name': 'Christian Eriksen',
                'Price': 25000000,
                'Salary': 8000000,
                'Performance': 'Normal',
            },
            {
                'name': 'Scott McTominay',
                'Price': 40000000,
                'Salary': 8000000,
                'Performance': 'Good',
            },
            {
                'name': 'Hannibal Mejbri',
                'Price': 12000000,
                'Salary': 2000000,
                'Performance': 'Good',
            },
            {
                'name': 'Kobbie Mainoo',
                'Price': 12000000,
                'Salary': 2000000,
                'Performance': 'Good',
            },
            {
                'name': 'Daniel Gore',
                'Price': 9000000,
                'Salary': 2000000,
                'Performance': 'Normal',
            },
        ]
        self.strikers = [
            {
                'name': 'Alejandro Garnacho',
                'Price': 12000000,
                'Salary': 10000000,
                'Performance': 'Good',
            },
            {
                'name': 'Rasmus Hojlund',
                'Price': 20000000,
                'Salary': 7000000,
                'Performance': 'Good',
            },
            {
                'name': 'Marcus Rashford',
                'Price': 25000000,
                'Salary': 10000000,
                'Performance': 'Good',
            },
            { 
                'name': 'Antony', 
                'Price': 25000000, 
                'Salary': 10000000, 
                'Performance': 'Normal' 
            },
            {
                'name': 'Anthony Martial',
                'Price': 18000000,
                'Salary': 4000000,
                'Performance': 'Normal',
            },
            {
                'name': 'Facundo Pellistri',
                'Price': 18000000,
                'Salary': 6000000,
                'Performance': 'Good',
            },
        ]

        self.market_players = {
                'goalkeppers': [
                    {
                        'name': 'Andriy Lunin',
                        'Price': 30000000,
                        'Salary': 10000000,
                        'Performance': 'Good',
                    },
                    {
                        'name': 'Dominic Livakovic',
                        'Price': 15000000,
                        'Salary': 9000000,
                        'Performance': 'Good',
                    },
                    {
                        'name': 'Rui Patricio',
                        'Price': 10000000,
                        'Salary': 7000000,
                        'Performance': 'Normal',
                    },
                    {
                        'name': 'Yassine Bounou',
                        'Price': 14000000,
                        'Salary': 9000000,
                        'Performance': 'Normal',
                    },
                ],
                'midfielders': [
                    {
                        'name': 'Enzo Fernández',
                        'Price': 35000000,
                        'Salary': 15000000,
                        'Performance': 'Good',
                    },
                    {
                        'name': 'Jamal Musiala',
                        'Price': 30000000,
                        'Salary': 10000000,
                        'Performance': 'Good',
                    },
                    {
                        'name': 'Arda Guler',
                        'Price': 18000000,
                        'Salary': 9000000,
                        'Performance': 'Normal',
                    },
                ],
                'rightside': [
                    {
                        'name': 'Achraf Hakimi',
                        'Price': 20000000,
                        'Salary': 15000000,
                        'Performance': 'Good',
                    },
                    {
                        'name': 'Jeremie Frimpong',
                        'Price': 12000000,
                        'Salary': 8000000,
                        'Performance': 'Good',
                    },
                    {
                        'name': 'Ronald Araujo',
                        'Price': 15000000,
                        'Salary': 10000000,
                        'Performance': 'Good',
                    },
                ],
                'strikers': [
                    {
                        'name': 'Victor Osimhen',
                        'Price': 30000000,
                        'Salary': 12000000,
                        'Performance': 'Good',
                    },
                    {
                        'name': 'Harry Kane',
                        'Price': 40000000,
                        'Salary': 15000000,
                        'Performance': 'Good',
                    },
                    {
                        'name': 'Karim Benzema',
                        'Price': 20000000,
                        'Salary': 20000000,
                        'Performance': 'Normal',
                    },
                ],
            }
    def evaluate_selling_needs(self, players):
        # Lógica para evaluar la necesidad de venta según las posiciones requeridas
        # Devolver una lista de jugadores que cumplen con los requisitos
        # Puedes adaptar esto según las necesidades específicas del entrenador
        players_to_sell = []

        # Ejemplo: El entrenador quiere vender a jugadores con rendimiento 'Normal'
        for player in players:
            if player['Performance'] == 'Normal':
                players_to_sell.append(player)

        return players_to_sell

    def calculate_sell_score(self, player):
        # Lógica para asignar puntuación basada en precio, salario, rendimiento, etc.
        # Devolver la puntuación
        sell_score = player['Price'] - player['Salary']
        return sell_score

    def suggest_players_for_sale(self):
        # Obtener la lista de jugadores sugeridos para la venta
        players_to_sell = self.evaluate_selling_needs(self.goalkeppers + self.defenders + self.rightside + self.leftside + self.midfielders + self.strikers)
        
        # Calcular la puntuación de venta para cada jugador
        for player in players_to_sell:
            player["sell_score"] = self.calculate_sell_score(player)

        # Ordenar la lista de jugadores según la puntuación de venta
        players_to_sell.sort(key=lambda x: x["sell_score"], reverse=True)

        return players_to_sell

# Crear una instancia de la clase
sistema_venta = Sistema_Venta()

# Obtener la lista de jugadores sugeridos para la venta
suggested_players_for_sale = sistema_venta.suggest_players_for_sale()

# Imprimir la lista sugerida
current_position = None

for player in suggested_players_for_sale:
    # Utilizar la clave del diccionario como posición
    player_position = None
    for position, players in sistema_venta.__dict__.items():
        if player in players:
            player_position = position
            break

    # Imprimir la posición como un título cuando cambia
    if player_position != current_position:
        current_position = player_position
        print(f"\nPosition: {current_position}")

    # Imprimir la información del jugador
    print(f"{player['name']} - Performance: {player['Performance']} - Sell Score: {player['sell_score']}")