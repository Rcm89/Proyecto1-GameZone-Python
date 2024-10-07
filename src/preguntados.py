import random

class Preguntados:
    def __init__(self):
        """
        Constructor de la clase JuegoPreguntados.
        
        Inicializa los atributos necesarios para el juego:
        - preguntas: Diccionario de preguntas categorizadas.
        - preguntas_realizadas: Lista para rastrear preguntas ya realizadas.
        - contador_aciertos: Contador de respuestas correctas consecutivas.
        """
        self.preguntas = self.obtener_preguntas()
        self.preguntas_realizadas = []
        self.contador_aciertos = 0

    def obtener_preguntas(self):
        """
        Devuelve el diccionario de preguntas y respuestas categorizadas.
        
        Returns:
            dict: Diccionario con categorías como claves y listas de preguntas como valores.
        """
        return {            
    'Historia': [
    {'Pregunta': '¿Cuánto duró la Guerra de los Cien Años?', 'Respuestas': {'a) 101': False, 'b) 100': True, 'c) 116': False, 'd) 99': False}},
    {'Pregunta': '¿En qué año se descubrió América?', 'Respuestas': {'a) 1492': True, 'b) 1501': False, 'c) 1212': False, 'd) 11776': False}},
    {'Pregunta': '¿Quién fue el primer presidente de la democracia española tras el franquismo?', 'Respuestas': {'a) Adolfo Suarez': True, 'b) Felipe Gonzalez': True, 'c) Florentino Perez': False, 'd) Jose María Aznar': False}},
    {'Pregunta': '¿Quién fue el responsable de la Reforma Protestante?', 'Respuestas': {'a) Martín Lutero': True, 'b) Juan Calvino': False, 'c) Enrique VIII': False, 'd) Francisco de Asís': False}},
    {'Pregunta': '¿Cuándo cayó el Muro de Berlín?', 'Respuestas': {'a) 1979': False, 'b) 1990': False, 'c) 1989': True, 'd) 1985': False}},
    {'Pregunta': '¿Qué reina inglesa fue conocida como "La reina virgen"?', 'Respuestas': {'a) Isabel I': True, 'b) María I': False, 'c) Isabel II': False, 'd) Ana Bolena': False}},
    {'Pregunta': '¿En qué año comenzó la Primera Guerra Mundial?', 'Respuestas': {'a) 1934': False, 'b) 1918': False, 'c) 1939': False, 'd) 1914': True}},
    {'Pregunta': '¿Quién lideró la Revolución Rusa de 1917?', 'Respuestas': {'a) Lenin': True, 'b) Stalin': False, 'c) Lenin': False, 'd) Gorbachov': False}},
    {'Pregunta': '¿En qué año llegó el hombre a la Luna?', 'Respuestas': {'a) 1969': True, 'b) 1959': False, 'c) 1968': False, 'd) 1972': False}},
    {'Pregunta': '¿Quién fue el dictador de Alemania durante la Segunda Guerra Mundial?', 'Respuestas': {'a) Adolf Hitler': True, 'b) Benito Mussolini': False, 'c) Joseph Stalin': False, 'd) Francisco Franco': False}},
    {'Pregunta': '¿Cuál era el nombre del barco en el que viajó Cristóbal Colón?', 'Respuestas': {'a) La Santa María': True, 'b) La Pinta': False, 'c) La Niña': False, 'd) Mayflower': False}},
    {'Pregunta': '¿En qué país ocurrió la Revolución Cultural?', 'Respuestas': {'a) México':False, 'b) Rusia': False, 'c) Francia': False, 'd) China': True}},
    {'Pregunta': '¿Qué dinastía gobernó China por más tiempo?', 'Respuestas': {'a) Han': False, 'b) Qing': True, 'c) Ming': False, 'd) Tang': False}},
    {'Pregunta': '¿Quién fue el faraón egipcio que construyó la Gran Pirámide de Giza?', 'Respuestas': {'a) Keops': True, 'b) Tutankamón': False, 'c) Ramsés II': False, 'd) Cleopatra': False}},
    {'Pregunta': '¿Qué país fue invadido por Alemania para dar inicio a la Segunda Guerra Mundial?', 'Respuestas': {'a) Polonia': True, 'b) Francia': False, 'c) Reino Unido': False, 'd) Checoeslovaquia': False}},
    {'Pregunta': '¿Quién fue el líder del movimiento independentista de la India?', 'Respuestas': {'a) Mahatma Gandhi': True, 'b) Jawaharlal Nehru': False, 'c) Subhas Chandra Bose': False, 'd) Indira Gandhi': False}},
    {'Pregunta': '¿Qué país fue el primero en abolir la esclavitud?', 'Respuestas': {'a) Haití': True, 'b) Estados Unidos': False, 'c) Reino Unido': False, 'd) Francia': False}},
    {'Pregunta': '¿Quién fue el último zar de Rusia?', 'Respuestas': {'a) Iván el Terrible': False, 'b) Pedro el Grande': False, 'c) Alejandro III': False, 'd) Nicolás II': True}},
    {'Pregunta': '¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?', 'Respuestas': {'a) 1776': True, 'b) 1783': False, 'c) 1804': False, 'd) 1812': False}},
    {'Pregunta': '¿Qué civilización construyó Machu Picchu?', 'Respuestas': {'a) Los Incas': True, 'b) Los Mayas': False, 'c) Los Aztecas': False, 'd) Los Olmecas': False}}
  ],
  'Cultura General': [
    {'Pregunta': '¿Cual es la montaña mas alta?', 'Respuestas': {'a) K2': False, 'b) Titanic': True, 'c) Mont Blanc': False, 'd) Acongcagua': False}},
    {'Pregunta': '¿Cuál es el país más grande del mundo?', 'Respuestas': {'a) Rusia': True, 'b) Canadá': False, 'c) China': False, 'd) Estados Unidos': False}},
    {'Pregunta': '¿Cuál es el idioma más hablado del mundo?', 'Respuestas': {'a) Inglés': False, 'b) Mandarín': True, 'c) Español': False, 'd) Hindi': False}},
    {'Pregunta': '¿Cuál es el país más pequeño de Europa?', 'Respuestas': {'a) Monaco': False, 'b) San Marino': False, 'c) Andorra': False, 'd) El Vaticano': True}},
    {'Pregunta': '¿Cuál es el río más largo del mundo?', 'Respuestas': {'a) Nilo': True, 'b) Amazonas': False, 'c) Danubio': False, 'd) Misisipi': False}},
    {'Pregunta': '¿Cuál es el país más poblado del mundo?', 'Respuestas': {'a) China': True, 'b) India': False, 'c) Estados Unidos': False, 'd) Brasil': False}},
    {'Pregunta': '¿Qué país tiene la mayor cantidad de pirámides?', 'Respuestas': {'a) Egipto': False, 'b) Perú': False, 'c) México': False, 'd) Sudán': True}},
    {'Pregunta': '¿Cuántos planetas hay en el sistema solar?', 'Respuestas': {'a) 8': True, 'b) 9': False, 'c) 7': False, 'd) 10': False}},
    {'Pregunta': '¿Quién pintó "La última cena"?', 'Respuestas': {'a) Leonardo da Vinci': True, 'b) Pablo Picasso': False, 'c) Miguel Ángel': False, 'd) Salvador Dalí': False}},
    {'Pregunta': '¿Cuál es la capital de Japón?', 'Respuestas': {'a) Tokio': True, 'b) Kioto': False, 'c) Osaka': False, 'd) Hiroshima': False}},
    {'Pregunta': '¿Qué país es conocido por la Torre Eiffel?', 'Respuestas': {'a) Francia': True, 'b) Italia': False, 'c) Alemania': False, 'd) España': False}},
    {'Pregunta': '¿Cuántos continentes hay en la Tierra?', 'Respuestas': {'a) 7': True, 'b) 5': False, 'c) 6': False, 'd) 8': False}},
    {'Pregunta': '¿Que signfica la frase "Alea iacta est"?', 'Respuestas': {'a) La suerte está echada': True, 'b) ¡Padre, por qué me has abandonado':False, 'c) La fortuna sonríe a los audaces': False, 'd) Y sin embargo, se mueve': False}},
    {'Pregunta': '¿Cuál es el animal terrestre más rápido?', 'Respuestas': {'a) Guepardo': True, 'b) León': False, 'c) Águila': False, 'd) Caballo': False}},
    {'Pregunta': '¿Qué país tiene la mayor cantidad de islas?', 'Respuestas': {'a) Suecia': True, 'b) Noruega': False, 'c) Canadá': False, 'd) Indonesia': False}},
    {'Pregunta': '¿Quién escribió "Don Quijote de la Mancha"?', 'Respuestas': {'a) William Shakespeare': False, 'b) Gabriel García Márquez': False, 'c) Miguel de Cervantes': True, 'd) Federico García Lorca': False}},
    {'Pregunta': '¿Qué órgano del cuerpo humano consume más energía?', 'Respuestas': {'a) El cerebro': True, 'b) El corazón': False, 'c) El hígado': False, 'd) Los pulmones': False}},
    {'Pregunta': '¿Cuál es el metal más abundante en la corteza terrestre?', 'Respuestas': {'a) Aluminio': True, 'b) Hierro': False, 'c) Oro': False, 'd) Cobre': False}},
    {'Pregunta': '¿Cuál es el océano más grande del mundo?', 'Respuestas': {'a) Antártico': False, 'b) Atlántico': False, 'c) Índico': False, 'd) Pacífico': True}},
    {'Pregunta': '¿Qué continente es conocido como "el continente blanco"?', 'Respuestas': {'a) Antártida': True, 'b) Europa': False, 'c) África': False, 'd) Oceanía': False}}
  ],
  'Entretenimiento': [
    {'Pregunta': '¿Quién interpretó a Jack en la película "Titanic"?', 'Respuestas': {'a) Brad Pitt': False, 'b) Leonardo DiCaprio': True, 'c) Johnny Depp': False, 'd) Tom Hanks': False}},
    {'Pregunta': '¿Cuál es el superhéroe que tiene como alter ego a Clar Kent?', 'Respuestas': {'a) Batman': False, 'b) Hulk': False, 'c) Spiderman': False, 'd) Superman': True}},
    {'Pregunta': '¿En qué ciudad se encuentra el parque de atracciones Disneyland?', 'Respuestas': {'a) Anaheim': True, 'b) Orlando': False, 'c) París': False, 'd) Tokio': False}},
    {'Pregunta': '¿Cuál es la saga de películas más taquillera de la historia?', 'Respuestas': {'a) Avengers': True, 'b) Star Wars': False, 'c) Harry Potter': False, 'd) El Señor de los Anillos': False}},
    {'Pregunta': '¿Quién es el creador de la serie animada "Los Simpson"?', 'Respuestas': {'a) Matt Groening': True, 'b) Seth MacFarlane': False, 'c) Trey Parker': False, 'd) Mike Judge': False}},
    {'Pregunta': '¿Qué famoso personaje de videojuegos es conocido por recolectar anillos?', 'Respuestas': {'a) Sonic': True, 'b) Mario': False, 'c) Donkey Kong': False, 'd) Link': False}},
    {'Pregunta': '¿Cuál es el grupo musical que lanzó la canción "Bohemian Rhapsody"?', 'Respuestas': {'a) Queen': True, 'b) The Beatles': False, 'c) Led Zeppelin': False, 'd) Pink Floyd': False}},
    {'Pregunta': '¿Quién interpretó a Iron Man en las películas de Marvel?', 'Respuestas': {'a) Robert Downey Jr.': True, 'b) Chris Evans': False, 'c) Chris Hemsworth': False, 'd) Mark Ruffalo': False}},
    {'Pregunta': '¿En qué año se estrenó la película "Star Wars: Episodio IV – Una nueva esperanza"?', 'Respuestas': {'a) 1977': True, 'b) 1980': False, 'c) 1983': False, 'd) 1974': False}},
    {'Pregunta': '¿Cómo se llama el lugar donde viven los hobbits en "El Señor de los Anillos"?', 'Respuestas': {'a) La Comarca': True, 'b) Gondor': False, 'c) Mordor': False, 'd) Rohan': False}},
    {'Pregunta': '¿Cuál es el nombre de la escuela de magia en la saga "Harry Potter"?', 'Respuestas': {'a) Hogwarts': True, 'b) Beauxbatons': False, 'c) Durmstrang': False, 'd) Ilvermorny': False}},
    {'Pregunta': '¿Qué película ganó el premio Óscar a la mejor película en 2020?', 'Respuestas': {'a) Parásitos': True, 'b) Joker': False, 'c) 1917': False, 'd) Once Upon a Time in Hollywood': False}},
    {'Pregunta': '¿Qué famoso cantante es conocido como "El Rey del Pop"?', 'Respuestas': {'a) Michael Jackson': True, 'b) Elvis Presley': False, 'c) Prince': False, 'd) Freddie Mercury': False}},
    {'Pregunta': '¿Qué película animada cuenta la historia de una princesa llamada Elsa?', 'Respuestas': {'a) Frozen': True, 'b) Moana': False, 'c) Rapunzel': False, 'd) La Sirenita': False}},
    {'Pregunta': '¿Qué videojuego popular tiene personajes como Mario, Luigi y Bowser?', 'Respuestas': {'a) Super Mario': True, 'b) Sonic': False, 'c) Minecraft': False, 'd) Call of Duty': False}},
    {'Pregunta': '¿Qué director de cine es conocido por películas como "Inception" y "The Dark Knight"?', 'Respuestas': {'a) Christopher Nolan': True, 'b) Steven Spielberg': False, 'c) Quentin Tarantino': False, 'd) Martin Scorsese': False}},
    {'Pregunta': '¿Qué personaje de Disney pierde su zapatilla de cristal?', 'Respuestas': {'a) Cenicienta': True, 'b) Bella': False, 'c) Blanca Nieves': False, 'd) Ariel': False}},
    {'Pregunta': '¿Cuál es la serie más vista en la historia de Netflix?', 'Respuestas': {'a) Stranger Things': False, 'b) El juego del calamar': True, 'c) La Casa de Papel': False, 'd) The Crown': False}},
    {'Pregunta': '¿Cual de estas películas no dirigió Steven Spielberg?', 'Respuestas': {'a) Tiburón': False, 'b) Jurassic Park': False, 'c) Star Wars': True, 'd) E.T.': False}},
    {'Pregunta': '¿Qué famoso realizador dirigió El clu de la lucha?', 'Respuestas': {'a) Sam Mendes': False, 'b) Martin Scorsese': False, 'c) David Fincher': True, 'd) Steven Spielberg': False}}
  ],
  'Ciencia': [
    {'Pregunta': '¿Cuál es la fórmula química del agua?', 'Respuestas': {'a) H2O': True, 'b) CO2': False, 'c) O2': False, 'd) H2O2': False}},
    {'Pregunta': '¿Qué órgano del cuerpo humano bombea sangre?', 'Respuestas': {'a) El corazón': True, 'b) El hígado': False, 'c) Los pulmones': False, 'd) El cerebro': False}},
    {'Pregunta': '¿Quién desarrolló la teoría de la relatividad?', 'Respuestas': {'a) Isaac Newton': False, 'b) Albert Einstein': True, 'c) Galileo Galilei': False, 'd) Nikola Tesla': False}},
    {'Pregunta': '¿Cuál es la unidad básica de la vida?', 'Respuestas': {'a) El átomo': False, 'b) La célula': True, 'c) El tejido': False, 'd) El órgano': False}},
    {'Pregunta': '¿Cuál es el planeta más cercano al sol?', 'Respuestas': {'a) Mercurio': True, 'b) Venus': False, 'c) Tierra': False, 'd) Marte': False}},
    {'Pregunta': '¿Qué gas es esencial para la respiración humana?', 'Respuestas': {'a) Dióxido de carbono': False, 'b) Oxígeno': True, 'c) Nitrógeno': False, 'd) Helio': False}},
    {'Pregunta': '¿Qué teoría explica el origen de las especies?', 'Respuestas': {'a) La teoría de la evolución': True, 'b) La teoría del Big Bang': False, 'c) La teoría de la relatividad': False, 'd) La teoría de cuerdas': False}},
    {'Pregunta': '¿A que temperatura hierve el agua?', 'Respuestas': {'a) -100º': False, 'b) 0º': False, 'c) 100º': True, 'd) 73º': False}},
    {'Pregunta': '¿Qué tipo de célula es responsable de la transmisión de impulsos nerviosos?', 'Respuestas': {'a) Células epiteliales': False, 'b) Células sanguíneas': False, 'c) Células musculares': False, 'd)  Neuronas': True }},
    {'Pregunta': '¿Quién es conocido como el padre de la genética?', 'Respuestas': {'a) Charles Darwin': False, 'b) Gregor Mendel': True, 'c) Louis Pasteur': False, 'd) Thomas Edison': False}},
    {'Pregunta': '¿Qué fenómeno describe la fuerza que atrae a los objetos hacia la Tierra?', 'Respuestas': {'a) La inercia': False, 'b) La gravedad': True, 'c) La fricción': False, 'd) La tensión': False}},
    {'Pregunta': '¿Cuál es el metal más ligero?', 'Respuestas': {'a) Aluminio': False, 'b) Litio': True, 'c) Hierro': False, 'd) Plomo': False}},
    {'Pregunta': '¿Qué parte del ojo humano controla la cantidad de luz que entra?', 'Respuestas': {'a) La retina': False, 'b) La córnea': False, 'c) El iris': True, 'd) El cristalino': False}},
    {'Pregunta': '¿Cuál es el número atómico del Helio?', 'Respuestas': {'a) 1': False, 'b) 10': False, 'c) 7': False, 'd) 2': True}},
    {'Pregunta': '¿Qué es un átomo?', 'Respuestas': {'a) La unidad más pequeña de un elemento': True, 'b) Un tipo de molécula': False, 'c) Un tipo de célula': False, 'd) Un compuesto químico': False}},
    {'Pregunta': '¿Qué elemento químico tiene el símbolo O?', 'Respuestas': {'a) Oxígeno': True, 'b) Oro': False, 'c) Osmio': False, 'd) Ozono': False}},
    {'Pregunta': '¿Cuál es el area de un cuadrado de 4 cm de lado?', 'Respuestas': {'a) 12': False, 'b) 8': False, 'c) 32': False, 'd) 16': True}},
    {'Pregunta': '¿Qué tipo de animal es un delfín?', 'Respuestas': {'a) Un pez': False, 'b) Un mamífero': True, 'c) Un reptil': False, 'd) Un anfibio': False}},
    {'Pregunta': '¿Cuál es la capa más externa de la Tierra?', 'Respuestas': {'a) El núcleo': False, 'b) El manto': False, 'c) La corteza': True, 'd) El magma': False}},
    {'Pregunta': '¿Qué órgano produce la insulina?', 'Respuestas': {'a) El hígado': False, 'b) El páncreas': True, 'c) Los riñones': False, 'd) El corazón': False}}
  ]
    }

    def seleccionar_pregunta(self):
        """
        Selecciona aleatoriamente una pregunta que no haya sido realizada previamente.
        
        Returns:
            tuple: Categoría y la pregunta seleccionada.
        """
        while True:
            categoria = random.choice(list(self.preguntas.keys()))
            pregunta = random.choice(self.preguntas[categoria])
            if pregunta not in self.preguntas_realizadas:
                self.preguntas_realizadas.append(pregunta)
                return categoria, pregunta

    def plantear_pregunta(self, categoria, pregunta):
        """
        Presenta la pregunta y las opciones al usuario.
        
        Args:
            categoria (str): Categoría de la pregunta.
            pregunta (dict): Diccionario con la pregunta y respuestas.
        """
        print(f"\nCategoría: {categoria}")
        print(pregunta['Pregunta'])
        for opcion in pregunta['Respuestas']:
            print(opcion)

    def obtener_respuesta_usuario(self):
        """
        Solicita al usuario que ingrese su respuesta controlando que se introduzca de forma correcta
        
        Returns:
            str: La opción elegida por el usuario (a, b, c o d).
        """
        respuesta = input("Tu respuesta (a, b, c, d): ").lower()
        while respuesta not in ["a", "b", "c", "d"]:
            respuesta = input("Opción inválida. Por favor ingresa a, b, c o d: ").lower()
        return respuesta

    def verificar_respuesta(self, pregunta, respuesta_usuario):
        """
        Verifica si la respuesta del usuario es correcta.
        
        Args:
            pregunta (dict): Diccionario con la pregunta y respuestas.
            respuesta_usuario (str): La opción elegida por el usuario.
        
        Returns:
            tuple: (bool, str) Indica si es correcta y cuál es la opción correcta.
        """
        respuestas = pregunta['Respuestas']
        respuesta_correcta = ''
        es_correcta = False

        for opcion_texto, valor in respuestas.items():
            opcion = opcion_texto.split(')')[0]  # Extrae la letra de la opción
            if valor:
                respuesta_correcta = opcion
            if opcion == respuesta_usuario:
                es_correcta = valor

        return es_correcta, respuesta_correcta
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
        
        Permite al jugador jugar múltiples partidas, hasta que decida salir.
        En cada partida, el jugador intenta responder correctamente a 10 preguntas consecutivas.
        """
        print("¡Bienvenido al juego Preguntados!")
        jugar_de_nuevo = True

        while jugar_de_nuevo:
            self.contador_aciertos = 0
            self.preguntas_realizadas = []
            print("\nGana el primero que alcance 10 aciertos consecutivos. ¡Buena suerte!\n")

            # Bucle principal de la partida
            while self.contador_aciertos < 10:
                categoria, pregunta_seleccionada = self.seleccionar_pregunta()
                self.plantear_pregunta(categoria, pregunta_seleccionada)
                respuesta_usuario = self.obtener_respuesta_usuario()
                es_correcta, respuesta_correcta = self.verificar_respuesta(pregunta_seleccionada, respuesta_usuario)

                if es_correcta:
                    self.contador_aciertos += 1
                    print(f"¡Correcto! Llevas {self.contador_aciertos} acierto(s) consecutivo(s).")
                else:
                    print(f"Incorrecto. La respuesta correcta era la opción {respuesta_correcta}.")
                    print("Has perdido el juego.")
                    break

                # Verificar si el jugador ha ganado
                if self.contador_aciertos == 10:
                    print("¡Felicidades! Has respondido correctamente a 10 preguntas seguidas por lo que has ganado el juego.")

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

