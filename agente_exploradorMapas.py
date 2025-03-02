import random
class AgenteExplorador:
    def __init__(self, mapa):
        self.mapa = mapa
        self.posicion = (0, 0)  # El agente empieza en la esquina superior izquierda
        self.visitadas = set()

    def mover(self, direccion):
        x, y = self.posicion
        if direccion == 'arriba':
            self.posicion = (x - 1, y)
        elif direccion == 'abajo':
            self.posicion = (x + 1, y)
        elif direccion == 'izquierda':
            self.posicion = (x, y - 1)
        elif direccion == 'derecha':
            self.posicion = (x, y + 1)

    def explorar(self):
        direcciones = ['arriba', 'abajo', 'izquierda', 'derecha']
        while True:
            # Si ya visitó la posición, salta a la siguiente
            if self.posicion in self.visitadas:
                break
            self.visitadas.add(self.posicion)
            print(f"Explorando: {self.posicion}")
            self.mover(random.choice(direcciones))  # Movimiento aleatorio para explorar

# Mapa representado como una cuadrícula de 5x5
mapa = [[0 for _ in range(5)] for _ in range(5)]
agente = AgenteExplorador(mapa)
agente.explorar()