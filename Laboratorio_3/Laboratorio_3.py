import random

def jugar_dados():
    jugar = "s"
    while jugar == "s":
        print("=== SIMULADOR DE DADOS ===")
        
        print("Modos: 1 - Un dado | 2 - Dos dados")
        modo = int(input("Selecciona modo: "))
        rondas = int(input("¿Cuántas rondas? "))
        
        victorias = 0
        derrotas = 0
        
        for i in range(1, rondas + 1):
            print(f"\n--- Ronda {i} ---")
            
            match modo:
                case 1:
                    dado1 = random.randint(1, 6)
                    print(f"Dado: {dado1}")
                    if dado1 >= 4:
                        print("¡Ganaste esta ronda!")
                        victorias += 1
                    else:
                        print("Perdiste esta ronda.")
                        derrotas += 1
                        
                case 2:
                    dado1 = random.randint(1, 6)
                    dado2 = random.randint(1, 6)
                    suma = dado1 + dado2
                    print(f"Dado1: {dado1} | Dado2: {dado2} | Suma: {suma}")
                    if suma >= 7:
                        print("¡Ganaste esta ronda!")
                        victorias += 1
                    else:
                        print("Perdiste esta ronda.")
                        derrotas += 1

        print(f"\n=== Victorias: {victorias} | Derrotas: {derrotas} ===")
        
        if victorias > derrotas:
            print("¡Ganaste la sesión!")
        elif derrotas > victorias:
            print("Perdiste la sesión.")
        else:
            print("¡Empate!")
        
        jugar = input("\n¿Jugar de nuevo? (s/n): ")

    print("¡Gracias por jugar!")

jugar_dados()