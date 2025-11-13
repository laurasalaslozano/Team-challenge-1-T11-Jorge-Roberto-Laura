import numpy as np

# Dimensiones del tablero
dimension_tablero = 10

# Barcos y sus dimensiones
varios_barcos = {
    "barco1": {"cantidad": 1, "eslora": 4},  # 1 barco de 4 casillas
    "barco2": {"cantidad": 2, "eslora": 3},  # 2 barcos de 3 casillas
    "barco3": {"cantidad": 3, "eslora": 2},  # 3 barcos de 2 casillas
    "barco4": {"cantidad": 4, "eslora": 1}   # 4 barcos de 1 casilla
}

# Representación del tablero
agua = "_"
barco = "B"
tocado = "X"
fallo = "F"

# Jugadores
variable_jugador = "Jugador"
variable_maquina = "Maquina"
