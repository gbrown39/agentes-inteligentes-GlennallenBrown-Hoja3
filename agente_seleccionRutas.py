class AgenteUtilidad:
    def __init__(self, entorno):
        self.entorno = entorno
        self.posicion = (0, 0)

    def evaluar_utilidad(self, camino):
        return sum(self.entorno[x][y] for x, y in camino)

    def seleccionar_ruta(self, rutas_posibles):
        mejor_camino = max(rutas_posibles, key=self.evaluar_utilidad)
        return mejor_camino

# Entorno de recompensas 5x5
entorno = [
    [1, -1, 0, 2, 0],
    [0, 3, 1, 0, -2],
    [-1, 0, 4, -1, 1],
    [2, -3, 0, 1, 0],
    [0, 2, -1, 0, 5]
]

# Rutas posibles representadas como listas de coordenadas
rutas_posibles = [
    [(0, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 0), (1, 1), (2, 2)]
]

agente = AgenteUtilidad(entorno)
mejor_ruta = agente.seleccionar_ruta(rutas_posibles)
print("La mejor ruta seleccionada es:", mejor_ruta)