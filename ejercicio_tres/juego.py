class Juego:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def jugar(self):
        print(
            f"Comienza el juego. Jugador 1: {self.jugador1.luchador}, Jugador 2: {self.jugador2.luchador}")
        jugador_actual = self.jugador1
        while self.jugador1.vida > 0 and self.jugador2.vida > 0:
            if jugador_actual == self.jugador1:
                jugador_objetivo = self.jugador2
            else:
                jugador_objetivo = self.jugador1
            print(f"Turno de {jugador_actual.nombre}")
            jugador_objetivo.recibir_golpe()
            jugador_actual = jugador_objetivo

        print("Fin del juego.")
        if self.jugador1.vida > 0:
            print(f"Gana el jugador 1 ({self.jugador1.nombre})")
        else:
            print(f"Gana el jugador 2 ({self.jugador2.nombre})")
