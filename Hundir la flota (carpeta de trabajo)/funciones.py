import random
from variables import dimension_tablero 

# Variable fija de las letras de las columnas
LETRAS_COLUMNAS = 'ABCDEFGHIJ'[:dimension_tablero]

# ¡¡AQUÍ ESTABA EL ERROR GORDO!! → quitamos los espacios de delante
def imprimir_bienvenida():
    #Instrucciones del juego.
    print("\nHola, para disparar, introduce las coordenadas de la siguiente forma: Letra,Número (ej: A,3 o E 9).")
    print("Las columnas van de la A a la J, y los números del 1 al 10")   # ← arreglada la barra


def pedir_coordenadas(): 
    
    #Pide y valida las coordenadas (Letra, Número)
    while True:
        # 1. Mensaje de entrada: Muestra el rango 1 a 10.
        entrada = input(f"Tu turno. Introduce coordenada (Letra-Columna, Número-Fila 1-{dimension_tablero}): ").strip().upper()
        
        # Filtramos para quedarnos con letras y números.
        coordenadas = [p for p in entrada if p.isalnum()]

        # Comprobación de longitud básica
        if len(coordenadas) != 2:
            print("Algo ha fallado, debes escribir una Letra y un Número (ej: A,3 o J,10).")
            continue 

        letra_columna = coordenadas[0]
        numero_fila = coordenadas[1]
        
        # 1. Validación de la Columna (Letra)
        if letra_columna not in LETRAS_COLUMNAS:
            print(f"Debe ser una de las siguientes letras: {LETRAS_COLUMNAS}")
            continue

        try:
            # 2. Conversión de Fila y Columna
            fila = int(numero_fila)
            col = LETRAS_COLUMNAS.index(letra_columna)

            # 3. Validación de rango para el USUARIO: 1 a 10 (INCLUIDO)
            if 1 <= fila <= dimension_tablero:
                # Me volví loco, restar porque el índice no corresponde del 1 al 10
                return fila - 1, col 
            else:
                # Mensaje de error ajustado al rango 1-10
                print(f"Que sea un número entre 1 y {dimension_tablero}.")
                continue                     

        except ValueError:
            # Si el segundo elemento no se pudo convertir a entero
            print("Por favor, escribe el número sin decimales.")
            continue                             


def generar_disparo_maquina():
    #Genera una coordenada aleatoria para el disparo de la máquina (fila, columna).
    fila = random.randint(0, dimension_tablero - 1)
    col = random.randint(0, dimension_tablero - 1)
    return fila, col


def mostrar_tableros_turno(tablero_jugador, tablero_maquina):
    """
    Muestra el estado de ambos tableros al inicio de cada turno.
    tablero_jugador y tablero_maquina son objetos de la clase Tablero.
    """
    print("\n--- Resultados ---")
    
    # Muestra el tablero del jugador (con sus barcos y los daños recibidos)
    print(f"\n--- Tu Tablero ({tablero_jugador.id_jugador}) ---")
    tablero_jugador.mostrar_tablero(mostrar_barcos=True)
    
    # Muestra el tablero de la máquina (solo los disparos que el jugador ha hecho)
    print(f"\n--- Tablero Enemigo ({tablero_maquina.id_jugador}) (Tus Disparos) ---")
    tablero_maquina.mostrar_tablero(mostrar_barcos=False)
