# 1. The Big Six of the English Premier League is composed of six teams: Manchester United, Liverpool, Arsenal, Chelsea, Manchester City, and Tottenham Hotspur.
#  Develop a system that generates between 0, 1, and 3 points randomly for each team. 
#  The winner of the Big Six will be the team with the highest accumulated points at the end.
#  Each team will play 3 matches against every opponent. 
#  After the matches, the system will display on-screen the team standings from highest to lowest points.
import random

class Sistema_de_puntos:
    def __init__(self):
        self.equipos = {"Manchester United": 0, "Liverpool": 0, "Arsenal": 0, "Chelsea": 0, "Manchester City": 0, "Tottenham Hotspur": 0}
        self.partidos_a_jugar = 3

    def generar_partidos(self):
        equipos = list(self.equipos.keys())
        for i in range(len(equipos)):
            for j in range(i + 1, len(equipos)):
                equipo1 = equipos[i]
                equipo2 = equipos[j]
                self.jugar_partidos(equipo1, equipo2)

    def jugar_partidos(self, equipo1, equipo2):
        resultados_e1 = []
        resultados_e2 = []
        for _ in range(self.partidos_a_jugar):
            resultado = self.generador_resultados()
            resultados_e1.append(resultado)
            if resultado == 1:
                contrincante = resultado    
            elif resultado == 0:
                contrincante = 3
            else:
                contrincante = 0
            resultados_e2.append(contrincante)
            print(f"{equipo1} vs {equipo2}: {resultado} - {contrincante}")
        self.actualizar_puntos(equipo1, resultados_e1)
        self.actualizar_puntos(equipo2, resultados_e2)

    def actualizar_puntos(self, equipo, resultados):
        self.equipos[equipo] += sum(resultados)

    def generador_resultados(self):
        return random.choice([3, 1, 0])

    def imprimir_resultado(self):
        equipos_ordenados = sorted(self.equipos.items(), key=lambda x: x[1], reverse=True)
        for posicion, (equipo, puntos) in enumerate(equipos_ordenados, start=1):
            print(f"{posicion}: {equipo} - Puntos: {puntos}")

    def principal(self):
        self.generar_partidos()
        self.imprimir_resultado()

prueba = Sistema_de_puntos()
prueba.principal()


