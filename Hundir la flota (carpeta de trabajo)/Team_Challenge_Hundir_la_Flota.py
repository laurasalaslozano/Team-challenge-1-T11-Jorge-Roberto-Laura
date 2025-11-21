#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:image.png)

# ## Introducción
# En esta entrega vais a crear vuestra propia versión del juego de **Hundir la flota** en Python. Para el desarrollo del programa neceistarás conocimientos de la librería `numpy`, módulos, bucles, funciones, clases y colecciones de Python. **La entrega deberá constar de  varios scripts de Python (archivos .py), en clase se os darán los detalles**.
# 

# 
# ## ¿Cómo funciona el juego?
# Vamos a realizar una versión que tiene algunas particularidades respecto al juego original, de manera que sea más sencillo el desarrollo. Veamos cómo funciona:
# 
# 1. Hay dos jugadores: tú y la máquina
# 2. Un **tablero de 10 x 10** posiciones donde irán los barcos
# 3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria. Ahora bien, puedes empezar colocando los barcos en unas posiciones fijas, que no cambien con cada partida, y después implementarlo aleatoriamente, ya que es más complejo. Los barcos son:**
#     * 4 barcos de 1 posición de eslora
#     * 3 barcos de 2 posiciones de eslora
#     * 2 barcos de 3 posiciones de eslora
#     * 1 barco de 4 posiciones de eslora
# 
# 4. Tanto tú, como la máquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
# 5. Funciona por turnos y empiezas tú.
# 6. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la máquina.
# 7. En los turnos de la máquina, si acerta también le vuelve a tocar. ¿Dónde dispara la maquina? A un punto aleatorio en tu tablero.
# 8. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.
# 
# En [esta página](http://es.battleship-game.org/) podrás probarlo online.

# ## Desarrollo
# Tendrás que desarrollar lo siguiente:
# 1. Necesitarás un conjunto de **constantes**, donde tengas inventariados los barcos del juego, dimensiones y demás variables que no vayan a cambiar que tendréis definidas en archivo de **variables.py**
# 
# 2. Tendrás que construir **una clase Tablero**. Para facilitar el desarrollo, la mejor opción es desarrollar una clase tablero donde implementes las siguientes funcionalidades:
#     * Cuando se inicialice deberás asignar
#         * Un id de jugador, para saber de quién es el tablero.
#         * Unas dimensiones de tablero, que en el fondo serán tus constantes 10 x 10.
#         * Unos barcos. Los que hayas definido como constantes. Aqui simplemente puedes pasar, por ejemplo, un diccionario donde especifiques el nombre de tus barcos, y la eslora de cada uno. Luego ya los colocarás en el tablero.
#         * **Un tablero sin barcos, que será un array de `numpy`** donde posicionarás los barcos. Este tablero está vacío, por lo que lo puedes rellenar de 0s, 1s, o el caracter que consideres.
#         * Adicionalmente la clase tablero necesitará otro array de `numpy`, ¿por qué? porque el tablero de la maquina tendrá internamente un array con sus barcos (lo que no vemos) y hará falta otro array (que sí veremos nosotros) con los disparos efectuados, para saber dónde tenemos que disparar.
#     * **Inicializar el tablero**, es decir, colocar los barcos. Puedes pasar por alto el hecho de que tengan que tener espacios entre ellos pero si los colocas aleatoriamente, mucho cuidado aquí de poner los barcos dentro del tablero, y de no colocar unos barcos encima de otros :)
#     * Necesitarás un método de **disparo coordenada**. Cuando hay un disparo de un jugador en ese tablero, tendrás que comprobar si ahi había un barco, o simplemente agua. Acuérdate de marcar en el tablero, tanto si hay un impacto, como si dio agua.
#     * NO te ciñas a los métodos que te acabo de mencionar, crea todos los que necesites, introduce en el constructor lo que quieras y desarrolla las funciones que consideres oportunas para facilitarte el desarrollo.
# 
# 3. Una vez ya tienes modelizado tu tablero, hay que montar el programa que se ejecutara desde un **main.py**:
#     * El programa no es más que el **típico `while true: `, con una serie de inputs del usuario**. Se está ejecutando constantemente y le pide al usuario coordenadas para comprobar si impacta.
#     * Cuando arranque el programa, primero pon algún mensaje de bienvenida y las instrucciones del juego.
#     * A continuación **inicializa los tableros de ambos jugadores** con los barcos. Estas dos primeras acciones solo se ejecutan una vez!! Que es el comienzo del juego.
#     * Después de eso ya comienza el juego. Básicamente **se irá ejecutando iterativamente en el `while`, y le irá preguntando coordenadas al usuario.**
#     * Recoges coordenadas, compruebas en el tablero de la máquina si habia barco.
#         * Hay barco: marca en el tablero de la maquina el impacto y le vuelve a tocar al usuario
#         * No hay barco: le toca a la maquina. O lo que es lo mismo, escoge una coordenada aleatoria, y comprueba en el tablero del usuario si habia barco.
#     * **Así hasta que uno de los dos jugadores se quede sin barcos, y termina el juego.**
#     * Cuando empiece tu turno deberías imprimir por pantalla tu tablero, para ver cuántos impactos te ha hecho la máquina, así como el tablero con los impactos que has hecho tu en el adversario, de manera que te sirva de ayuda para el siguiente disparo.
#     * Todas aquellas funciones que puedas construir para la ejecución de este programa deberán estar definidas en un script que se llame **funciones.py**.
# 
# Hay infinidad de maneras para resolver este ejercicio, sentíos libres de implementarlo de la forma que te resulte más cómoda.
# 
# 

# ## Recomendaciones
# 1. **No es necesario tener una clase barco, aunque es recomendable** con los barcos de cada jugador, cuáles están tocados y demás. Simplemente con llevar un inventario de las coordenadas con barco es suficiente. Por ejemplo, si el tablero tuviese 2 barcos de 4 posiciones de eslora, es como si tuvieses 8 vidas. Cuando se te acaban las vidas, pierdes.
# 2. Para implementar el bucle `while`, puedes usar **sentencias `continue`, `break`**.
# 3. Se recomienda tener el código separado en **varios scripts**. Por ejemplo:
#     * main.py: donde corre todo el programa
#     * clases.py: aquí irán las clases
#     * funciones.py: aquí irán las funciones
#     * variables.py: donde están declaradas las constantes
#     * A gusto del desarrollador...
# 4. Cuando se imprime el tablero por pantalla, básicamente será un `print()` del array de `numpy`. Escoge con sentido qué quieres que se imprima por pantalla, de manera que se vea bien dónde hay barco, donde ha habido impacto, agua... Tendrás los siguients casos:
#     * Agua donde no se ha impactado
#     * Agua donde se ha impactado
#     * Barco donde no se ha impactado
#     * Barco donde se ha impactado
# 5. Utiliza el `debugging` del IDE de Visual Studio Code si ves que tu programa no se comporta como debería y no sabes muy bien por qué.
# 6. Se recomienda en la clase tablero manejar dos arrays de 10x10. Uno con las coordenadas de los barcos y los impactos, que será tu tablero, lo que veas tu cuando imprimes tu tablero por pantalla. Y otro tablero SIN los barcos, únicamente con los impactos, para ver qué impactos has hecho en el tablero de la maquina.
# 7. Si vas a posicionar los barcos de manera aleatoria, tendrás que escoger unas coordenadas aleatoriamente, y una orientación N/S/E/O, de manera que si tu barco tiene 3 de eslora y la orientación es N, se posicionará hacia arriba, desde la posición inicial elegida aleatoriamente.
# 8. Si no tienes un nivel alto de Python, prueba primero a crear el array de numpy vacío y a colocar los barcos en unas posiciones concretas que nunca cambien, porque si lo haces aleatoriamente te será más complicado. No es justo como funciona el juego, pero mejor avanzar a quedarnos atascados al principio.
# 

# ## Presentación
# Cada grupo realizará una presentación en la clase de Team Challenge del **Sprint 5**, donde se contarán con **10 minutos máximo**, importante ceñirse al tiempo. Se tendrá que enseñar:
# 1. El repositorio de github y las partes más relevantes del desarrollo de código
# 3. Una demo donde se muestren el funcionamiento del juego
# 
# Para esta presentación podéis apoyaros en cualquier recurso que necesites.

# **Por supuesto, pudes preguntar cualquier duda a los profesores si tienes cualquier problema con el desarrollo o no entiendes algo del enunciado :)**

# In[1]:


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



# In[23]:


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



# In[3]:


#código corregido

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
        # Verificar si ya se disparó aquí
        if self.tablero[fila, col] in [tocado, fallo]:
            print("Ya habías disparado aquí.")
            return None

        # Verificar si hay barco
        if self.tablero[fila, col] == barco:
            self.tablero[fila, col] = tocado
            print("¡Impacto!")
            return True
        else:
            # Solo marcar fallo en el tablero, no cambiar agua
            self.tablero[fila, col] = fallo
            print("Agua...")
            return False

    def registrar_disparo(self, fila, col, resultado):
        """Registra el disparo en el tablero de disparos (vista del oponente)"""
        if resultado:
            self.tablero_disparos[fila, col] = tocado
        else:
            self.tablero_disparos[fila, col] = fallo

    def mostrar_tablero(self, mostrar_barcos=True):
        """Muestra el tablero por pantalla"""
        print(f"\n--- Tablero de {self.id_jugador} ---")
        print("   " + " ".join(map(str, range(dimension_tablero))))
        tablero_a_mostrar = self.tablero if mostrar_barcos else self.tablero_disparos
        for i, fila in enumerate(tablero_a_mostrar):
            print(f"{i:2} " + " ".join(fila))

    def quedan_barcos(self):
        """Comprueba si quedan barcos vivos"""
        return np.any(self.tablero == barco)


# In[ ]:


import numpy as np
from variables import varios_barcos, variable_jugador, variable_maquina
from clases import Tablero

def main():
    print("=== BIENVENIDO A HUNDIR LA FLOTA ===\n")

    # Inicializar tableros (aquí se crean e inicializan automáticamente)
    tablero_jugador = Tablero(variable_jugador, varios_barcos)
    tablero_maquina = Tablero(variable_maquina, varios_barcos)

    print("Tableros creados e inicializados!")
    print("\n--- Tu tablero (con tus barcos visibles) ---")
    tablero_jugador.mostrar_tablero(mostrar_barcos=True)

    print("\n--- Tablero de la máquina (sin ver sus barcos) ---")
    tablero_maquina.mostrar_tablero(mostrar_barcos=False)

    # Bucle principal del juego
    turno = 0
    while tablero_jugador.quedan_barcos() and tablero_maquina.quedan_barcos():
        turno += 1
        print(f"\n{'='*50}")
        print(f"TURNO {turno}")
        print(f"{'='*50}")

        # Turno del jugador
        print("\n--- TU TURNO ---")
        tablero_maquina.mostrar_tablero(mostrar_barcos=False)

        # Pedir coordenadas al jugador
        while True:
            try:
                fila = int(input("Introduce fila (0-9): "))
                col = int(input("Introduce columna (0-9): "))

                if 0 <= fila <= 9 and 0 <= col <= 9:
                    break
                else:
                    print("Coordenadas fuera del rango. Intenta de nuevo.")
            except ValueError:
                print("Por favor, introduce números válidos.")

        # Disparar al tablero de la máquina
        resultado = tablero_maquina.disparar(fila, col)

        if resultado is not None:  # Disparo válido
            tablero_jugador.registrar_disparo(fila, col, resultado)
        else:
            print("Ya habías disparado ahí. Pierdes el turno.")
            continue

        # Verificar si ganó el jugador
        if not tablero_maquina.quedan_barcos():
            print("\n¡¡¡FELICIDADES!!! ¡Has hundido todos los barcos!")
            break

        # Turno de la máquina
        print("\n--- TURNO DE LA MÁQUINA ---")
        import random
        fila_maq = random.randint(0, 9)
        col_maq = random.randint(0, 9)

        print(f"La máquina dispara a ({fila_maq}, {col_maq})")
        resultado_maq = tablero_jugador.disparar(fila_maq, col_maq)

        if resultado_maq is None:
            print("La máquina disparó donde ya había disparado.")

        # Verificar si ganó la máquina
        if not tablero_jugador.quedan_barcos():
            print("\n¡Oh no! La máquina ha hundido todos tus barcos.")
            break

        # Mostrar tu tablero después del turno de la máquina
        print("\n--- Tu tablero ---")
        tablero_jugador.mostrar_tablero(mostrar_barcos=True)

    print("\n=== FIN DEL JUEGO ===")

if __name__ == "__main__":
    main()


# In[ ]:


import numpy as np
import random
from variables import varios_barcos, variable_jugador, variable_maquina
from clases import Tablero

def main():
    print("=== BIENVENIDO A HUNDIR LA FLOTA ===\n")

    # Inicializar tableros (aquí se crean e inicializan automáticamente)
    tablero_jugador = Tablero(variable_jugador, varios_barcos)
    tablero_maquina = Tablero(variable_maquina, varios_barcos)

    print("Tableros creados e inicializados!")
    print("\n--- Tu tablero (con tus barcos visibles) ---")
    tablero_jugador.mostrar_tablero(mostrar_barcos=True)

    print("\n--- Tablero de la máquina (sin ver sus barcos) ---")
    tablero_maquina.mostrar_tablero(mostrar_barcos=False)

    # Bucle principal del juego
    turno = 0
    while tablero_jugador.quedan_barcos() and tablero_maquina.quedan_barcos():
        turno += 1
        print(f"\n{'='*50}")
        print(f"TURNO {turno}")
        print(f"{'='*50}")

        # Turno del jugador
        print("\n--- TU TURNO ---")
        tablero_maquina.mostrar_tablero(mostrar_barcos=False)

        # Pedir coordenadas al jugador
        disparo_valido = False
        while not disparo_valido:
            try:
                fila = int(input("Introduce fila (0-9): "))
                col = int(input("Introduce columna(0-9)"))


# In[6]:


import numpy as np
import random
from variables import varios_barcos, variable_jugador, variable_maquina
from clases import Tablero

def main():
    print("=== BIENVENIDO A HUNDIR LA FLOTA ===\n")

    # Inicializar tableros (aquí se crean e inicializan automáticamente)
    tablero_jugador = Tablero(variable_jugador, varios_barcos)
    tablero_maquina = Tablero(variable_maquina, varios_barcos)

    print("Tableros creados e inicializados!")
    print("\n--- Tu tablero (con tus barcos visibles) ---")
    tablero_jugador.mostrar_tablero(mostrar_barcos=True)

    print("\n--- Tablero de la máquina (sin ver sus barcos) ---")
    tablero_maquina.mostrar_tablero(mostrar_barcos=False)

    # Bucle principal del juego
    turno = 0
    while tablero_jugador.quedan_barcos() and tablero_maquina.quedan_barcos():
        turno += 1
        print(f"\n{'='*50}")
        print(f"TURNO {turno}")
        print(f"{'='*50}")

        # Turno del jugador
        print("\n--- TU TURNO ---")
        tablero_maquina.mostrar_tablero(mostrar_barcos=False)

        # Pedir coordenadas al jugador
        disparo_valido = False
        while not disparo_valido:
            try:
                fila = int(input("Introduce fila (0-9): "))
                col = int(input("Introduce columna (0-9): "))

                if 0 <= fila <= 9 and 0 <= col <= 9:
                    # Disparar al tablero de la máquina
                    resultado = tablero_maquina.disparar(fila, col)

                    if resultado is not None:  # Disparo válido
                        tablero_jugador.registrar_disparo(fila, col, resultado)
                        disparo_valido = True
                    else:
                        print("Ya habías disparado ahí. Intenta de nuevo.")
                else:
                    print("Coordenadas fuera del rango. Intenta de nuevo.")
            except ValueError:
                print("Por favor, introduce números válidos.")

        # Verificar si ganó el jugador
        if not tablero_maquina.quedan_barcos():
            print("\n¡¡¡FELICIDADES!!! ¡Has hundido todos los barcos!")
            break

        # Turno de la máquina
        print("\n--- TURNO DE LA MÁQUINA ---")
        fila_maq = random.randint(0, 9)
        col_maq = random.randint(0, 9)

        print(f"La máquina dispara a ({fila_maq}, {col_maq})")
        resultado_maq = tablero_jugador.disparar(fila_maq, col_maq)

        if resultado_maq is None:
            print("La máquina disparó donde ya había disparado.")

        # Verificar si ganó la máquina
        if not tablero_jugador.quedan_barcos():
            print("\n¡Oh no! La máquina ha hundido todos tus barcos.")
            break

        # Mostrar tu tablero después del turno de la máquina
        print("\n--- Tu tablero ---")
        tablero_jugador.mostrar_tablero(mostrar_barcos=True)

    print("\n=== FIN DEL JUEGO ===")

if __name__ == "__main__":
    main()


# In[ ]:


# Corregido Laura:

import numpy as np
import random
from variables import dimension_tablero, agua, barco, tocado, fallo

class Tablero:
    def __init__(self, id_jugador, barcos_dict, dimension = dimension_tablero):
        self.id_jugador = id_jugador
        self.dimension = dimension
        self.barcos_dict = barcos_dict # diccionario con cantidades y esloras
        # Tablero principal: contiene barco, agua, tocado, fallo
        self.tablero = np.full((self.dimension, self.dimension), agua, dtype = str)
        self.tablero_disparos = np.full((self.dimension, self.dimension), agua, dtype = str)
        self.colocar_barcos()

    def colocar_barcos(self):
        """Coloca los barcos aleatoriamente sin solapamientos"""
        for _, info in self.barcos_dict.items():
            cantidad = info["cantidad"]
            eslora = info["eslora"]
            for _ in range(cantidad):
                colocado = False
                intentos = 0
                while not colocado:
                    intentos += 1
                    if intentos > 1000:
                        #seguridad: reinicia el tablero y vuelve a intentar (muy improbable)
                        self.tablero = np.full((self.dimension, self.dimension), agua, dtype = str)
                        intentos = 0
                    fila = random.randint(0, self.dimension - 1)
                    col = random.randint(0, self.dimension - 1)
                    orientacion = random.choice(["H", "V"])
                    if self._puede_colocar(fila, col, eslora, orientacion):
                        self._colocar(fila, col, eslora, orientacion)
                        colocado = True

    def _puede_colocar(self, fila, col, eslora, orientacion):
        """Comprueba si se puede colocar un barco en la posición indicada y no choque con otros"""
        if orientacion == "H":
            if col + eslora > self.dimension: 
                return False
            for i in range(eslora):
                if self.tablero[fila, col + i] != agua:
                    return False
        else:  # Vertical
            if fila + eslora > self.dimension: 
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

    def recibir_disparo(self, fila, col):

        """
        Procesa un disparo en el tablero (el que recibe el disparo).
        Devuelve:
            None -> ya se disparó ahí antes (no válido)
            True -> impacto (y marca TOCADO)
            False -> agua (y marca FALLO)
        """
        #Validar índices:

        if not (0 <= fila < self.dimension and 0 <= col < self.dimension):
            raise IndexError("Coordenadas fuera del tablero")

        actual = self.tablero[fila, col]
        if actual in (tocado, fallo):
            return None

        if actual == barco:
            self.tablero[fila, col] = tocado

        else:
            # si estaba agua, marcamos fallo
            self.tablero[fila, col] = fallo
            return False

    def registrar_disparo(self, fila, col, resultado):
        """Registra el disparo en el tablero de disparos (vista del jugador)"""

        if resultado is True:
            self.tablero_disparos[fila, col] = tocado
        elif resultado is False:
            self.tablero_disparos[fila, col] = fallo

    def mostrar_tablero(self, mostrar_barcos=True):
        """Muestra el tablero por pantalla Si mostrar barcos es False, muestra la vista de disparos """
        print(f"\n--- Tablero de {self.id_jugador} ---")
        print("   " + " ".join(map(str, range(self.dimension)))) 
        tablero_a_mostrar = self.tablero if mostrar_barcos else self.tablero_disparos
        for i, fila in enumerate(tablero_a_mostrar):
            print(f"{i:2} " + " ".join(fila))

    def quedan_barcos(self):
        """Comprueba si quedan barcos vivos"""
        return np.any(self.tablero == barco)

    def contar_barcos_vivos(self):
        """ Número de casillas de barco que aún no han sido tocadas"""
        return int((self.tablero == barco).sum())


# In[ ]:


import numpy as np
import random
from variables import dimension_tablero

def pedir_coordenadas():
    """Pide coordenadas al usuario y las valida (devuelve fila, col)."""
    while True:
        try:
            fila = int(input(f"Introduce fila (0-{dimension_tablero-1}): "))
            col = int(input(f"Introduce columna (0-{dimension_tablero-1}): "))
            if 0 <= fila < dimension_tablero and 0 <= col < dimension_tablero:
                return fila, col
            else:
                print("Coordenadas fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Por favor, introduce número enteros válidos")

def coordenada_aleatoria_no_probada(disponibles):
    """Elige una coordenada aleatoria de la lista "disponibles". "disponibles" es una lista o set de tuplas (fila, col)."""

    #Convertir a lista si es set
    if not disponibles:
        return None
    return random.choice(list(disponibles))


# In[ ]:


import numpy as np
import random
from variables import varios_barcos, jugador, maquina, agua, tocado, fallo
from clases import Tablero
from funciones import pedir_coordenadas, coordenada_aleatoria_no_probada

def main():
    print(" === BIENVENIDO A HUNDIR LA FLOTA ===\n")
    print("Reglas rápidas:")
    print("- Tablero 10x10. Tú empiezas")
    print("- Si aciertas, vuelves a jugar. Si fallas, juega la máquina.")
    print("- La máquina dispara a casillas no probadas y también repite si acierta.\n")

    #Inicializar tableros
    tablero_jugador = Tablero(jugador, varios_barcos)
    tablero_maquina = Tablero(maquina, varios_barcos)

    #Conjuntos de coordenadas no probadas para la máquina (para evitar repetir)
    disponibles_maq = {(r, c) for r in range(10), for c in range(10)}

    print("Tableros creados e inicializados!\n")
    print("--- Tu tablero (tus barcos visibles) ---")
    tablero_jugador.mostrar_tablero(mostrar_barcos = True)

    #Bucle principal
    turno = 0
    while tablero_jugador.quedan_barcos() and tablero_maquina.quedan_barcos():
        turno += 1
        print(f"\n{'='*50}")
        print(f"Turno {turno}")
        print(f"{'='*50}")

        #Mostrar información útil al jugador
        print("\nTu tablero (con los barcos):")
        tablero_jugador.mostrar_tablero(mostrar_barcos = True)
        print("\nTablero de disparos (tu vista sobre la máquina):")
        tablero_maquina.mostrar_tablero(mostrar_barcos = False)

        # ---- Turno del jugador ----
        print("\n --- TU TURNO ---")
        jugador_sigue = True
        while jugador_sigue and tablero_maquina.quedan_barcos():
            fila, col = pedir_coordenadas()

            #Comprobar si ya se disparó ahí en la vista del jugador
            if tablero_maquina.tablero_disparos[fila, col] in (tocado, fallo):
                print("Ya habías disparado en esa casilla. Elige otra.")
                continue
            resultado = tablero_maquina.recibir_disparo(fila, col)
            #Registrar resultado en la vista del jugador (tablero_disparos de la máquina)
            tablero_maquina.registrar_disparo(fila, col, resultado)

            if resultado is None:
                #No debería ocurrir, pero por si acaso comprobamos
                print("Ese disparo ya se efectuó. No válido")
                jugador_sigue = False

            elif resultado:
                print("¡Has impactado! Te toca de nuevo.")
                # Si no quedan barcos, sales
                if not tablero_maquina.quedan_barcos():
                    break
                jugador_sigue = True

            else:
                print("Has fallado. Turno de la máquina.")
                jugador_sigue = False

        if not tablero_maquina.quedan_barcos():
            print("\n¡¡¡FELICIDADES!!! ¡Has hundido todos los barcos!")
            break

        # --- Turno de la máquina ---
        print("\n--- TURNO DE LA MÁQUINA ---")
        maquina_sigue = True
        while maquina_sigue and tablero_jugador.quedan_barcos():
            #Elegir coordenada aleatoria no probada
            coord = coordenada_aleatoria_no_probada(disponibles_maq)
            if coord is None:
                print("La máquina no tiene más coordenadas disponibles.")
                maquina_sigue = False
                break
            fila_maq, col_maq = coord
            #Marcar como probada para que no vuelva a salir
            disponibles_maq.discard(coord)

            print(f"La máquina dispara a ({fila_maq, col_maq})")
            resultado_maq = tablero_jugador.recibir_disparo(fila_maq, col_maq)

            #La máquina no tiene un tablero_disparos propio visible aquí, pero el resultado se ve en el tablero del jugador impreso después
            if resultado_maq is None:
                #ya probado (no debería suceder, pero por si acaso)
                print("La máquina disparó a una casilla ya probada. Sigue intentando.")
                maquina_sigue = True

            elif resultado_maq:
                print("La máquina ha impactado y vuelve a disparar.")
                maquina_sigue = True

            else:
                print("La máquina ha fallado.")
                maquina_sigue = False

            if not tablero_jugador.quedan_barcos():
                break

        if not tablero_jugador.quedan_barcos():
            print("\n¡Oh no! La máquina te ha vencido. Ha hundido todos tus barcos.")
            break

        #Mostrar el tablero del jugador después del turno de la máquina
        print("\n--- Estado al final del turno ---")
        print("Tu tablero:")
        tablero_jugador.mostrar_tablero(mostrar_barcos = True)
        print("\nEl tablero de la máquina:")
        tablero_maquina.mostrar_tablero(mostrar_barcos = False)

    print("\n--- FIN DEL JUEGO ---")

if __name__ == "__main__":
    main()

