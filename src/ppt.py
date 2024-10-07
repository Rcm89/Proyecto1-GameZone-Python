import random

class PiedraPapelTijera:
    def __init__(self):
        """
        Constructor de la clase JuegoPPT.
        
        Inicializa los marcadores de puntaje para el jugador y la máquina.
        """
        # Inicializar los marcadores de jugador y máquina
        self.marcador_jugador = 0
        self.marcador_maquina = 0

    def mostrar_mensaje_bienvenida(self):
        """
        Muestra un mensaje de bienvenida al jugador con las opciones disponibles.
        """
        print("¡Bienvenido al juego!")
        print("Puedes elegir entre dos versiones:")
        print("1.- La de los boomers: Piedra-Papel-Tijera")
        print("2.- La de los frikis: Piedra-Papel-Tijera-Lagarto-Spock")

    def seleccionar_version(self):
        """
        Solicita al jugador que elija entre las dos versiones del juego y configura las reglas en consecuencia.
        
        Returns:
            Tuple[List[str], Dict[str, str], Dict[str, List[str]]]: Una tupla que contiene:
                - opciones (List[str]): Lista de opciones válidas en minúsculas.
                - opciones_mostrar (Dict[str, str]): Diccionario para mostrar las opciones con Spock con la s mayúscula.
                - vencedor_reglas (Dict[str, List[str]]): Diccionario que define las reglas del juego.
        """
        while True:
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
                print("\nHas seleccionado: Piedra-Papel-Tijera")
                return opciones, opciones_mostrar, vencedor_reglas
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
                print("\nHas seleccionado: Piedra-Papel-Tijera-Lagarto-Spock")
                return opciones, opciones_mostrar, vencedor_reglas
            else:
                # Mensaje de error si la elección no es válida
                print("Selección inválida. Por favor, introduce 1 o 2.")

    def obtener_eleccion_jugador(self, opciones, opciones_mostrar):
        """
        Solicita al jugador que elija una opción válida entre las disponibles.
        
        Parámetros:
            opciones (List[str]): Lista de opciones válidas en minúsculas.
            opciones_mostrar (Dict[str, str]): Diccionario para mostrar las opciones con Spock con la S mayúscula.
        
        Retorna:
            str: La elección del jugador en minúsculas.
        """
        while True:
            try:
                # Crear una cadena con las opciones disponibles para mostrar
                opciones_texto = ', '.join(map(opciones_mostrar.get, opciones))
                eleccion_jugador = input(f"\nElige una opción ({opciones_texto}): ").strip()
                eleccion_jugador_lower = eleccion_jugador.lower()  # Convertir la elección a minúsculas
                if eleccion_jugador_lower not in opciones:
                    raise ValueError("Tienes que elegir entre las opciones presentadas.")
                return eleccion_jugador_lower
            except ValueError as e:
                # Mostrar el mensaje de error y solicitar nuevamente la entrada
                print(e)

    def obtener_eleccion_maquina(self, opciones):
        """
        Genera una elección aleatoria para la máquina.
        
        Parámetros:
            opciones (List[str]): Lista de opciones válidas en minúsculas.
        
        Retorna:
            str: La elección de la máquina en minúsculas.
        """
        return random.choice(opciones)

    def determinar_ganador_ronda(self, eleccion_jugador, eleccion_maquina, vencedor_reglas):
        """
        Determina el ganador de la ronda comparando las elecciones del jugador y de la máquina según las reglas.
        
        Parámetros:
            eleccion_jugador (str): Elección del jugador en minúsculas.
            eleccion_maquina (str): Elección de la máquina en minúsculas.
            vencedor_reglas (Dict[str, List[str]]): Diccionario que define las reglas del juego.
        
        Retorna:
            str: 'empate' si hay empate, 'jugador' si el jugador gana la ronda, 'maquina' si la máquina gana la ronda.
        """
        if eleccion_jugador == eleccion_maquina:
            return 'empate'
        elif eleccion_maquina in vencedor_reglas[eleccion_jugador]:
            return 'jugador'
        else:
            return 'maquina'

    def mostrar_marcador(self, marcador_jugador, marcador_maquina):
        """
        Muestra el marcador actual de ambos jugadores.
        
        Parámetros:
            marcador_jugador (int): Número de victorias del jugador.
            marcador_maquina (int): Número de victorias de la máquina.
        """
        print(f"Marcador -> Jugador: {marcador_jugador} | Máquina: {marcador_maquina}\n")

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
    
    def jugar(self):
        """
        Función principal que controla el flujo del juego.
        
        Permite al jugador elegir entre dos versiones del juego, maneja el juego hasta que
        uno de los jugadores alcanza 3 victorias, y gestiona la repetición o finalización del juego.
        """
        while True:
            # Mostrar el mensaje de bienvenida y opciones
            self.mostrar_mensaje_bienvenida()
            
            # Seleccionar la versión del juego y obtener las configuraciones correspondientes
            opciones, opciones_mostrar, vencedor_reglas = self.seleccionar_version()
            
            print("\nGana el primero que alcance 3 victorias.\n")
            
            # Reiniciar los marcadores para una nueva partida
            self.marcador_jugador = 0
            self.marcador_maquina = 0
            
            # Bucle principal del juego hasta que uno de los jugadores alcance 3 victorias
            while self.marcador_jugador < 3 and self.marcador_maquina < 3:
                # Obtener la elección del jugador y la máquina
                eleccion_jugador = self.obtener_eleccion_jugador(opciones, opciones_mostrar)
                eleccion_maquina = self.obtener_eleccion_maquina(opciones)
                eleccion_maquina_mostrar = opciones_mostrar[eleccion_maquina]
                print(f"\nLa máquina ha elegido: {eleccion_maquina_mostrar}")
                
                # Determinar el ganador de la ronda
                ganador_ronda = self.determinar_ganador_ronda(eleccion_jugador, eleccion_maquina, vencedor_reglas)
                
                # Actualizar los marcadores según el resultado de la ronda
                if ganador_ronda == 'empate':
                    print("¡Esta ronda acaba en empate!")
                elif ganador_ronda == 'jugador':
                    print("¡Has ganado esta ronda!")
                    self.marcador_jugador += 1
                else:
                    print("¡La máquina gana esta ronda!")
                    self.marcador_maquina += 1
                
                # Mostrar el marcador actualizado
                self.mostrar_marcador(self.marcador_jugador, self.marcador_maquina)
            
            # Determinar y mostrar el ganador final del juego
            if self.marcador_jugador == 3:
                print("¡Felicidades! ¡Eres el ganador!\n")
            else:
                print("Lo siento, ha ganado la máquina.\n")
            
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

"""# Punto de entrada del script
if __name__ == "__main__":
    juego = PiedraPapelTijera()  # Crear una instancia del juego
    juego.jugar()       # Iniciar el juego
"""