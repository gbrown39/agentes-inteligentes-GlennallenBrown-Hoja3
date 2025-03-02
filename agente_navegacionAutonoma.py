from collections import deque

def bfs(laberinto, inicio, meta):
    filas, columnas = len(laberinto), len(laberinto[0])
    visitado = set()
    cola = deque([(inicio, [inicio])])  # (posición, camino)
    
    while cola:
        (x, y), camino = cola.popleft()
        if (x, y) == meta:
            return camino
        
        if (x, y) not in visitado:
            visitado.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] == 0 and (nx, ny) not in visitado:
                    cola.append(((nx, ny), camino + [(nx, ny)]))
    return None

# Laberinto 5x5, 0 es camino libre, 1 es pared
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0)
meta = (4, 4)
camino = bfs(laberinto, inicio, meta)
print("Camino encontrado:", camino)