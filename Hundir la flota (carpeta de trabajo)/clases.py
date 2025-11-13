import numpy as np
import random
from variables import dimension_tablero, agua, barco, tocado, fallo

class Tablero:
    def __init__(self, id_jugador, barcos):
        self.id_jugador = id_jugador
        self.barcos = barcos
        self.tablero = np.full((dimension_tablero, dimension_tablero), agua)
        self.tablero_disparos = np.full((dimension_tablero, dimension_tablero), agua)
        self.colocar_barcos()
    
    def colocar_barcos(self):
        """Coloca los barcos aleatoriamente en el tablero"""
        for _, info in self.barcos.items():
            for _ in range(info["cantidad"]):
                colocado = False
                while not colocado:
                    fila = random.randint(0, dimension_tablero - 1)
                    col = random.randint(0, dimension_tablero - 1)
                    orientacion = random.choice(["H", "V"])
                    if self._puede_colocar(fila, col, info["eslora"], orientacion):
                        self._colocar(fila, col, info["eslora"], orientacion)
                        colocado = True

    def _puede_colocar(self, fila, col, eslora, orientacion):
        """Comprueba si se puede colocar un barco en la posición indicada"""
        if orientacion == "H":
            if col + eslora > dimension_tablero:
                return False
            for i in range(eslora):
                if self.tablero[fila, col + i] != agua:
                    return False
        else:  # Vertical
            if fila + eslora > dimension_tablero:
                return False
            for i in range(eslora):
                if self.tablero[fila + i, col] != agua:
                    return False
        return True
    
    def _colocar(self, fila, col, eslora, orientacion):
        """Coloca efectivamente un barco en el tablero"""
        if orientacion == "H":
            for i in range(eslora):
                self.tablero[fila, col + i] = barco
        else:  # Vertical
            for i in range(eslora):
                self.tablero[fila + i, col] = barco

    def disparar(self, fila, col):
        """Procesa un disparo en el tablero"""
        if self.tablero[fila, col] == barco:
            self.tablero[fila, col] = tocado
            print("¡Impacto!")
            return True
        elif self.tablero[fila, col] in [tocado, fallo]:
            print("Ya habías disparado aquí.")
            return None
        else:
            self.tablero[fila, col] = fallo
            print("Agua...")
            return False

    def registrar_disparo(self, fila, col, resultado):
        """Registra el disparo en el tablero de disparos (vista del jugador)"""
        self.tablero_disparos[fila, col] = tocado if resultado else fallo

    def mostrar_tablero(self, mostrar_barcos=True):
        """Muestra el tablero por pantalla"""
        print("   " + " ".join(map(str, range(dimension_tablero))))
        tablero_a_mostrar = self.tablero if mostrar_barcos else self.tablero_disparos
        for i, fila in enumerate(tablero_a_mostrar):
            print(f"{i:2} " + " ".join(fila))

    def quedan_barcos(self):
        """Comprueba si quedan barcos vivos"""
        return np.any(self.tablero == barco)

