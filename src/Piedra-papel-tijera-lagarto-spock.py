import random

def mostrar_mensaje_bienvenida():
    """Muestra un mensaje de bienvenida al jugador."""
    print("¡Bienvenido al juego!")
    print("Puedes elegir entre dos versiones:")
    print("1.-La de los boomers: Piedra-Papel-Tijera")
    print("2.-La de los frikis: Piedra-Papel-Tijera-Lagarto-Spock")

def obtener_eleccion_jugador(opciones, opciones_mostrar):
    """
    Solicita al jugador que elija una opción válida entre las de una lista 

    Parámetros:
    - opciones: lista de opciones válidas en minúsculas.
    - opciones_mostrar: diccionario para mostrar las opciones con Spock con la S mayúscula.

    Retorna:
    - eleccion_jugador_lower: la elección del jugador en minúsculas.
    """
    while True:
        try:
            opciones_texto = ', '.join(map(opciones_mostrar.get, opciones))
            eleccion_jugador = input(f"Elige una opción ({opciones_texto}): ").strip()
            eleccion_jugador_lower = eleccion_jugador.lower() # Leemos tambien en caso de que el usuario meta alguna letra mayuscula
            if eleccion_jugador_lower not in opciones:
                raise ValueError("Tienes que elegir entre las opciones presentadas.")
            return eleccion_jugador_lower
        except ValueError as e:
            print(e)

def obtener_eleccion_maquina(opciones):
    """Genera una elección aleatoria para la máquina."""
    return random.choice(opciones)

def determinar_ganador_ronda(eleccion_jugador, eleccion_maquina, vencedor_reglas):
    """
    Determina el ganador de la ronda comparando las elecciones de jugador y maquina de acuerdo a las reglas.

    Parámetros:
    - eleccion_jugador: elección del jugador en minúsculas.
    - eleccion_maquina: elección de la máquina en minúsculas.
    - vencedor_reglas: diccionario con las reglas del juego.

    Retorna:
    - 'empate' si hay empate.
    - 'jugador' si el jugador gana la ronda.
    - 'maquina' si la máquina gana la ronda.
    """
    if eleccion_jugador == eleccion_maquina:
        return 'empate'
    elif eleccion_maquina in vencedor_reglas[eleccion_jugador]:
        return 'jugador'
    else:
        return 'maquina'

def mostrar_marcador(marcador_jugador, marcador_maquina):
    """Muestra la marcador actual de ambos jugadores."""
    print(f"Marcador -> Jugador: {marcador_jugador} | Máquina: {marcador_maquina}\n")

def jugar_ppt():
    """Función principal que controla el flujo del juego."""
    while True:
        mostrar_mensaje_bienvenida()
        # Se pregunta al usuario qué versión quiere jugar y se obliga a que introduzca 1 o 2
        version_valida = False
        while not version_valida:
            eleccion_version = input("Introduce 1 o 2 según tu elección: ").strip()
            if eleccion_version == '1':
                # Configuración para Piedra-Papel-Tijera
                opciones = ['piedra', 'papel', 'tijera']
                opciones_mostrar = {
                    'piedra': 'piedra',
                    'papel': 'papel',
                    'tijera': 'tijera'
                }
                vencedor_reglas = {
                    'piedra': ['tijera'],
                    'papel': ['piedra'],
                    'tijera': ['papel']
                }
                version_valida = True
            elif eleccion_version == '2':
                # Configuración para Piedra-Papel-Tijera-Lagarto-Spock
                opciones = ['piedra', 'papel', 'tijera', 'lagarto', 'spock']
                opciones_mostrar = {
                    'piedra': 'piedra',
                    'papel': 'papel',
                    'tijera': 'tijera',
                    'lagarto': 'lagarto',
                    'spock': 'Spock'
                }
                vencedor_reglas = {
                    'piedra': ['tijera', 'lagarto'],
                    'papel': ['piedra', 'spock'],
                    'tijera': ['papel', 'lagarto'],
                    'lagarto': ['spock', 'papel'],
                    'spock': ['tijera', 'piedra']
                }
                version_valida = True
            else:
                print("Selección inválida. Por favor, Introduce 1 o 2.")

        print("Gana el primero que alcance 3 victorias.")

        # Inicializar los marcadores de jugador y maquina
        marcador_jugador = 0
        marcador_maquina = 0

        # Bucle principal del juego
        while marcador_jugador < 3 and marcador_maquina < 3:
            eleccion_jugador = obtener_eleccion_jugador(opciones, opciones_mostrar)
            eleccion_maquina = obtener_eleccion_maquina(opciones)
            eleccion_maquina_mostrar = opciones_mostrar[eleccion_maquina]
            print(f"La máquina ha elegido: {eleccion_maquina_mostrar}")

            ganador_ronda = determinar_ganador_ronda(eleccion_jugador, eleccion_maquina, vencedor_reglas)

            if ganador_ronda == 'empate':
                print("¡Esta ronda acaba en empate!")
            elif ganador_ronda == 'jugador':
                print("¡Has ganado esta ronda!")
                marcador_jugador += 1
            else:
                print("¡La máquina gana esta ronda!")
                marcador_maquina += 1

            mostrar_marcador(marcador_jugador, marcador_maquina)

        # Determinar y mostrar el ganador del juego
        if marcador_jugador == 3:
            print("¡Felicidades! ¡Eres el ganador!")
        else:
            print("Lo siento, ha ganado la maquina")

        # Preguntar al jugador si quiere jugar otra vez
        respuesta = input("¿Quieres jugar otra vez (s/n): ")
        if respuesta.lower() != "s":
            break
    print("¡Gracias por jugar! ¡Vuelve cuando quieras!")

# Iniciar el juego
if __name__ == "__main__":
    jugar_ppt()
