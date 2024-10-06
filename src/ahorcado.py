import random

def obtener_palabra_aleatoria(lista_palabras):
    """Selecciona aleatoriamente una palabra de la lista."""
    return random.choice(lista_palabras)

def dibujar_ahorcado(fallos):
    """Dibuja el estado actual del ahorcado según el número de fallos."""
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
    # Aquí nos aseguramos de que el índice no exceda el rango de la lista
    if fallos < len(ahorcado_etapas):
        print(ahorcado_etapas[fallos])
    else:
        print("¡ El número de fallos excede las etapas definidas!")

def juego_ahorcado():
    """
    Función principal que ejecuta el juego.
    """
    jugar_de_nuevo = True
    # Lista de palabras que se emplean para el juego
    palabras = [
    "radio", "caballo", "motocicleta", "descampado", "algebra","nube", "cielo", "mesa", "silla",
    "libro", "gato", "papel", "coche", "tren", "leche", "barco", "playa", "camion", "bosque",
    "ciudad", "calle", "puente", "parque", "meseta", "biblioteca", "mariposa", "elefante", "arrecife",
    "universidad", "amabilidad", "ventilador", "arquitecto", "cascabeles", "trastero", "tristeza",
    "naturaleza", "estrategia", "gratificante", "pelota", "imprimir", "paraguas", "nevera", "campo"
    "sostenible", "tranquilidad", "error", "zapatillas", "corresponsal", "cordillera", "escuela"]
    while jugar_de_nuevo:
        # Selecciona una palabra al azar de la lista
        palabra_seleccionada = obtener_palabra_aleatoria(palabras)
        letras_intentadas = []  # Lista para almacenar las letras que el jugador ha intentado
        intentos_fallidos = 0   # Contador de intentos fallidos
        maximo_de_intentos = 6        # Número máximo de intentos permitidos antes de perder

        # Crea una representación de la palabra con guiones bajos para las letras no adivinadas
        tablero = ['_'] * len(palabra_seleccionada)

        print('¡Bienvenido al juego del Ahorcado!')

        # Bucle principal del juego que continúa hasta que se cumpla una condición de fin
        while intentos_fallidos < maximo_de_intentos and '_' in tablero:
            # Muestra el estado actual del ahorcado y del tablero al jugador
            dibujar_ahorcado(intentos_fallidos)
            print('Palabra: ' + ' '.join(tablero))
            print('Letras intentadas: ' + ', '.join(letras_intentadas))
            # Solicita al jugador que ingrese una letra
            letra = input('Introduce una letra: ').lower()

            # Verifica que el jugador haya ingresado un solo carácter y que sea alfabético
            if len(letra) != 1 or not letra.isalpha():
                print('Por favor, introduce una sola letra.')
                continue  # Vuelve al inicio del bucle para una nueva entrada

            # Verifica si la letra ya ha sido intentada anteriormente
            if letra in letras_intentadas:
                print('Ya has adivinado esa letra. Intenta con otra.')
                continue  # Vuelve al inicio del bucle

            # Añade la letra a la lista de letras intentadas
            letras_intentadas.append(letra)
            
            # Comprueba si la letra está en la palabra seleccionada
            if letra in palabra_seleccionada:
                print(f'¡Muy bien! La letra "{letra}" está en la palabra.')
                # Actualiza el tablero reemplazando los guiones bajos por la letra acertada
                for i, l in enumerate(palabra_seleccionada):
                    if l == letra:
                        tablero[i] = letra
            else:
                # Incrementa el contador de intentos fallidos si la letra no está en la palabra
                intentos_fallidos += 1
                print(f'La letra "{letra}" no está en la palabra. Te quedan {maximo_de_intentos - intentos_fallidos} intentos.')

        # Se muestra la etapa final del dibujo del ahorcado
        dibujar_ahorcado(intentos_fallidos)

        # Condición para determinar si el jugador ha ganado
        if '_' not in tablero:
            print('\n¡Felicidades! Has adivinado la palabra: ', palabra_seleccionada)
        else:
            # Condición para determinar si el jugador ha perdido
            print('\nLo siento, has perdido. La palabra era: ', palabra_seleccionada)
        # Preguntar al jugador si desea otra partida
        respuesta = input("¿Quieres jugar otra vez? (s/n): ")
        if respuesta.lower() != "s":
            break
    print("¡Gracias por jugar!. ¡Vuelve cuándo quieras!")
# Punto de entrada del programa que inicia el juego
if __name__ == '__main__':
    juego_ahorcado()
