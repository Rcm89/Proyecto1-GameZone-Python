import random

class TresEnRaya:
    def __init__(self):
        """
        Inicializa el juego de Tres en Raya.
        """
        self.tablero = self.generar_tablero()
        self.jugadores = ["X", "O"]
        self.jugador = "X"
        self.maquina = "O"

    def generar_tablero(self):
        """
        Crea y devuelve un tablero de 3x3 vacío representado como una lista de listas.
        """
        tablero = []
        for _ in range(3):
            fila = []
            for _ in range(3):
                fila.append(" ")
            tablero.append(fila)
        return tablero
    
    def mostrar_tablero(self):
        """Muestra el tablero actual."""
        print("   0   1   2")
        for indice_fila, fila in enumerate(self.tablero):
            print(indice_fila, "| " + " | ".join(fila) + " |")
            if indice_fila < 2:
                print("  -------------")

    def hay_ganador(self, jugador):
        """
        Comprueba si el jugador dado ha ganado el juego.
        """
        # Comprobar filas
        for fila in self.tablero:
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
                if self.tablero[fila][columna] != jugador:
                    ganador = False
                    break
            if ganador:
                return True
        # Comprobar diagonal principal
        ganador = True
        for i in range(3):
            if self.tablero[i][i] != jugador:
                ganador = False
                break
        if ganador:
            return True
        # Comprobar diagonal secundaria
        ganador = True
        for i in range(3):
            if self.tablero[i][2 - i] != jugador:
                ganador = False
                break
        if ganador:
            return True
        return False

    def tablero_completo(self):
        """
        Verifica si el tablero está completo, lo que indica un empate.

        Args:
            tablero (list): El estado actual del tablero.

        Returns:
            bool: True si el tablero está completo, False en caso contrario.
        """
        for fila in self.tablero:
            for celda in fila:
                if celda == " ":
                    return False
        return True
    
    def tablero_completo(self):
        """
        Verifica si el tablero está completo, lo que indica un empate.
       
        """
        for fila in self.tablero:
            for celda in fila:
                if celda == " ":
                    return False
        return True
    def movimiento_jugador(self):
        """
        Solicita al jugador que introduzca las coordenadas para su movimiento.
        """
        while True:
            try:
                # Solicitar coordenadas al jugador
                fila = int(input("Introduce el numero de fila de tu movimiento (0, 1, 2): "))
                columna = int(input("Introduce el numero de columna de tu movimiento (0, 1, 2): "))
                # Verificar que las coordenadas estén dentro del rango
                if fila in [0, 1, 2] and columna in [0, 1, 2]:
                    # Verificar que la posición esté vacía
                    if self.tablero[fila][columna] == " ":
                        self.tablero[fila][columna] = self.jugador
                        break
                    else:
                        print("Posición ocupada. Intentalo de nuevo.")
                else:
                    print("Entrada inválida. Por favor, introduce números entre 0 y 2.")
            except ValueError:
                print("Entrada inválida. Debes introducir números.")


    def movimiento_maquina(self):
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
                if self.tablero[fila][columna] == " ":
                    self.tablero[fila][columna] = self.maquina
                    if self.hay_ganador(self.maquina):
                        return
                    else:
                        self.tablero[fila][columna] = " "
        # Bloquear al jugador si está a punto de ganar
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == " ":
                    self.tablero[fila][columna] = self.jugador
                    if self.hay_ganador(self.jugador):
                        self.tablero[fila][columna] = self.maquina
                        return
                    else:
                        self.tablero[fila][columna] = " "
        # Elegir una posición aleatoria si no puede ganar ni bloquear
        while True:
            fila = random.randint(0, 2)
            columna = random.randint(0, 2)
            if self.tablero[fila][columna] == " ":
                self.tablero[fila][columna] = self.maquina
                break
    
    def mostrar_final_juego(self):
        """
        Instrucciones que se muestran tras finalizar el juego.

        Returns:
            int: devuelve un 1 o 2 dependiendo de la opción seleccionada.
        """
        print("Elija una opción:")
        print("1. Volver al menú principal")
        print("2. Salir")
        while True:
            try:
                seleccion_final = int(input("Su elección: "))
                if seleccion_final not in [1, 2]:
                    print("Por favor introduzca un 1 o un 2.")
                else:
                    break
            except ValueError:
                print("Por favor introduzca un 1 o un 2.")
        return seleccion_final
    
    def jugar_nueva_partida(self):
        """
        Inicia una nueva partida de Tres en Raya.
        """
        self.tablero = self.generar_tablero()
        self.jugador = random.choice(self.jugadores)
        self.maquina = "O" if self.jugador == "X" else "X"
        print(f"El jugador es el '{self.jugador}' y la máquina es la '{self.maquina}'")
        self.turno = "jugador" if random.choice([True, False]) else "maquina"
    
    def jugar(self):
        """Gestiona el flujo del juego, alternando turnos entre el jugador y la máquina"""
        print("¡Bienvenido al juego de Tres en Raya!")
        #seleccion_final=0
        while True:
            self.jugar_nueva_partida()
            juego_activo = True
            while juego_activo:
                self.mostrar_tablero()
                if self.turno == "jugador":
                    print("Turno del Jugador")
                    self.movimiento_jugador()
                    if self.hay_ganador(self.jugador):
                        self.mostrar_tablero()
                        print("¡Felicidades! Eres el ganador.")
                        juego_activo = False
                    elif self.tablero_completo():
                        self.mostrar_tablero()
                        print("La partida ha finalizado en empate.")
                        juego_activo = False
                    else:
                        self.turno = "maquina"
                else:
                    print("Turno de la Máquina")
                    self.movimiento_maquina()
                    if self.hay_ganador(self.maquina):
                        self.mostrar_tablero()
                        print("La máquina ha ganado.")
                        juego_activo = False
                    elif self.tablero_completo():
                        self.mostrar_tablero()
                        print("La partida ha finalizado en empate.")
                        juego_activo = False
                    else:
                        self.turno = "jugador"
            # Preguntar al jugador que desea hacer
            respuesta = input("¿Quieres jugar otra vez? (s/n): ")
            if respuesta.lower() != "s":
                seleccion_final = self.mostrar_final_juego()
                if seleccion_final == 1:
                    print("¡Gracias por jugar al Tres en Raya! Vuelve cuando quieras.")
                else:
                    print("¡Gracias por jugar! Hasta luego.")
                break

