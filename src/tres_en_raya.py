import random

def generar_tablero():
    """
    Crea y devuelve un tablero de 3x3 vacío representado como una lista de listas.

    Returns:
        list: Tablero inicializado con espacios vacíos.
    """
    tablero = []
    for _ in range(3):
        fila = []
        for _ in range(3):
            fila.append(" ")
        tablero.append(fila)
    return tablero

def mostrar_tablero(tablero):
    """
    Muestra el tablero actual

    Args:
        tablero (list): El estado actual del tablero.
    """
    print("   0   1   2")
    for indice_fila, fila in enumerate(tablero):
        print(indice_fila, "| " + " | ".join(fila) + " |")
        if indice_fila < 2:
            print("  -------------")

def hay_ganador(tablero, jugador):
    """
    Comprueba si el jugador dado ha ganado el juego.

    Args:
        tablero (list): El estado actual del tablero.
        jugador (str): El símbolo del jugador ('X' o 'O').

    Returns:
        bool: True si el jugador ha ganado, False en caso contrario.
    """
    # Comprobar filas
    for fila in tablero:
        ganador = True
        for celda in fila:
            if celda != jugador:
                ganador = False
                break
        if ganador:
            return True
    # Comprobar columnas
    for columna in range(3):
        ganador = True
        for fila in range(3):
            if tablero[fila][columna] != jugador:
                ganador = False
                break
        if ganador:
            return True
    # Comprobar diagonal principal
    ganador = True
    for i in range(3):
        if tablero[i][i] != jugador:
            ganador = False
            break
    if ganador:
        return True
    # Comprobar diagonal secundaria
    ganador = True
    for i in range(3):
        if tablero[i][2 - i] != jugador:
            ganador = False
            break
    if ganador:
        return True
    return False

def tablero_completo(tablero):
    """
    Verifica si el tablero está completo, lo que indica un empate.

    Args:
        tablero (list): El estado actual del tablero.

    Returns:
        bool: True si el tablero está completo, False en caso contrario.
    """
    for fila in tablero:
        for celda in fila:
            if celda == " ":
                return False
    return True

def movimiento_jugador(tablero, jugador):
    """
    Solicita al jugador que introduzca las coordenadas para su movimiento.

    Args:
        tablero (list): El estado actual del tablero.
        jugador (str): El símbolo del jugador ('X' o 'O').
    """
    while True:
        try:
            # Solicitar coordenadas al jugador
            fila = int(input("Introduce el numero de fila de tu movimiento (0, 1, 2): "))
            columna = int(input("Introduce el numero de columna de tu movimiento (0, 1, 2): "))
            # Verificar que las coordenadas estén dentro del rango
            if fila in [0, 1, 2] and columna in [0, 1, 2]:
                # Verificar que la posición esté vacía
                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador
                    break
                else:
                    print("Posición ocupada. Intentalo de nuevo.")
            else:
                print("Entrada inválida. Por favor, introduce números entre 0 y 2.")
        except ValueError:
            print("Entrada inválida. Debes introducir números.")

def movimiento_maquina(tablero, maquina, jugador):
    """
    Define la lógica del movimiento de la máquina, intentando ganar o bloquear al jugador para que no gane.

    Args:
        tablero (list): El estado actual del tablero.
        maquina (str): El símbolo de la máquina ('X' o 'O').
        jugador (str): El símbolo del jugador ('X' o 'O').
    """
    # Intentar ganar en el próximo movimiento
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                tablero[fila][columna] = maquina
                if hay_ganador(tablero, maquina):
                    return
                else:
                    tablero[fila][columna] = " "
    # Bloquear al jugador si está a punto de ganar
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                tablero[fila][columna] = jugador
                if hay_ganador(tablero, jugador):
                    tablero[fila][columna] = maquina
                    return
                else:
                    tablero[fila][columna] = " "
    # Elegir una posición aleatoria si no puede ganar ni bloquear
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = maquina
            break

def juego_tres_en_raya():
    """
    Controla el flujo principal del juego, alternando turnos entre el jugador y la máquina.
    """
    print("¡Bienvenido al juego de Tres en Raya!")
    while True:
        # Inicializar el tablero y asignar símbolos
        tablero = generar_tablero()
        jugadores = ["X", "O"]
        jugador = random.choice(jugadores)
        maquina = "O" if jugador == "X" else "X"
        print(f"El jugador es el '{jugador}' y la máquina es la '{maquina}'")
        # Decidir quién comienza
        turno = "jugador" if random.choice([True, False]) else "maquina"
        # print(f"Inicia {turno}")
        juego_activo = True
        while juego_activo:
            mostrar_tablero(tablero)
            if turno == "jugador":
                print ("Turno del Jugador")
                movimiento_jugador(tablero, jugador)
                # Verificar si el jugador ha ganado
                if hay_ganador(tablero, jugador):
                    mostrar_tablero(tablero)
                    print("¡Felicidades! Eres el ganador.")
                    juego_activo = False
                # Verificar si hay empate
                elif tablero_completo(tablero):
                    mostrar_tablero(tablero)
                    print("La partida ha finalizado en empate.")
                    juego_activo = False
                else:
                    turno = "maquina"
            else:
                print ("Turno de la Máquina")
                movimiento_maquina(tablero, maquina, jugador)
                # Verificar si la máquina ha ganado
                if hay_ganador(tablero, maquina):
                    mostrar_tablero(tablero)
                    print("La máquina ha ganado.")
                    juego_activo = False
                # Verificar si hay empate
                elif tablero_completo(tablero):
                    mostrar_tablero(tablero)
                    print("La partida ha finalizado en empate.")
                    juego_activo = False
                else:
                    turno = "jugador"
        # Preguntar si el jugador desea otra partida
        respuesta = input("¿Quieres jugar otra vez? (s/n): ")
        if respuesta.lower() != "s":
            break
    print("¡Gracias por jugar!. ¡Vuelve cuándo quieras!")

if __name__ == "__main__":
    juego_tres_en_raya()
