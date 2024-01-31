# You are the Manager of Manchester United FC, and your objective is to defeat Tottenham Hotspur. To achieve this, you must consider the power level of your players and choose the appropriate line-up against your opponent. Select 11 players from your team.

# Tottenham Hotspur:
# Goalkeepers

# Hugo Lloris 85 pts
# Guglielmo Vicario 79 pts
# Fraser Forster 79 pts
# Brandon Austin 79 pts
# Defenders
# Eric Dier 80 pts
# Cristian Romero 80 pts
# Davinson Sánchez 74 pts
# Japhet Tanganga 70 pts
# Matt Doherty 70 pts
# Djed Spence 70 pts
# Sergio Reguilón 74 pts
# Ben Davies 76 pts
# Joe Rodon 70 pts
# Mislav Orsic 71 pts
# Midfielders
# Oliver Skipp 70 pts
# Pierre-Emile Højbjerg 70 pts
# Yves Bissouma 72 pts
# James Maddison 74 pts
# Giovani Lo Celso 78 pts
# Ryan Sessegnon 80 pts
# Dejan Kulusevski 60 pts
# Pape Sarr 65 pts
# Rodrigo Bentancur 65 pts
# Oliver Skipp 65 pts
# Forwards
# Son Heung-Min 78 pts
# Richarlison 82 pts
# Bryan Gil 80 pts
# Timo Werner 82 pts
# Brennan Johnson 70 pts
# Manor Solomon 70 pts
# Alejo Véliz 75 pts
# Dane Scarlett 75 pts
# Manchester United:
# Goalkeepers

# André Onana 80 pts
# Tom Heaton 75 pts
# Altay Bayindir 69 pts
# Defenders
# Victor Lindelöf 80 pts
# Harry Maguire 82 pts
# Lisandro Martínez 82 pts
# Tyrell Malacia 67 pts
# Raphaël Varane 80 pts
# Diogo Dalot 89 pts
# Luke Shaw 89 pts
# Aaron Wan-Bissaka 70 pts
# Midfielders
# Sofyan Amrabat 76 pts
# Scott McTominay 80 pts
# Bruno Fernandes 88 pts
# Christian Eriksen 67 pts
# Mason Mount 77 pts
# Kobbie Mainoo 65 pts
# Daniel Gore 60 pts
# Forwards
# Anthony Martial 50 pts
# Marcus Rashford 76 pts
# Antony 75 pts
# Rasmus Højlund 80 pts
# Alejandro Garnacho 85 pts
# Facundo Pellistri: 75 pts
# How it works: The system will randomly generate 11 Tottenham Hotspur players, comprising 1 goalkeeper, 3 midfielders, and 3 strikers.

# As the Manager of Manchester United, you must select 11 players following the same system: 4-3-3.

import random

class Equipo_contrario:
    def __init__(self):
        self.Goalkeepers = { 
            "Hugo Lloris": 85, "Guglielmo Vicario": 79, "Fraser Forster": 79, "Brandon Austin": 79
            }
        self.Defenders = {
            "Eric Dier": 80, "Cristian Romero": 80, "Davinson Sánchez": 74, "Japhet Tanganga": 70, "Matt Doherty": 70, "Djed Spence": 70, "Sergio Reguilón": 74, "Ben Davies": 76, "Joe Rodon": 70, "Mislav Orsic": 71
        }
        self.Midfielders = {
            "Oliver Skipp": 70, "Pierre-Emile Højbjerg": 70, "Yves Bissouma": 72, "James Maddison": 74, "Giovani Lo Celso": 78, "Ryan Sessegnon": 80, "Dejan Kulusevski": 60, "Pape Sarr": 65, "Rodrigo Bentancur": 65, "Oliver Skipp": 65
        }
        self.Forwards = {
            "Son Heung-Min": 78, "Richarlison": 82, "Bryan Gil": 80, "Timo Werner": 82, "Brennan Johnson": 70, "Manor Solomon": 70, "Alejo Véliz": 75, "Dane Scarlett": 75
        }

    def equipoAleatorio(self):
        # Seleccionar un portero aleatorio con sus puntos y posicion
        goalkeeper = random.choice([(name, 'Goalkeeper', points) for name, points in self.Goalkeepers.items()])

        # Seleccionar 4 defensores aleatorios con sus puntos y posicion
        defenders = random.sample([(name, 'Defender', points) for name, points in self.Defenders.items()], 4)

        # Seleccionar 3 mediocampistas aleatorios con sus puntos y posicion
        midfielders = random.sample([(name, 'Midfielder', points) for name, points in self.Midfielders.items()], 3)

        # Seleccionar 3 delanteros aleatorios con sus puntos y posicion
        forwards = random.sample([(name, 'Forward', points) for name, points in self.Forwards.items()], 3)

        # Combinar las listas para formar el equipo completo
        # goalkeeper va entre [] para asegurarnos que sea una lista ya que random.choice retorna un unico elemento
        team = [goalkeeper] + defenders + midfielders + forwards
        # print(team)
        return team

    
class Manchester:
    def __init__(self):
        self.Goalkeepers = {
            "André Onana": 80, "Tom Heaton": 75, "Altay Bayindir": 69,
        }
        self.Defenders = {
            "Victor Lindelöf": 80, "Harry Maguire": 82, "Lisandro Martínez": 82, "Tyrell Malacia": 67, "Raphaël Varane": 80, "Diogo Dalot": 89, "Luke Shaw": 89, "Aaron Wan-Bissaka": 70,
        }
        self.Midfielders = {
            "Sofyan Amrabat": 76, "Scott McTominay": 80, "Bruno Fernandes": 88, "Christian Eriksen": 67, "Mason Mount": 77, "Kobbie Mainoo": 65, "Daniel Gore": 60,
        }
        self.Forwards = {
            "Anthony Martial": 50, "Marcus Rashford": 76, "Antony": 75, "Rasmus Højlund": 80, "Alejandro Garnacho": 85, "Facundo Pellistri": 75,
        }

    def elegirEquipo(self, contrario):
        # Obtener el equipo aleatorio del equipo contrario
        equipoContrario = contrario.equipoAleatorio()

        # Filtrar jugadores del Manchester United por posición
        porterosManchester = [(name, 'Goalkeeper', points) for name, points in self.Goalkeepers.items()]
        defensoresManchester = [(name, 'Defender', points) for name, points in self.Defenders.items()]
        mediocampistasManchester = [(name, 'Midfielder', points) for name, points in self.Midfielders.items()]
        delanterosManchester = [(name, 'Forward', points) for name, points in self.Forwards.items()]

        # Ordenar jugadores por puntos de mayor a menor
        porterosManchester.sort(key=lambda x: x[2], reverse=True)
        defensoresManchester.sort(key=lambda x: x[2], reverse=True)
        mediocampistasManchester.sort(key=lambda x: x[2], reverse=True)
        delanterosManchester.sort(key=lambda x: x[2], reverse=True)

        # Seleccionar la cantidad correspondiente para cada posición
        mejorPortero = porterosManchester[0]
        mejoresDefensores = defensoresManchester[:4]
        mejoresMediocampistas = mediocampistasManchester[:3]
        mejoresDelanteros = delanterosManchester[:3]

        # Combinar los mejores jugadores en una lista para formar el equipo del Manchester United
        equipoManchester = [mejorPortero] + mejoresDefensores + mejoresMediocampistas + mejoresDelanteros

        # Retornar los equipos seleccionados
        return equipoManchester, equipoContrario
    
# Ejemplo de uso
ejemplo = Equipo_contrario()
prueba1 = Manchester()
manchester, contra = prueba1.elegirEquipo(ejemplo)

print("\nEquipo Manchester United:")
for jugador in manchester:
    if jugador is not None:
        print(f"{jugador[0]} - {jugador[1]} - Puntos: {jugador[2]}")
    else:
        print("Error: No se pudo seleccionar un jugador del Manchester United.")

print("\nEquipo Contrario:")
if all(jugador is not None for jugador in contra):
    for jugador in contra:
        print(f"{jugador[0]} - {jugador[1]} - Puntos: {jugador[2]}")
else:
    print("Error: No se pudo seleccionar un jugador del equipo contrario.")