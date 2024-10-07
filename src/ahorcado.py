import random

class Ahorcado:
    def __init__(self):
        """
        Método Constructor de la clase Ahorcado.
        
        Inicializa los atributos necesarios para el juego, incluyendo la lista de palabras,
        el estado actual del juego (palabra seleccionada, letras intentadas, etc.).
        """
        # Lista de palabras posibles para el juego
        self.palabras = [
            "radio", "caballo", "motocicleta", "descampado", "algebra", "nube",
            "cielo", "mesa", "silla", "libro", "gato", "papel", "coche",
            "tren", "leche", "barco", "playa", "camion", "bosque", "ciudad",
            "calle", "puente", "parque", "meseta", "biblioteca", "mariposa",
            "elefante", "arrecife", "universidad", "amabilidad", "ventilador",
            "arquitecto", "cascabel", "trastero", "tristeza", "naturaleza",
            "estrategia", "gratificante", "pelota", "imprimir", "paraguas",
            "nevera", "campo", "sostenible", "tranquilidad", "error",
            "zapatillas", "corresponsal", "cordillera", "escuela"
        ]
        
        self.palabra_seleccionada = ""
        self.letras_intentadas = []
        self.intentos_fallidos = 0
        self.maximo_de_intentos = 6
        self.tablero = []
        self.jugar_de_nuevo = True
    
    def obtener_palabra_aleatoria(self):
        """
        Selecciona aleatoriamente una palabra de la lista de palabras.

        Returns:
            str: La palabra seleccionada para la partida.
        """
        palabra = random.choice(self.palabras)
        return palabra
    
    def dibujar_ahorcado(self):
        """
        Dibuja las diferentes etapas del ahorcado recogidas en la lista ahorcado_etaps.
        """
        ahorcado_etapas = [
            r"""
               +---+
               |   |
                   |
                   |
                   |
                   |
            =========
            """,
            r"""
               +---+
               |   |
               O   |
                   |
                   |
                   |
            =========
            """,
            r"""
               +---+
               |   |
               O   |
               |   |
                   |
                   |
            =========
            """,
            r"""
               +---+
               |   |
               O   |
              /|   |
                   |
                   |
            =========
            """,
            r"""
               +---+
               |   |
               O   |
              /|\  |
                   |
                   |
            =========
            """,
            r"""
               +---+
               |   |
               O   |
              /|\  |
              /    |
                   |
            =========
            """,
            r"""
               +---+
               |   |
               O   |
              /|\  |
              / \  |
                   |
            =========
            """
        ]
        if self.intentos_fallidos < len(ahorcado_etapas):
            print(ahorcado_etapas[self.intentos_fallidos])
        
    
    def inicializar_partida(self):
        """
        Inicializa una nueva partida del Ahorcado.

        Selecciona una palabra aleatoria, resetea las letras intentadas, el contador de fallos y
        configura el tablero con guiones bajos.
        """
        self.palabra_seleccionada = self.obtener_palabra_aleatoria()
        self.letras_intentadas = []
        self.intentos_fallidos = 0
        self.tablero = ['_'] * len(self.palabra_seleccionada)
        print('\n¡Bienvenido al juego del Ahorcado!')
        print('Intenta acertar la palabra adivinando letra por letra.')
    
    def mostrar_estado_juego(self):
        """
        Muestra el estado actual del juego al jugador.
        Incluye el dibujo del ahorcado, la palabra con las letras adivinadas y las letras que ya ha intentado.
        """
        self.dibujar_ahorcado()
        # Mostrar la palabra con las letras adivinadas y guiones bajos
        print('Palabra: ' + ' '.join(self.tablero))
        # Mostrar las letras que el jugador ya ha intentado
        print('Letras intentadas: ' + ', '.join(self.letras_intentadas))
    
    def solicitar_letra(self):
        """
        Solicita al jugador que introduzca una letra válida.
        Verifica que la entrada sea una sola letra alfabética y que no haya sido intentada previamente.

        Returns:
            str: La letra válida ingresada por el jugador.
        """
        while True:
            letra = input('Introduce una letra: ').lower()
            # Verificar que solo se haya introducido un carácter alfabético
            if len(letra) != 1 or not letra.isalpha():
                print('Por favor, introduce una sola letra.')
                continue 
            # Verificar si la letra ya ha sido intentada
            if letra in self.letras_intentadas:
                print('Ya has intentado esa letra. Intenta con otra.')
                continue  # Volver al inicio del bucle
            return letra
    
    def actualizar_tablero(self, letra):
        """
        Actualiza el tablero con la letra adivinada si está en la palabra.

        Args:
            letra (str): La letra que el jugador ha intentado adivinar.
        """
        if letra in self.palabra_seleccionada:
            print(f'¡Muy bien! La letra "{letra}" está en la palabra.')
            # Reemplazar los guiones bajos por la letra acertada en las posiciones correctas
            for indice, caracter in enumerate(self.palabra_seleccionada):
                if caracter == letra:
                    self.tablero[indice] = letra
        else:
            # Incrementar el contador de intentos fallidos si la letra no está en la palabra
            self.intentos_fallidos += 1
            intentos_restantes = self.maximo_de_intentos - self.intentos_fallidos
            print(f'La letra "{letra}" no está en la palabra. Te quedan {intentos_restantes} intentos.')
    
    def verificar_ganador(self):
        """
        Verifica si el jugador ha adivinado todas las letras de la palabra.

        Returns:
            bool: `True` si el jugador ha ganado, `False` en caso contrario.
        """
        return '_' not in self.tablero
    
    def verificar_perdedor(self):
        """
        Verifica si el jugador ha alcanzado el número máximo de intentos fallidos.

        Returns:
            bool: `True` si el jugador ha perdido, `False` en caso contrario.
        """
        return self.intentos_fallidos >= self.maximo_de_intentos
    
    def mostrar_final_juego(self):
        """
        Muestra las opciones al finalizar la partida y solicita al jugador que elija 
        entre volver al menú principal o salir del juego.

        Returns:
            int: La opción seleccionada por el jugador (1 o 2).
        """
        print("\nElija una opción:")
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
    
    def jugar(self):
        """
        Controla el flujo principal del juego, permitiendo al jugador jugar múltiples partidas.
        Maneja la inicialización de partidas, el ciclo de juego, la verificación de condiciones de fin,
        y la decisión de jugar nuevamente o salir.
        """
        while self.jugar_de_nuevo:
            self.inicializar_partida()
            # Bucle principal de la partida
            while not self.verificar_ganador() and not self.verificar_perdedor():
                self.mostrar_estado_juego()
                letra = self.solicitar_letra()
                self.letras_intentadas.append(letra)
                self.actualizar_tablero(letra)
                print()  # Línea en blanco para mejorar la legibilidad
            
            # Mostrar el estado final del juego
            self.dibujar_ahorcado()
            if self.verificar_ganador():
                print(f'\n¡Felicidades! Has adivinado la palabra: {self.palabra_seleccionada}')
            else:
                print(f'\nLo siento, has perdido. La palabra era: {self.palabra_seleccionada}')
            
            # Preguntar al jugador si desea jugar otra vez y si dice que no se le da a elegir
            # entre volver al menu principal o salir del juego
            respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
            if respuesta != "s":
                seleccion_final = self.mostrar_final_juego()
                if seleccion_final == 1:
                    print("¡Gracias por jugar al Tres en Raya! Vuelve cuando quieras.")
                    return seleccion_final
                else:
                    return seleccion_final
                break

"""
if __name__ == "__main__":
    juego = Ahorcado()
    juego.jugar()     
"""            
            
            
            
            
            
            
            
            
            
            
            

