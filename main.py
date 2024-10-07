from src.piedra_papel_tijera import PiedraPapelTijera
from src.tres_en_raya import TresEnRaya
from src.ahorcado import Ahorcado
from src.preguntados import Preguntados


def mostrar_menu():
    print("###################################################")
    print("#                                                 #")
    print("#       ¡¡BIENVENIDO A RETROJUEGOS SALÓN!!        #")
    print("# JUEGA A 4 CLÁSICOS JUEGOS PARA TODAS LAS EDADES #")                               
    print("#                                                 #")
    print("###################################################")
    print("#                                                 #")
    print("#        ✨  ELIGE TU JUEGO FAVORITO  ✨         #")
    print("#                                                 #")
    print("#        1.- Ahorcado                             #")
    print("#        2.- Piedra, Papel, Tijera                #")                           
    print("#        3.- Tres en Raya                         #")
    print("#        4.- Preguntados                          #")
    print("#        5️.- Salir                                #")
    print("#                                                 #")
    print("###################################################")
    print("🚀     ¡Elige tu opción y empieza a jugar!      🚀")

def main():
    while True:
        eleccion = 0
        mostrar_menu()
        try:
            juego_elegido = int(input("\nElija el número del juego al que quiera jugar: "))
        
            if juego_elegido == 5:
                print("Gracias por jugar con nosotros. Esperamos que vuelva pronto​\n")
                break

            elif juego_elegido == 1:
                eleccion = Ahorcado().jugar()
                
            elif juego_elegido == 2:
                eleccion = PiedraPapelTijera().jugar()
                pass
            elif juego_elegido == 3:
                eleccion = TresEnRaya().jugar()
                

            elif juego_elegido == 4:
                eleccion = Preguntados().jugar()
                pass

            else:
                print("\nPor favor introduzca un número comprendido entre 1 y 5.")

            if eleccion == 2:
                print("Gracias por jugar con nosotros. Esperamos que vuelva pronto​\n")
                break

        except ValueError:
            print("Por favor ingrese un número entre 1 y 5.\n")
            main()



if __name__ == "__main__":
    main()