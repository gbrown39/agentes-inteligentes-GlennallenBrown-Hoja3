import random
import time

class AgentePatrullaje:
    def __init__(self, ruta):
        self.ruta = ruta
        self.posicion = 0  # El agente empieza en la primera posición

    def detectar_obstaculo(self):
        # Simula la detección de un obstáculo aleatorio en la ruta
        return random.choice([True, False])

    def mover(self):
        if self.detectar_obstaculo():
            print("¡Obstáculo detectado! El agente cambia de dirección.")
            # Cambiar la dirección aleatoriamente
            self.posicion += random.choice([-1, 1])

        # Asegurarse de que el agente no se mueva fuera de la ruta
        self.posicion = max(0, min(self.posicion, len(self.ruta) - 1))
        print(f"Agente moviéndose a la posición {self.ruta[self.posicion]}")

    def patrullar(self):
        for _ in range(10):  # Simulamos 10 movimientos
            self.mover()
            time.sleep(1)  # Pausa de 1 segundo para ver el movimiento

# Entorno de ruta predefinida
ruta = ['Posición 1', 'Posición 2', 'Posición 3', 'Posición 4', 'Posición 5']
agente = AgentePatrullaje(ruta)
agente.patrullar()